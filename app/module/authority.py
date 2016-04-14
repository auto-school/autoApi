from conn import Connection


def valid_login(username, password):
    conn = Connection()
    users = conn.find_user_by_username(username)
    if user_not_exist(users):
        return False
    if equal_password(users[0], password):
        return True
    return False


def signup(username, password):

    conn = Connection()

    user = conn.find_user_by_username(username)
    if not user_not_exist(user):
        return False
    result = conn.insert_user(dict(username=username, password=password))
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

