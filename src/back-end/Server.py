from flask import Flask, render_template, request, jsonify
import DBAccess as dba
import DBAdapter as db
import json
import numpy as np
from collections import defaultdict
from Prediction import predict
from utils import *

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend/static')
conn = dba.connect_to_db()


def generate_prediction(user_likes, user_dislikes, user_id):
    recipes = db.get_recipes(conn)
    r_count = len(recipes)

    mat = create_pref_mat(conn, r_count)
    user_vec = np.array(join_encoding_vec(user_likes, user_dislikes, r_count))

    mask = create_filter_mask(conn, user_id, r_count)
    user_vec = np.reshape(user_vec, (1, -1))
    return predict(mat, user_vec, mask, 8, 4)


def generate_group_prediction(user_ids, suggestions_per_group=2, group_size=4):
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


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/fetch-recipies', methods=['GET'])
def fetchRecipies():
    return 'fetch recipies'


@app.route('/setPreferences', methods=['POST'])
def setPreferences():
    data = request.get_json()
    user_id = data['user_id']
    allergies = data['allergies']
    db.set_allergies_for_user(user_id, allergies)
    return 'set prefs'


@app.route('/favorRecipe', methods=['POST'])
def favorRecipe():
    data = request.get_json()
    user_id = data['user_id']
    recipe_id = data['recipe_id']
    db.user_add_like(conn, user_id, recipe_id)
    return 'fav recipe'


@app.route('/get-user', methods=['GET'])
def getUser():
    data = request.get_json()
    user_name = data['user_name']
    user_pw = data['user_pw']
    user_id = db.get_user_id(conn, user_name, user_pw)
    return json.dumps({'user_id': user_id})


@app.route('/set-user', methods=['POST'])
def set_user():
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

