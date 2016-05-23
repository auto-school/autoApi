import time
from datetime import datetime

from flask import g
from db.pydb import get_db
from project import ProjectManager
from bson.objectid import ObjectId


class ApplicationManager:

    def __init__(self):
        self.conn = get_db()

    def insert_application(self, application):
        application['created_time'] = datetime.now()
        applier = dict(username=g.user['username'], name=g.user['name'])
        application['applier'] = applier
        application['status'] = 0
        pm = ProjectManager()
        apply_project = pm.find_project_by_id(application['project']['id'])
        self.conn.projects.update_one(
            {'_id': ObjectId(application['project']['id'])},
            {
                '$push': {
                    'appliers': applier
                }
            }
        )
        application['project']['name'] = apply_project['name']
        result = self.conn.application.insert_one(application)
        message = dict()
        message['created_time'] = datetime.now()
        message['receiver'] = apply_project['creator']['id']
        message['sender'] = applier
        message['type'] = 0
        message['status'] = 0
        message['attachment'] = dict(application=str(result.inserted_id))
        self.conn.messages.insert_one(message)
        return True

    def find_application_by_id(self, application_id):
        application = self.conn.application.find_one({'_id': ObjectId(application_id)})
        return convert_application_bson_type(application)

    def approve_application(self, application_id):

        self.conn.application.update_one(
            {'_id': ObjectId(application_id)},
            {
                '$set': {
                    "status": 1
                }
            }
        )

        role_list = ['member', 'mentor', 'outside_mentor']
        application = self.conn.application.find_one({'_id': ObjectId(application_id)})
        self.conn.projects.update_one(
            {'_id': ObjectId(application['project']['id'])},
            {
                '$push': {
                    'team.'+role_list[application['role']]: application['applier']
                },
                '$pull': {
                    'appliers': application['applier']
                }
            }
        )

        message = dict(status=0,
                       attachment=dict(application=application_id),
                       receiver=application['applier']['username'],
                       created_time=datetime.now(),
                       type=1,
                       sender=dict(username=g.user['username'], name=g.user['name']))

        self.conn.messages.insert_one(message)

        return True

    def reject_application(self, application_id):
        self.conn.application.update_one(
            {'_id': ObjectId(application_id)},
            {
                '$set': {
                    "status": 2
                }
            }
        )

        role_list = ['member', 'mentor', 'outside_mentor']
        application = self.conn.application.find_one({'_id': ObjectId(application_id)})
        self.conn.projects.update_one(
            {'_id': ObjectId(application['project']['id'])},
            {
                '$pull': {
                    'appliers': application['applier']
                }
            }
        )

        message = dict(status=0,
                       attachment=dict(application=application_id),
                       receiver=application['applier']['username'],
                       created_time=datetime.now(),
                       type=2,
                       sender=dict(username=g.user['username'], name=g.user['name']))

        self.conn.messages.insert_one(message)
        return True


def convert_application_bson_type(application):
    application['created_time'] = time.mktime(application['created_time'].timetuple())
    application['_id'] = str(application['_id'])
    return application
