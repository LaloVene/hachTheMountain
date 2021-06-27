import os
import db
from flask import Flask, render_template, send_from_directory, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db
import jwt


# Flask uses load dotenv by default
app = Flask(__name__)

app.config["DATABASE"] = os.path.join(os.getcwd(), "flask.sqlite")

db.init_app(app)

# directories

@app.route("/")
def main():
    return "Okay",200
    #return render_template('index.html', title="learn2code", url=os.getenv("URL"))

@app.route("/languages",methods=["POST"])
def languages():
    if request.method == 'POST':
        try:
            body = request.get_json()
        except:
            return jsonify({"status": "bad", "message": "no information provided"}), 401

        try:
            name = str(body['name'])
            pic_url = str(body['pic_url'])
            desc = str(body['desc'])
            example = str(body['example'])
            db = get_db()
            error = None
        except:
            return jsonify({"status": "bad", "message": "missing data"}), 400

        if not name:
            error = 'Name is required.'
        elif not pic_url:
            error = 'Picture url is required.'
        elif not desc:
            error = 'Description id is required'
        elif not example:
            error = 'Example id is required'

        if error is None:
            db.execute(
                'INSERT INTO languages (Name, Pic_url, Desc, Example) VALUES (?, ?, ?, ?)',
                (name,pic_url,desc,example)
            )
            db.commit()
            return f"The Language {name} created successfully"
        else:
            return error, 418

    return "Login Page not yet implemented", 501

@app.route("/topics",methods=["POST"])
def topics():
    if request.method == 'POST':
        try:
            body = request.get_json()
        except:
            return jsonify({"status": "bad", "message": "no information provided"}), 401

        try:
            name = str(body['name'])
            pic_url = str(body['pic_url'])
            id_lang = str(body['id_lang'])
            db = get_db()
            error = None
        except:
            return jsonify({"status": "bad", "message": "missing data"}), 400

        if not name:
            error = 'Name is required.'
        elif not pic_url:
            error = 'Picture url is required.'
        elif not id_lang:
            error = 'Language id is required'
        """elif db.execute(
            'SELECT idTopic FROM topic WHERE idTopic = ?', (id,)
        ).fetchone() is not None:
            error = f"The topic {id} is already registered."""

        if error is None:
            db.execute(
                'INSERT INTO topic (Name, Pic_url, Id_Languages) VALUES (?, ?, ?)',
                (name,pic_url,id_lang)
            )
            db.commit()
            return f"The topic {name} created successfully"
        else:
            return error, 418

    return "Login Page not yet implemented", 501

@app.route("/resources",methods=["POST"])
def resources():
    if request.method == 'POST':
        try:
            body = request.get_json()
        except:
            return jsonify({"status": "bad", "message": "no information provided"}), 401

        try:
            difficulty = str(body['difficulty'])
            title = str(body['title'])
            idTopic = str(body['idTopic'])
            db = get_db()
            error = None
        except:
            return jsonify({"status": "bad", "message": "missing data"}), 400

        #if not id:
        #    error = 'Id is required.'
        if not difficulty:
            error = 'Difficulty is required.'
        elif not title:
            error = 'Title is required.'
        elif not idTopic:
            error = 'idTopic id is required'

        if error is None:
            db.execute(
                'INSERT INTO rec (Difficulty, Title, Id_Topic) VALUES (?, ?, ?)',
                (difficulty,title,idTopic)
            )
            db.commit()
            return f"The resource {title} created successfully"
        else:
            return error, 418

    return "Login Page not yet implemented", 501

@app.route("/url",methods=["POST"])
def url():
    if request.method == 'POST':
        try:
            body = request.get_json()
        except:
            return jsonify({"status": "bad", "message": "no information provided"}), 401

        try:
            name = str(body['name'])
            url = str(body['url'])
            idRec = str(body['idRec'])
            db = get_db()
            error = None
        except:
            return jsonify({"status": "bad", "message": "missing data"}), 400

        #if not id:
        #    error = 'Id is required.'
        if not name:
            error = 'Name is required.'
        elif not url:
            error = 'Url is required.'
        elif not idRec:
            error = 'Resource id is required'

        if error is None:
            db.execute(
                'INSERT INTO url (Name, Url, Id_Rec) VALUES (?, ?, ?)',
                (name,url,idRec)
            )
            db.commit()
            return f"The url {name} created successfully"
        else:
            return error, 418

    return "Login Page not yet implemented", 501


@app.route("/videos",methods=["POST"])
def videos():
    if request.method == 'POST':
        try:
            body = request.get_json()
        except:
            return jsonify({"status": "bad", "message": "no information provided"}), 401

        try:
            name = str(body['name'])
            url = str(body['url'])
            idRec = str(body['idRec'])
            db = get_db()
            error = None
        except:
            return jsonify({"status": "bad", "message": "missing data"}), 400

        if not name:
            error = 'Name is required.'
        elif not url:
            error = 'Url is required.'
        elif not idRec:
            error = 'Resource is required'

        if error is None:
            db.execute(
                'INSERT INTO videos (Name, Url, Id_Rec) VALUES (?, ?, ?)',
                (name,url,idRec)
            )
            db.commit()
            return f"The video {name} created successfully"
        else:
            return error, 418

    return "Login Page not yet implemented", 501

@app.route("/visited",methods=["POST"])
def visited():
    if request.method == 'POST':
        try:
            body = request.get_json()
        except:
            return jsonify({"status": "bad", "message": "no information provided"}), 401

        try:
            idRec = str(body['idRec'])
            idTopic = str(body['idTopic'])
            username = str(body['username'])
            db = get_db()
            error = None
        except:
            return jsonify({"status": "bad", "message": "missing data"}), 400
        

        if not idRec:
            error = 'Resource id is required.'
        elif not idTopic:
            error = 'Topic id is required.'
        elif not username:
            error = 'Username is required'

        if error is None:
            db.execute(
                'INSERT INTO visited (IdRec, Id_Topic, User_Username) VALUES (?, ?, ?)',
                (idRec,idTopic,username)
            )
            db.commit()
            return f"The visited register from the user {username} created successfully"
        else:
            return error, 418

    return "Login Page not yet implemented", 501


@app.route("/set_language", methods=["POST"])
def set_language():
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    # ? html, title?
    try:
        body = request.get_json()
    except:
        return jsonify({"status": "bad", "message": "no information provided"}), 401

    try:
        name = str(body['name'])
        icon = str(body['icon'])
        status = 1
    except:
        return jsonify({"status": "bad", "message": "missing data"}), 400
    return jsonify({"status": "ok", "message":"", "name": name}), 200

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
        db = db.get_db()
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
        db = db.get_db()
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
    !CHECKED!
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
        name = str(body['Name'])
        url = str(body['Url'])
        id_topic = int(body["Id_Rec"])
        status = 1
    except:
        return jsonify({"status": "bad", "message": "missing data"}), 400

    if body["IdUrl"]:
        id_resource = int(body["IdUrl"])
    else:
        id_resource = int(body["IdVideos"])
    return jsonify({
        "status": "ok", "name": name, "Url" : url,
         "id_topic_resource" : id_topic, "id_resource" : id_resource
    }), 200

# ! health directory !
@app.route("/health")
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
