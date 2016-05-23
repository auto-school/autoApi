from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo


class Connection:

    def __init__(self):
        client = MongoClient("localhost:27017")
        conn = client.auto
        self.conn = conn

    def insert_user(self, user):
        self.conn.users.insert_one(user)
        return True





