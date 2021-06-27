import os
import db
from flask import Flask, render_template, send_from_directory, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db

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

@app.route("/sign-in", methods=["POST"])
def sign_in():
    if request.method == "POST":
        username = request.form.get("Username")
        password = request.form.get("Password")
        db = get_db()
        error = None

        if not username:
            error = "Username is required"
        elif not password:
            error = "Password is required"
        elif db.execute(
            "SELECT * FROM user WHERE Username = ?", (username)
        ).fetchone() != None:
            error = f"user {username} already exists"

        if error == None:
            db.execute(
                "INSERT INTO user (Username,Password) values (?,?)",
                username, generate_password_hash(password))
            db.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    # ? html, title?
    return ""

@app.route("/log-in", methods=["POST"])
def log_in():
    if request.method == "POST":
        username = request.form.get("Username")
        password = request.form.get("Password")
        db = get_db()
        error = None

        user = db.execute(
            "SELECT * from user WHERE Username = ?", (username)
        ).fetchone()
        
        if not user:
            error = "Incorrect Username or nonexistent"
        elif not check_password_hash(user["Password"],password):
            error = "Incorrect password"

        if not error:
            return "Successful login", 200
        else:
            return error, 418
            
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    # ? html, title?
    return "Ok",200

# ! health directory !
@app.route("/health")
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
