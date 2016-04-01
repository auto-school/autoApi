# coding=utf-8
from db.factory import MongoFactory, MysqlFactory
import format


def cal_member(team):
    current_person = 0
    for k in team:
        current_person += len(team[k])
    return current_person


class ProjectManager:
    def __init__(self):
        self._mysql_conn = MysqlFactory().get_connection()
        self._mongo_conn = MongoFactory().get_connection()

    def create_project(self, project):
        result = self._mongo_conn.insert_project(project)
        return result

    def apply_project(self, applier_id, project_id):
        pass

    def approve_applier(self, applier_id, project_id):
        pass

    def start_project(self, project_id):
        pass

    def finish_project(self, project_id):
        pass

    def cancel_project(self, project_id):
        pass

    def find_all_project(self):
        projects = self._mongo_conn.find_all_project()
        return projects

    def add_member(self, join_info):
        result = self._mongo_conn.update_member(join_info)
        return result

    def find_all_project_by_username(self, username):
        projects = self._mongo_conn.find_all_project_by_username(username)
        return projects

    def find_project_by_id(self, project_id):
        project = self._mongo_conn.find_project_by_id(project_id)
        if project is None:
            return None
        return project

