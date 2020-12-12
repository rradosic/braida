from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
from lighting.lighting import Lighting

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/braida"

CORS(app,  resources={r"/*": {"origins": "*"}})
mongo = PyMongo(app)

@app.route('/', methods=["GET"])
def status():
    status = {"status":"Still Alive!"}
    return jsonify(status)

@app.route('/lighting', methods=["GET"])
def get_lighting():
    lighting = mongo.db.lighting.find_one_or_404({"_id":1})
    return jsonify(lighting)

@app.route('/lighting', methods=["POST"])
def set_lighting():
    lightingData = request.get_json()
    mongo.db.lighting.update_one({"_id":1}, {"$set": lightingData})
    update_lighting(lightingData)
    return jsonify({"success": "true"})

@app.route('/music', methods=["GET"])
def get_music():
    music = mongo.db.music.find_one_or_404({"_id":1})
    return jsonify(music)

@app.route('/music', methods=["POST"])
def set_music():
    musicData = request.get_json()
    mongo.db.music.update_one({"_id":1}, {"$set": musicData})
    return jsonify({"success": "true"})

@app.route('/settings', methods=["GET"])
def get_settings():
    settings = mongo.db.settings.find_one_or_404({"_id":1})
    return jsonify(settings)

@app.route('/settings', methods=["POST"])
def set_settings():
    settingsData = request.get_json()
    mongo.db.settings.update_one({"_id":1}, {"$set": settingsData})
    return jsonify({"success": "true"})

def update_lighting(options):
    print(options)
    lighting = Lighting()
    lighting.update(options)
    return True