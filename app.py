import json
from flask import Flask, request, jsonify
from models.specialite import Specialite
from controllers.specialite_controller import get_all_specialites, get_specialite
from controllers.utilisateur_controller import get_all_users, get_user
from controllers.medecin_controller import get_all_medecins, get_medecin
from controllers.med_et_controller import get_medecin_in_etablissement

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/specialites", methods=['GET'])
def specialites():
    return jsonify(get_all_specialites())


@app.route("/specialites/<int:id>", methods=['GET'])
def getSpecialiteById(id):
    return jsonify(get_specialite(id))


@app.route("/users", methods=['GET'])
def users():
    return jsonify(get_all_users())


@app.route("/users/<int:id>", methods=['GET'])
def getUserById(id):
    return jsonify(get_user(id))


@app.route("/medecins", methods=['GET'])
def medecins():
    return jsonify(get_all_medecins())


@app.route("/medecins/<int:id>", methods=['GET'])
def getMedecinById(id):
    return jsonify(get_medecin(id))

@app.route("/et/<int:id>", methods=['GET'])
def get_med_et(id):
    return jsonify(get_medecin_in_etablissement(id))


app.run()
