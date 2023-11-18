from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/fetchRecipies')
def fetchRecipies():
    return 'fetch recipies'


@app.route('/setPreferences')
def setPreferences():
    return 'set prefs'


@app.route('/favorRecipe')
def favorRecipe():
    return 'fav recipe'


@app.route('/getUser')
def getUser():
    return "get user"


@app.route('/setUser')
def set_user():
    return "set user"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
