from bson.json_util import dumps as json_dumps
from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
# to properly configure the db, we need :
# 1. starts with the engine, here : "mongodb://"
# 2. <user>:<password> the ones the container 'api'
# 3. @<db-container-name> else -> unreachable!
# 4. :<port>/<db-name>
app.config["MONGO_URI"] = "mongodb://" + \
                          os.environ["MONGODB_USERNAME"] + ":" + os.environ["MONGODB_PASSWORD"] + \
                          "@" + os.environ["MONGODB_HOST"] + ":27017/webapp"

mongo = PyMongo(app)
db = mongo.db


@app.route("/hi")
def index():
    if not db.todos.find_one():
        todos = db.todos
        todos.insert_one({"name": "say hi!"})
    todos = db.todos.find_one()
    return json_dumps(todos)


if __name__ == "__main__":
    app.run(debug=True, port=5000)