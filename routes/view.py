from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import Tasks
from extensions import db
from flask_jwt_extended import jwt_required

view = Blueprint("view", __name__)


@view.route("/")
def home():
    # Fetch all tasks from the database to display them
    tasks = Tasks.query.order_by(Tasks.id).all()
    return render_template("index.html", tasks=tasks)


# POST
@view.route("/add_task", methods=["POST"])
@jwt_required()
def add_task():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"msg": "title is required"}), 400
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
        return redirect(url_for("view.home"))
    else:
        return render_template("edit_task.html", task=task)

# DELETE
@view.route("/delete_task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    data = Tasks.query.get(task_id)
    if data:
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for("view.home"))
    else:
        return jsonify({"msg": "task not found"}), 404
