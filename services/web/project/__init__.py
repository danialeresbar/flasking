from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('project.config.Config')
database = SQLAlchemy(app)


class User(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(128), unique=True, nullable=False)
    active = database.Column(database.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/")
def hello_world():
    return jsonify(hello="world")

@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)
