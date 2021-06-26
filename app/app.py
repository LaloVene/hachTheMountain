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

@app.route("/languages")
def languages():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        pic_url = request.form.get('pic_url')
        desc = request.form.get('desc')
        example = request.form.get('example')
        db = get_db()
        error = None

        if not id:
            error = 'Id is required.'
        elif not name:
            error = 'Name is required.'
        elif not pic_url:
            error = 'Picture url is required.'
        elif not desc:
            error = 'Description id is required'
        elif not example:
            error = 'Example id is required'
        elif db.execute(
            'SELECT IdLanguages FROM topic WHERE IdLanguages = ?', (id,)
        ).fetchone() is not None:
            error = f"The Language {id} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO languages (IdLanguages, Name, Pic_url, Desc, Example) VALUES (?, ?, ?, ?, ?)',
                (id,name,pic_url,desc,example)
            )
            db.commit()
            return f"The Language {id} created successfully"
        else:
            return error, 418

    return "Login Page not yet implemented", 501

@app.route("/topics")
def topics():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        pic_url = request.form.get('pic_url')
        id_lang = request.form.get('id_lang')
        db = get_db()
        error = None

        if not id:
            error = 'Id is required.'
        elif not name:
            error = 'Name is required.'
        elif not pic_url:
            error = 'Picture url is required.'
        elif not id_lang:
            error = 'Language id is required'
        elif db.execute(
            'SELECT idTopic FROM topic WHERE idTopic = ?', (id,)
        ).fetchone() is not None:
            error = f"The topic {id} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO topic (idTopic, Name, Pic_url, Id_Languages) VALUES (?, ?, ? ,?)',
                (id,name,pic_url,id_lang)
            )
            db.commit()
            return f"The topic {id} created successfully"
        else:
            return error, 418

    return "Login Page not yet implemented", 501

@app.route("/resources")
def resources():
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    #SELECT * FROM (TABLA) WHERE id = id
    # ? html, title?
    return ""

@app.route("/url")
def url():
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    #SELECT * FROM (TABLA) WHERE id = id
    # ? html, title?
    return ""

@app.route("/videos")
def videos():
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    #SELECT * FROM (TABLA) WHERE id = id
    # ? html, title?
    return ""

@app.route("/visited")
def visited():
    # TODO return render_template('index.html', title="main page", url=os.getenv("URL"))
    #SELECT * FROM (TABLA) WHERE id = id
    # ? html, title?
    return ""


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
    return jsonify({"status": "ok", "name": name}), 200

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
    return ""

# ! health directory !
@app.route("/health")
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
