import flask
import controller.utilisateur_controller as user_controller


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods='GET')
def home():
    return "It's home page"


@app.route('/user/get_all', methods='GET')
def get_all_users():
    return user_controller.get_all_users()


app.run()
