from flask import Flask
from flask_pymongo import PyMongo
import os

from .init_db import init_db
from .example_blueprint import bp

app = Flask(__name__)
init_db()
# to properly configure the db, we need :
# 1. starts with the engine, here : "mongodb://"
# 2. <user>:<password> the ones the container 'api'
# 3. @<db-container-name> else -> unreachable!
# 4. :<port>/<db-name>
app.config["MONGO_URI"] = "mongodb://" + \
                          os.environ["MONGODB_USERNAME"] + ":" + os.environ["MONGODB_PASSWORD"] + \
                          "@" + os.environ["MONGODB_HOST"] + ":27017/webapp"

app.db = PyMongo(app).db

app.register_blueprint(bp)


if __name__ == "__main__":
    app.run(debug=True, port=5000)