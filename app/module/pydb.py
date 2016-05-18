from flask import g
from pymongo import MongoClient
from conn import Connection


def connect_db():
    db = Connection()
    return db


def get_db():
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db



