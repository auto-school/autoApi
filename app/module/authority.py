from flask import g

from db.conn import Connection
from db.pydb import get_db


def valid_login(username, password):
    conn = get_db()
    user = conn.users.find_one({'username': username})
    if user is None:
        return False
    if user['password'] == password:
        g.user = convert_user_bson_type(user)
        g.user.pop('password')
        return user
    return False


def signup(username, password, name):
    conn = get_db()
    user = conn.users.find_one({'username': username})
    if user:
        return False
    conn.users.insert_one(dict(username=username,
                                   password=password,
                                   professional_skill='',
                                   contact='',
                                   practice_experience='',
                                   edu_experience='',
                                   name=name,
                                   role=0))
    return True


def convert_user_bson_type(user):
    user['_id'] = str(user['_id'])
    return user
