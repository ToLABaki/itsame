from flask import Flask, jsonify, request
import core

app = Flask(__name__)

@app.route("/", methods=["POST"])
@app.route("/login", methods=["POST"])
def login():
    try:
        u = core.authenticate(request.form["username"], request.form["password"])
        return jsonify({"login": "success"})
    except core.FailedToAuthenticate:
        return jsonify({"login": "fail"})

@app.route("/register", methods=["POST"])
def register():
    try:
        u = core.register(request.form["username"], request.form["password"])
        return jsonify({"register": "success"})
    except core.FailedToAuthenticate:
        return jsonify({"register": "fail"})

core._api_mains.append(app.run)
