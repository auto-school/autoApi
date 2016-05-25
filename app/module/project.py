# coding=utf-8

import time
from datetime import datetime

from flask import g

from db.pydb import get_db

import pymongo

from bson.objectid import ObjectId


def cal_member(team):
    current_person = 0
    for k in team:
        current_person += len(team[k])
    return current_person


class ProjectManager:

    def __init__(self):
        self.conn = get_db()

    def create_project(self, project):
        project['status'] = 0
        project['deadline'] = datetime.fromtimestamp(project['deadline'])
        project['created_time'] = datetime.now()
        project['team'] = dict()
        project['team']['charge_person'] = dict(id=g.user['username'], name=g.user['name'])
        project['team']['member'] = []
        project['team']['mentor'] = []
        project['team']['outside_mentor'] = []
        project['appliers'] = []
        project['creator'] = dict(id=g.user['username'], name=g.user['name'])

        result = self.conn.projects.insert_one(project)
        return result

    def find_all_project(self, **keyword):
        query = dict()
        status = keyword.get('status', None)
        if status:
            query['status'] = int(status)
        else:
            query['$and'] = [{'status': {'$ne': 2}}, {'status': {'$ne': 0}}]
        projects = list(self.conn.projects.find(query)
                    .skip(keyword['offset'])
                    .limit(keyword['limit'])
                    .sort([('created_time', pymongo.DESCENDING), ]))
        projects = map(convert_project_bson_type,projects)
        return projects

    def find_all_project_by_username(self, username):
        projects = list(self.conn.projects.find({'creator.id': username}))
        projects = map(convert_project_bson_type,projects)
        return projects

    def find_project_by_id(self, project_id):
        project = self.conn.projects.find_one({'_id':ObjectId(project_id)})
        return convert_project_bson_type(project)

    def approve_project(self, project_id):
        self.conn.projects.update_one(
            {'_id': ObjectId(project_id)},
            {
                '$set': {
                    "status": 1
                }
            }
        )
        return True

    def reject_project(self, project_id):
        self.conn.projects.update_one(
            {'_id': ObjectId(project_id)},
            {
                '$set': {
                    "status": 2
                }
            }
        )
        return True

    def close_project(self, project_id):
        self.conn.projects.update_one(
            {'_id': ObjectId(project_id)},
            {
                '$set': {
                    "status": 3
                }
            }
        )
        return True

    def find_projects_for_owner(self, username):
        return list(self.conn.projects.find({'team.charge_person.id':username}))

    def find_projects_for_participant(self, username):

        return list(self.conn.projects.find({
            '$or': [
                {'team.member.username': username},
                {'team.mentor.username': username},
                {'team.outside_mentor.username': username}
            ]
        }))


def convert_project_bson_type(project):
    project['created_time'] = time.mktime(project['created_time'].timetuple())
    project['deadline'] = time.mktime(project['deadline'].timetuple())
    project['_id'] = str(project['_id'])
    return project
