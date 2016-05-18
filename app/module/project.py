# coding=utf-8

from datetime import datetime
from flask import g
import time
from pydb import get_db


def cal_member(team):
    current_person = 0
    for k in team:
        current_person += len(team[k])
    return current_person


class ProjectManager:

    def __init__(self):
        self._mongo_conn = get_db()

    def create_project(self, project):
        project['status'] = 0
        project['deadline'] = datetime.fromtimestamp(project['deadline'])
        project['created_time'] = datetime.now()
        project['team']['member'] = []
        project['team']['mentor'] = []
        project['team']['outside_mentor'] = []
        project['creator'] = dict(id=g.user['username'], name=g.user['name'])
        result = self._mongo_conn.insert_project(project)
        return result

    def find_all_project(self, **keyword):
        projects = self._mongo_conn.find_all_project(**keyword)
        projects = map(convert_project_bson_type,projects)
        return projects

    def add_member(self, join_info):
        result = self._mongo_conn.update_member(join_info)
        return result

    def find_all_project_by_username(self, username):
        projects = self._mongo_conn.find_all_project_by_username(username)
        projects = map(convert_project_bson_type,projects)
        return projects

    def find_project_by_id(self, project_id):
        project = self._mongo_conn.find_project_by_id(project_id)
        if project is None:
            return None
        return convert_project_bson_type(project)

    def approve_project(self, project_id):
        self._mongo_conn.update_project_status(project_id, status=1)
        return True

    def new_project(self, project):
        result = self._mongo_conn.insert_project(project)


def convert_project_bson_type(project):
    project['created_time'] = time.mktime(project['created_time'].timetuple())
    project['deadline'] = time.mktime(project['deadline'].timetuple())
    project['_id'] = str(project['_id'])
    return project
