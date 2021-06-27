from flask import Flask, render_template, send_from_directory, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import db
import jwt
import os

# Flask uses load dotenv by default
app = Flask(__name__)

app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.sqlite")
db.init_app(app)

# directories
@app.route("/sign-in", methods=["GET","POST"])
def sign_in():
    """
    !CHECKED!
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
        dab = db.get_db()
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
            dab.execute(
                "INSERT INTO user (Username,Password) VALUES (?,?)",
                (username, generate_password_hash(password),))
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
    !CHECKED!
    Function that checks for existence of the username and validates the 
    password for loging in the web app.
    """
    if request.method == "POST":

        # gets the username and password posted
        dab = db.get_db()
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
        user_ = dab.execute(
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
            token = jwt.encode({"username" : username}, "error--", algorithm="HS256")
            return jsonify({"status" : "ok", "message" : "correct username", "token" : token}),200
        # return the error
        else:
            return error, 418
    
    else:
        return ""

@app.route("/get-language", methods=["GET", "POST"])
def get_lang():
    """
    !CHECKED!
    Function that takes all of the languages and returns if existing
    """
    try:
        body = request.get_json()
    except:
        return jsonify({"status": "bad", "message": "no information provided"}), 401

    try:
        this_id = int(body["IdLanguages"])
        status = 1
    except:
        return jsonify({"status": "bad", "message": "missing data"}), 400

    dab = db.get_db()
    info = dab.execute(
        # ? NAME, PIC_URL, DESC, EXAMPLE
        "SELECT * FROM languages WHERE IdLanguages = ?", (this_id,)
    ).fetchone()

    if info != None:
        name = info["Name"]
        pic_url = info["Pic_Url"]
        desc = info["Desc"]
        example = info["Example"]

        return jsonify({
            "status": "ok", "name": name, "pic_url" : pic_url, "desc" : desc,
            "example" : example, "id" : this_id
        }), 200
    
    else:
        return jsonify({"status": "bad", "message": "not implemented"}), 400

@app.route("/get-topic", methods=["GET", "POST"])
def get_topic():
    """
    !CHECKED!
    Gets and returns the topic via the language input
    """
    try:
        body = request.get_json()
    except:
        return jsonify({"status": "bad", "message": "no information provided"}), 401

    try:
        this_id = int(body["idTopic"])
        status = 1
    except:
        return jsonify({"status": "bad", "message": "missing data"}), 400

    dab = db.get_db()
    info = dab.execute(
        # ? NAME, PIC_URL, DESC, EXAMPLE
        "SELECT * FROM languages WHERE IdLanguages = ?", (this_id,)
    ).fetchone()

    if info != None:
        name = info["Name"]
        pic_url = info["Pic_Url"]
        id_lang = info["Id_Languages"]

        return jsonify({
            "status": "ok", "name": name, "pic_url" : pic_url, "id_language" : id_lang,
            "id" : this_id
        }), 200
    
    else:
        return jsonify({"status": "bad", "message": "not implemented"}), 400

@app.route("/get-resources", methods=["GET","POST"])
def get_resource():
    """
    !CHECKED!
    Function that gets all of the resources available for the topic of the language.
    """
    try:
        body = request.get_json()
    except:
        return jsonify({"status": "bad", "message": "no information provided"}), 401

    try:
        this_id = int(body["IdRec"])
        status = 1
    except:
        return jsonify({"status": "bad", "message": "missing data"}), 400

    dab = db.get_db()
    info = dab.execute(
        # ? NAME, PIC_URL, DESC, EXAMPLE
        "SELECT * FROM languages WHERE IdLanguages = ?", (this_id,)
    ).fetchone()

    if info != None:
        if info["IdVideos"]:
            idt = info["IdVideos"]
        else:
            idt = info["IdUrl"]
        name = info["Name"]
        url = info["Url"]
        

        return jsonify({
            "status": "ok", "name": name, "url" : url, "Id_Source" : idt,
            "id" : this_id
        }), 200
    
    else:
        return jsonify({"status": "bad", "message": "not implemented"}), 400


# ! health directory !
@app.route("/health")
def health():
    return ""

if __name__ == "__main__":
    app.run()