from flask import Blueprint, request, jsonify, render_template
from models import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        if User.query.filter_by(name=name).first():
            return jsonify({"msg" : "User name is already used."}), 400
        elif len(name) < 2:
            return jsonify({"msg": "User name is too short."}), 400
        elif len(password) < 6:
            return jsonify({"msg": "Password name is too short, must be at least 6 characters."}), 400
        else:
            new_user = User(name=name, password=generate_password_hash(password, method="scrypt"))
            db.session.add(new_user)
            db.session.commit()
            access_token = create_access_token(identity=name)
            return 
    else:
        return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")
        password = data.get("password")
        
        if len(name) < 2:
            return jsonify({"msg": "The name is too short."}), 400
        elif len(password) < 6:
            return jsonify({"msg": "The password is too short."}), 400
        else:
            user = User.query.filter_by(name=name).first()
            if user and check_password_hash(user.password, password):
                access_token = create_access_token(identity=name)
                return jsonify(access_token=access_token), 200
            else:
                return jsonify({"msg": "user does't exist"}), 401
    else:
        return render_template("register.html")