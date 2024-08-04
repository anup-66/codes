import os

from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///password_keeper.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:anup%406536@localhost/restaurant"
# can be set to true if logs ae needed . However, makes overhead.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.environ.get("SECRET_KEY")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username =db.Column(db.String(150),unique = True,nullable = False)
    password =db.Column(db.String(150),nullable = False)
    passwords = db.relationship("Password",backref = "user",lazy = True)

class Password(db.Model):
    id  = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(150),nullable = False)
    username = db.Column(db.String(150),nullable = False)
    password= db.Column(db.String(150),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable = False)

with app.app_context():
    db.create_all()

@app.route("/users",methods = ["POST"])
def create_user():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    new_user = User(username = data['username'],password = hashed_password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":"User added successfuly"}),201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message":"User already exists"}),400


@app.route('/average_password_length', methods=['GET'])
@jwt_required()
def average_password_length():
    # Get the current user from JWT
    current_user = get_jwt_identity()

    # Find the user instance
    user = User.query.filter_by(username=current_user).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    # Query to calculate average password length
    avg_stmt = (
        db.session.query(func.avg(func.length(Password.password)))
        .filter(Password.user_id == user.id)
    )

    average_length = avg_stmt.scalar()  # Get the average value

    return jsonify({"average_password_length": average_length}), 200


@app.route("/login",methods = ["POST"])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(username = data["username"]).first()
    if user and bcrypt.check_password_hash(user.password,data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token = access_token)
    return jsonify({"messgae":"Invalid Credentials"})

@app.route("/passwords",methods = ["POST"])
@jwt_required()
def store_password():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and bcrypt.check_password_hash(user.password,data["password"]):
        new_password = Password(
            title = data["title"],
            username = data["stored_username"],
            password  = bcrypt.generate_password_hash(data["stored_password"]).decode("utf-8"),
            user_id = user.id
        )
        try:
            db.session.add(new_password)
            db.session.commit()
            return jsonify({"message":"Password stored sucessfully"}),201
        except:
            return jsonify({"message":"something went wrong"}),401
    else:
        return jsonify({"message":"Invalid credentials"}),401

@app.route("/GetPassword",methods = ["GET"])
@jwt_required()
def get_password():
    data = request.get_json()
    user = User.query.filter_by(username = data["username"]).first()
    if user and bcrypt.check_password_hash(user.password,data['password']):
        passwords = Password.query.filter_by(user_id = user.id).all()
        password_list = [
            {"title": p.title,
             "username": p.username,
             "password": p.password}
            for p in passwords
        ]
        return jsonify(password_list),200
    else:
        return jsonify({"message":"Invalid credentials"}),401

@app.route('/passwords/<int:id>',methods = ['PUT'])
@jwt_required()
def update_password(id):
    data = request.get_json()
    user = User.query.filter_by(username = data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        password_entry = Password.query.get_or_404(id)
        if password_entry.user_id != user.id:
            return jsonify({"message": "Unauthorized access"}), 403

        password_entry.title = data['title']
        password_entry.username = data['stored_username']
        password_entry.password = bcrypt.generate_password_hash(data['stored_password']).decode('utf-8')

        db.session.commit()
        return jsonify({"message": "Password updated successfully"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
if __name__ =="__main__":
    app.run(debug=True)