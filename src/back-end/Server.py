from flask import Flask, render_template, request, jsonify
import DBAccess as dba
import DBAdapter as db
import json
import numpy as np
from Prediction import predict
from utils import *

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend/static')
conn = dba.connect_to_db()
active_groups = {} # map of UUID map of user-ids to obj of selections of all users, will be moved to processed order once all have voted

def generate_prediction(user_likes, user_dislikes, user_id):
    """
    Generates a list of recipe ids, which the user might like
    :param user_likes: list of recipe ids the user likes
    :param user_dislikes: list of recipe ids the user dislikes
    :param user_id: user id
    :return: list of recipe ids to suggest to user
    """
    recipes = db.get_recipes(conn)
    r_count = len(recipes)

    mat = create_pref_mat(conn, r_count)
    user_vec = np.array(join_encoding_vec(user_likes, user_dislikes, r_count))

    mask = create_filter_mask(conn, user_id, r_count)
    user_vec = np.reshape(user_vec, (1, -1))
    return predict(mat, user_vec, mask, 8, 4)


def generate_group_prediction(user_ids, suggestions_per_group=2, group_size=4):
    """
    Generates a list of recipe ids, which the user might like
    :param user_ids: list of user ids
    :param suggestions_per_group: number of suggestions per group
    :param group_size: number of users per group
    """
    recipes = db.get_recipes(conn)
    r_count = len(recipes)

    users_vec = {}
    for user in user_ids:
        users_vec[user] = np.array(join_encoding_vec(db.get_user_likes(conn, user), db.get_user_dislikes(conn, user), r_count))

    remaining_users = user_ids
    ids_per_group = []
    for i in range(group_size):
        if i == group_size-1:
            ids_per_group.append(remaining_users)
            break
        base_user = remaining_users[0]
        idx = k_closest_vector_indices(users_vec[base_user], [users_vec[us] for us in remaining_users], group_size+1)
        ids_per_group.append(remaining_users[idx])
        remaining_users = [remaining_users[i] for i in range(len(remaining_users)) if i not in idx]

    mat = create_pref_mat(conn, r_count)
    pred_per_group = []
    for user_group in ids_per_group:
        mask = create_filter_mask_group(conn, user_group, r_count)
        vec = np.mean(np.vstack([users_vec[i] for i in user_group]), axis=0)
        pred_per_group.append(predict(mat, vec, mask, suggestions_per_group, 4))

    return flatten_list(pred_per_group)



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/create-group', methods=['GET', 'POST'])
def create_group():
    if request.method == 'GET':
        return render_template('template_group.html')
    if request.method == 'POST':
        data = request.get_json()
        user_ids = data['users']
        uuid = generate_url_safe_uuid()
        obj = {user_id: {'selected': False, 'selection': ''} for user_id in user_ids}
        active_groups[uuid] = obj
        return f"{uuid}"


@app.route('/predict', methods=['GET'])
def get_prediction():
    data = request.get_json()
    user_id = data['user-id']
    liked_rid = data['user-likes']
    disliked_rid = data['user-dislikes']
    pred_r_ids = generate_prediction(liked_rid, disliked_rid, user_id)
    recs = db.get_recipes_for_user(conn, user_id)
    result = [rec for rec in recs if rec['id'] in pred_r_ids]
    return json.dumps(result)


@app.route('/predict/<str:uuid>', methods=['GET'])
def get_prediction_group(uuid):
    data = request.get_json()
    user_ids = data['user-ids']
    pred_r_ids = generate_group_prediction(user_ids)
    recs = db.get_recipes_for_users(conn, user_ids)
    result = [rec for rec in recs if rec['id'] in pred_r_ids]
    return json.dumps(result)


@app.route('/groups/data/<str:uuid>', methods=['GET', 'POST'])
def group_data(uuid):
    if uuid not in active_groups.keys():
        return "Page does not exist."

    if request.method == 'GET':
        return json.dumps(active_groups.get(uuid, {}))
    else:
        data = request.get_json()
        user_name = data['user-name']
        rec_id = data['rec-id']
        pw = data['pw']

        user_id = db.get_user_id(conn, user_name, pw)
        if user_id is None:
            return "User does not exist"
        if user_id not in active_groups[uuid].keys():
            return "User is not in group"

        active_groups[uuid][user_id]['selected'] = True
        active_groups[uuid][user_id]['selection'] = rec_id
        return "Operation Successful"


@app.route('/groups/<str:uuid>', methods=['GET'])
def show_group(uuid):
    if uuid in active_groups.keys():
        return render_template("template_group_view.html")
    else:
        return "Does not exist"


@app.route('/fetch-recipies', methods=['GET'])
def fetchRecipies():
    return 'fetch recipies'


@app.route('/create-user', methods=['GET'])
def create_user():
    return render_template("template_create_user.html")


@app.route('/setPreferences', methods=['POST'])
def setPreferences():
    """
    Set the preferences (allergies) for a user
    :param user_id: user id
    :param allergies: list of allergies (ids)
    """
    data = request.get_json()
    user_id = data['user_id']
    allergies = data['allergies']
    db.set_allergies_for_user(user_id, allergies)
    return 'set prefs'


@app.route('/favorRecipe', methods=['POST'])
def favorRecipe():
    """
    This endpoint lets a user add a like to a recipe 
    :param user_id: user id
    :param recipe_id: recipe id
    """
    data = request.get_json()
    user_id = data['user_id']
    recipe_id = data['recipe_id']
    db.user_add_like(conn, user_id, recipe_id)
    return 'fav recipe'


@app.route('/get-users', methods=['GET'])
def get_users():
    data = [(id, name) for id, name, _ in db.load_all_users(conn)]
    obj = {'users': [{'name': name, 'id': id} for id, name in data]}
    return json.dumps(obj)


@app.route('/get-user', methods=['GET'])
def getUser():
    """
    This endpoint is a simple mock endpoint to facilitate account management
    :param user_id: user id
    :param user_pw: user password
    :return: user id
    """
    data = request.get_json()
    user_name = data['user_name']
    user_pw = data['user_pw']
    user_id = db.get_user_id(conn, user_name, user_pw)
    return json.dumps({'user_id': user_id})


@app.route('/set-user', methods=['POST'])
def set_user():
    """
    This endpoint is used to mock user account creation
    :param user_name: user name
    :param user_pw: user password
    :return: status incicating if creating was successful
    """
    # Check if the request has JSON data
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()

    # Validate 'user_name' and 'user_pw' in the data
    user_name = data.get('user_name')
    user_pw = data.get('user_pw')
    if not user_name or not user_pw:
        return jsonify({"error": "Missing username or password"}), 400

    try:
        # Insert user data into the database
        db.insert_user(conn, user_name, user_pw)
        return jsonify({"message": "User set successfully"}), 201
    except Exception as e:
        # Handle any exceptions (e.g., database errors)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

