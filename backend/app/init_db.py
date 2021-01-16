from pymongo import MongoClient
import os


def init_db():
    client = MongoClient(host=os.environ["MONGODB_HOST"], port=27017)
    admin, admin_pw = os.environ["MONGO_INITDB_ROOT_USERNAME"], os.environ["MONGO_INITDB_ROOT_PASSWORD"]
    client.admin.authenticate(admin, admin_pw)
    if "webapp" not in client.list_database_names():
        print("---- Initializing mongodb ----")
        client["webapp"].add_user(os.environ["MONGODB_USERNAME"], os.environ["MONGODB_PASSWORD"],
                                  roles=[{"role": "readWrite", "db": "webapp"}])

        # initialize your db with some data...
