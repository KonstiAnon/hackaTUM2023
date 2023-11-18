from flask import Flask, render_template, request
import DBAdapter as dba

app = Flask(__name__, template_folder='../front-end', static_folder='../front-end/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetch-recipies')
def fetchRecipies():
    return 'fetch recipies'


@app.route('/setPreferences')
def setPreferences():
    data = request.get_json()
    user_id = data['user_id']
    allergies = data['allergies']
    dba.set_allergies_for_user(user_id, allergies)
    return 'set prefs'


@app.route('/favorRecipe')
def favorRecipe():
    return 'fav recipe'


@app.route('/get-user')
def getUser():
    return "get user"


@app.route('/set-user')
def set_user():
    return "set user"


if __name__ == '__main__':
    app.run(debug=True)
