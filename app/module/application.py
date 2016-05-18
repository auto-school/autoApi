from datetime import datetime
import time
from pydb import get_db
from project import ProjectManager
from flask import g


class ApplicationManager:

    def __init__(self):
        self._mongo_conn = get_db()

    def insert_application(self, application):
        application['created_time'] = datetime.now()
        applier = dict(username=g.user['username'], name=g.user['name'])
        application['applier'] = applier
        application['status'] = 0
        apply_project = ProjectManager().find_project_by_id(application['project']['id'])
        application['project']['name'] = apply_project['name']
        result = self._mongo_conn.insert_application(application)
        message = dict()
        message['created_time'] = datetime.now()
        message['receiver'] = apply_project['creator']['id']
        message['sender'] = dict(username=application['applier']['username'], name=application['applier']['name'])
        message['type'] = 0
        message['status'] = 0
        message['attachment'] = dict(application=str(result.inserted_id))
        self._mongo_conn.insert_msg(message)
        return True

    def find_application_by_id(self, application_id):
        application = self._mongo_conn.find_application_by_id(application_id)
        return convert_application_bson_type(application)

    def approve_application(self, application_id):
        self._mongo_conn.update_application_status(application_id, status=1)
        return True


def convert_application_bson_type(application):
    application['created_time'] = time.mktime(application['created_time'].timetuple())
    application['_id'] = str(application['_id'])
    return application
