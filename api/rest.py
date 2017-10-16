from flask import Flask, jsonify, request
import core
app = Flask(__name__)

@app.route("/", methods=["POST"])
@app.route("/login", methods=["POST"])
def login():
    return jsonify(core.User(request.form["username"], request.form["password"]))

core._api_mains.append(app.run)
