from bson.json_util import dumps as json_dumps
from flask import Blueprint, current_app as app


bp = Blueprint("hi", __name__)


@bp.route("/hi")
def index():
    db = app.db
    if not db.todos.find_one():
        todos = db.todos
        todos.insert_one({"message": "hi hi!"})
    todos = db.todos.find_one()
    return json_dumps(todos)
