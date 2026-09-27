from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
tasks = [
    {"id": 1, "title": "Learn networking basics", "done": False},
    {"id": 2, "title": "Build a REST API", "done": False},
]
next_id = 3

# GET all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

# GET one task
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

# POST - create a task
@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_task = {"id": next_id, "title": data["title"], "done": False}
    tasks.append(new_task)
    next_id += 1
    return jsonify(new_task), 201

# PUT - update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task), 200

# DELETE - remove a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
        app.run(debug=True, ssl_context="adhoc")