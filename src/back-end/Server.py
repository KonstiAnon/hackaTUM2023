from flask import Flask, render_template, request, jsonify
import DBAccess as dba
import DBAdapter as db
import json
import numpy as np
from collections import defaultdict
from Prediction import predict

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend/static')
conn = dba.connect_to_db()


def generate_prediction(user_likes, user_dislikes, user_id):
    recipes = db.get_recipes(conn)
    r_count = len(recipes)

    likes = db.get_likes(conn)
    grouped_data = defaultdict(list)
    for user_id, recipe_id in likes:
        grouped_data[user_id].append(recipe_id)
    likes_per_user = list(grouped_data.values())
    del grouped_data
    dislikes = db.get_dislikes(conn)
    grouped_data = defaultdict(list)
    for user_id, recipe_id in dislikes:
        grouped_data[user_id].append(recipe_id)
    dislikes_per_user = list(grouped_data.values())

    def join_encoding(list1, list2, total_size):
        result = []
        for l1, l2 in zip(list1, list2):
            encoding = [0] * total_size
            for idx in l1:
                encoding[idx] = 1
            for idx in l2:
                encoding[idx] = -1
            result.append(encoding)
        return np.array(result)
    mat = join_encoding(likes_per_user, dislikes_per_user, r_count)
    user_vec = [0] * r_count
    for l in user_likes:
        user_vec[l] = 1
    for l in user_dislikes:
        user_vec[l] = -1
    user_vec = np.array(user_vec)

    user_recipes = db.get_recipes_for_user(conn, user_id)
    mask = [False] * r_count
    for rec in user_recipes:
        mask[rec['id']] = True

    return predict(mat, user_vec, mask, 8, 4)


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
