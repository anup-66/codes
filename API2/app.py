from flask import Flask , request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError,OperationalError
from sqlalchemy import create_engine,text

# Setting the app instance to flask
app = Flask(__name__)
try:
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:anup%406536@localhost/notes"
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    engine.connect()
except OperationalError:
    create_engine("mysql://root:anup%406536@localhost").connect().execute(text("CREATE DATABASE notes;"))

# can be set to true if logs ae needed . however, makes overhead.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.environ.get("SECRET_KEY")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
print()
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(150),nullable = False)
    password = db.Column(db.String(150),nullable = False)
    relation = db.relationship("Notes",backref = "user",lazy = True)

class Notes(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(150),nullable = True)
    note = db.Column(db.Text,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable = False)

with app.app_context():
    db.create_all()
@app.route("/login",methods = ["POST"])
# @jwt_required()
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    user = User.query.filter_by(username = username).first()
    if user and bcrypt.check_password_hash(user.password,password):
        token = create_access_token(identity = user.username)
        return jsonify({"token":token}),200
    else:
        return jsonify({"message":"Invalid credentials"}) ,401

@app.route("/register",methods = ["POST"])
@jwt_required()
def register():
    data = request.get_json()
    username = data["username"]
    password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    try:
        new_user = User(username = username,password = password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":"User registered successfully"}),200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message":"Invalid username choose new username."}),401

@app.route("/add",methods = ["POST"])
@jwt_required()
def add():
    try:
        data = request.get_json()
        username = data['username']
        password = data["password"]
        title = data["title"]
        notes = data["notes"]
        user = User.query.filter_by(username = username).first()
        if user and bcrypt.check_password_hash(user.password,password):
            new_notes = Notes(
                # username = username,
                # password = bcrypt.generate_password_hash(password),
                title = title,
                note = notes,
                user_id = user.id
            )
            try:
                db.session.add(new_notes)
                db.session.commit()
                return jsonify({"message":"notes added successfully."})
            except IntegrityError:
                return jsonify({"message":"Some error ocured"})
        else:
            return jsonify({"message":"please provide correct username and password"})
    except KeyError:
        return jsonify({"message":"please check all the fields."})
@app.route("/modifyNote/<int:d>",methods = ["PUT"])
@jwt_required()
def modify(d):
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(username)
    user = User.query.filter_by(username = username).first()
    if user and bcrypt.check_password_hash(user.password,password):
        print(d)
        Note = Notes.query.filter_by(user_id = d).all()
        print(Note)
        for i in Note:
            print(i.title)
            if i.title==data['title']:
                i.note = data['notes']
                i.title = data['title']
                db.session.commit()
                return jsonify({"message":"successfully updated"})
        else:
            return jsonify({"message":"invalid title"})
    else:
        return jsonify({"message":"incorrect username or password"})

if __name__ == "__main__":
    app.run(debug = True)