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

    def insert_project(self, project):
        self.conn.projects.insert_one(project)
        return True

    def find_all_project(self, **keyword):
        query = dict()
        query['status'] = {'$ne': 0}
        status = keyword.get('status', None)
        if status:
            query['status'] = int(status)
        return list(self.conn.projects.find(query)
                    .skip(keyword['offset'])
                    .limit(keyword['limit'])
                    .sort([('created_time', pymongo.DESCENDING),]))

    def update_member(self, join_info):

        result = self.conn.projects.update_one(
                    {'_id':ObjectId(join_info['project-id'])},
                    {
                        '$push': {
                            'team.'+join_info['apply-role']:{
                                'id': join_info['applier-id'],
                                'name': join_info['applier-name']
                            }
                        }
                    }

                )
        return True

    def find_project_by_id(self, project_id):
        projects_cursor = self.conn.projects.find({'_id':ObjectId(project_id)})
        projects = []
        for project in projects_cursor:
            projects.append(project)
        if len(projects) > 0:
            return projects[0]
        return None

    def find_all_project_by_username(self,username):
        projects_cursor = self.conn.projects.find({'creator.id': username})
        projects = []
        for project in projects_cursor:
            projects.append(project)
        return projects

    def insert_msg(self, msg):
        self.conn.messages.insert_one(msg)
        return True

    def find_all_messages_for_receiver(self, username):
        msgs_cursor = self.conn.messages.find({'receiver.id': username})
        msgs = []
        for msg in msgs_cursor:
            msgs.append(msg)
        return msgs

    def update_message_status(self, message_id, status):

        result = self.conn.messages.update_one(
                    {'_id':ObjectId(message_id)},
                    {
                        '$set': {
                            "status":1
                        }
                    }

                )
        return True

    def insert_application(self, application):
        _id = self.conn.application.insert_one(application)
        return _id

    def find_application_by_id(self, application_id):
        return list(self.conn.application.find({'_id': ObjectId(application_id)}))[0]

    def update_application_status(self, application_id, status):
        self.conn.application.update_one(
                    {'_id':ObjectId(application_id)},
                    {
                        '$set': {
                            "status": status
                        }
                    }
                )
        return True

    def update_project_status(self, project_id, status):
        self.conn.projects.update_one(
                    {'_id':ObjectId(project_id)},
                    {
                        '$set': {
                            "status": status
                        }
                    }
                )
        return True


