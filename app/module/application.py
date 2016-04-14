from conn import Connection
from datetime import datetime


class ApplicationManager:
    conn = Connection()

    def __init__(self):
        pass

    @classmethod
    def insert_application(cls, application):
        application['created_time'] = datetime.now()
        result = cls.conn.insert_application(application)
        return True
