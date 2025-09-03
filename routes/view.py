from flask import Blueprint, request, jsonify, render_template
from models import Tasks
from extensions import db
from flask_jwt_extended import jwt_required

view = Blueprint("view", __name__)


@view.route("/")
def home():
    return render_template("index.html")


# POST
@view.route("/add_task", methods=["POST"])
@jwt_required()
def add_task():
    data = request.get_json()
    new_task = Tasks(title=data["title"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"msg": "task added successfuly"}), 201

# UPDATE
@view.route("/update_task/<int:task_id>", methods=["PUT"])
def update(task_id):
    data = request.get_json()
    task = Tasks.query.get(task_id)
    if task:
        task.title = data.get("title", task.title)
        task.done = data.get("done", task.done)
        db.session.commit()
        return jsonify({"msg": "task updated successfuly"}), 201
    else:
        return jsonify({"msg": "task not found"}), 404

# DELETE
@view.route("/delete_task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    data = Tasks.query.get(task_id)
    if data:
        db.session.delete(data)
        db.session.commit()
        return jsonify({"msg": "task deleted successfuly"}), 201
    else:
        return jsonify({"msg": "task not found"}), 404
