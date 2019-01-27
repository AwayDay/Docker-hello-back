from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/group")
def message():
    return jsonify(group="Aqours")


@app.route("/members")
def member_list():
    return jsonify(members=["takami", "watanabe", "sakurauchi", "kurosawa(R)", "kunikita", "tsushima", "kurosawa(D)", "matsuura", "ohara"])