from flask import Flask, render_template, request
import DBAccess as dba
import DBAdapter as db
import json

app = Flask(__name__, template_folder='../frontend', static_folder='../frontend/static')
conn = dba.connect_to_db()


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
    data = request.get_json()
    user_name = data['user_name']
    user_pw = data['user_pw']
    db.insert_user(conn, user_name, user_pw)
    return 'set user'


if __name__ == '__main__':
    app.run(debug=True)
