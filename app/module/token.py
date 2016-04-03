from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


class Token:
    secret_key = ''

    def __init__(self):
        pass


def set_token_key(key):
    Token.secret_key = key


def generate_auth_token(uid, expiration=600):
    s = Serializer(Token.secret_key, expires_in=expiration)
    return s.dumps({'id': uid})


def verify_auth_token(token):
    s = Serializer(Token.secret_key)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None    # valid token, but expired
    except BadSignature:
        return None    # invalid token
    return data['id']