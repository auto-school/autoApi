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

    def find_user_by_username(self, username):
        results = list(self.conn.users.find({'username': username}))
        return results




