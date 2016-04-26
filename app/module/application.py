from conn import Connection
from datetime import datetime
import message_mgr
import time


class ApplicationManager:
    conn = Connection()

    def __init__(self):
        pass

    @classmethod
    def insert_application(cls, application):
        application['created_time'] = datetime.now()
        result = cls.conn.insert_application(application)
        message = dict()
        message['created_time'] = datetime.now()
        message['receiver'] = application['project']['creator']
        message['sender'] = application['applier']
        message['type'] = 0
        project = dict(id=str(result.inserted_id))
        message['attachment'] = dict(project=project)
        message_mgr.add_message(message)
        return True

    @classmethod
    def find_application_by_id(self, application_id):
        application = self.conn.find_application_by_id(application_id)
        return convert_application_bson_type(application)

    @classmethod
    def approve_application(self, application_id):
        self.conn.update_application_status(application_id, status=1)
        return True


def convert_application_bson_type(application):
    application['created_time'] = time.mktime(application['created_time'].timetuple())
    application['_id'] = str(application['_id'])
    return application
