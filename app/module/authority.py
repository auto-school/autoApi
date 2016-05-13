from conn import Connection
from flask import g


def valid_login(username, password):
    conn = Connection()
    users = conn.find_user_by_username(username)
    if user_not_exist(users):
        return False
    if equal_password(users[0], password):
        g.user = convert_user_bson_type(users[0])
        g.user.pop('password')
        return users[0]
    return False


def signup(username, password, name):

    conn = Connection()

    user = conn.find_user_by_username(username)
    if not user_not_exist(user):
        return False
    result = conn.insert_user(dict(username=username,
                                   password=password,
                                   professional_skill='',
                                   contact='',
                                   practice_experience='',
                                   edu_experience='',
                                   name=name,
                                   role=0))
    if result:
        return True
    else:
        return False


def user_not_exist(user):
    if len(user) == 0:
        return True
    else:
        return False


def equal_password(user, password):
    return user['password'] == password

def convert_user_bson_type(user):
    user['_id'] = str(user['_id'])
    return user
