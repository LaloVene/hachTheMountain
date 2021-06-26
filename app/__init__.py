from flask import Flask, render_template, send_from_directory, request, jsonify
from dotenv import dotenv_values
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db
from . import db
import jwt
import os

# Flask uses load dotenv by default
app = Flask(__name__)
SECRETS = dotenv_values(".env")

app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.sqlite")
db.init_app(app)

# directories
@app.route("/sign-in", methods=["GET","POST"])
def sign_in():
    """
    Function that inserts the new username and password to the sql database.
    Checks for any error.
    """
    if request.method == "POST":

        # storing the posted username and password
        try:
            body = request.get_json()
        except:
            return jsonify({"status": "bad", "message": "no information provided"}), 401

        try:
            print(body["username"])
            password = str(body["password"])
            username = str(body['username'])
        except:
            return jsonify({"status": "bad", "message": "missing data"}), 400
        db = get_db()
        error = None

        # checks for any errors
        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is required"
        elif db.execute(
            "SELECT * FROM user WHERE Username = ?", (username,)
        ).fetchone() != None:
            error = f"user {username} already exists"

        # insert into database
        if error == None:
            db.execute(
                "INSERT INTO user (Username,Password) values (?,?)",
                (username,), generate_password_hash(password,))
            db.commit()
            return f"User {username} created successfully"
        
        # returns the error 
        else:
            return error, 418

    else:
        return ""

@app.route("/log-in", methods=["GET","POST"])
def log_in():
    """
    Function that checks for existence of the username and validates the 
    password for loging in the web app.
    """
    if request.method == "POST":

        # gets the username and password posted
        db = get_db()
        error = None
        try:
            body = request.get_json()
        except:
            return jsonify({"status": "bad", "message": "no information provided"}), 401

        try:
            print(body["username"])
            password = str(body["password"])
            username = str(body['username'])
        except:
            return jsonify({"status": "bad", "message": "missing data"}), 400

        # look for the user in the db
        user_ = db.execute(
            "SELECT * FROM user WHERE Username = ?", (username,)
        ).fetchone()
        
        # no user match
        if not user_:
            error = "Incorrect Username or nonexistent"
        # check password validity
        elif not check_password_hash(user_["Password"], password):
            error = "Incorrect password"

        # return json token with ok status
        if not error:
            token = jwt.encode(username, "error--", algorithm="HS256")
            return jsonify({"status" : "ok", "message" : "correct username", "token" : token}),200
        # return the error
        else:
            return error, 418
    
    else:
        return ""

@app.route("/get-language", methods=["GET", "POST"])
def get_lang():
    """
    Function that takes all of the languages and returns if existing
    """
    try:
        body = request.get_json()
    except:
        return jsonify({"status": "bad", "message": "no information provided"}), 401

    try:
        id_lang = int(body["IdLanguages"])
        name = str(body['Name'])
        pic_url = str(body['Pic_url'])
        desc = str(body['Desc'])
        example = str(body['Example'])
        status = 1
    except:
        return jsonify({"status": "bad", "message": "missing data"}), 400

    return jsonify({
        "status": "ok", "name": name, "pic_url" : pic_url, "desc" : desc,
        "example" : example, "id" : id_lang
    }), 200


@app.route("/get-topic", methods=["GET", "POST"])
def get_topic():
    """
    Gets and returns the topic via the language input
    """
    try:
        body = request.get_json()
    except:
        return jsonify({"status": "bad", "message": "no information provided"}), 401

    try:
        id_topic = int(body["IdTopic"])
        name = str(body['Name'])
        pic_url = str(body['Pic_url'])
        id_lang = str(body['Id_Languages'])
        status = 1
    except:
        return jsonify({"status": "bad", "message": "missing data"}), 400

    return jsonify({
        "status": "ok", "name": name, "pic_url" : pic_url,
         "id" : id_topic, "id_lang" : id_lang
    }), 200


# ! health directory !
@app.route("/health")
def health():
    return ""

if __name__ == "__main__":
    app.run()