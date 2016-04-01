from config import DbConfig
import MySQLdb
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo

# using borg design pattern, every instance share a connection


class AbstractConnection:

    def __init__(self, sql):
        self.config = DbConfig().get_config(sql)

    def _get_instance(self):
        raise NotImplementedError


class MysqlConnection(AbstractConnection):
    __share_state = {}

    def __init__(self):
        AbstractConnection.__init__(self,'mysql')
        self.__share_state['config'] = self.config
        self.__dict__ = self.__share_state
        if not hasattr(self, 'conn_instance'):
            print 'create...'
            self._conn_instance = self._get_instance()

    def _get_instance(self):
        conn = MySQLdb.connect(host=self.config['host'],
                               user=self.config['user'],
                               passwd=self.config['password'],
                               db=self.config['database'],
                               port=int(self.config['port']))
        return conn

    def find_user_by_username(self, username):
        cursor = self._conn_instance.cursor()
        cursor.execute("select * from user where username = '%s'" % username)
        results = cursor.fetchall()
        return results

    def insert_user(self,username,password):
        cursor=self._conn_instance.cursor()
        result=cursor.execute("insert into user(username,password)values('%s','%s')"% (username,password))
        self._conn_instance.commit()
        return result


class MongoConnection(AbstractConnection):
    __share_state = {}

    def __init__(self):
        AbstractConnection.__init__(self, 'mongo')

        self.__share_state['config'] = self.config
        self.__dict__ = self.__share_state
        if not hasattr(self, 'conn_instance'):
            print 'create...'
            self._conn_instance = self._get_instance()

    def _get_instance(self):
        client = MongoClient("localhost:27017")
        conn = client.mobile
        return conn

    def insert_project(self, project):
        self._conn_instance.projects.insert_one(project)
        return True

    def find_all_project(self):
        projects_cursor = self._conn_instance.projects.find().sort([('created_time', pymongo.DESCENDING),])
        projects = []
        for project in projects_cursor:
            projects.append(project)
        return projects

    def update_member(self, join_info):

        result = self._conn_instance.projects.update_one(
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
        projects_cursor = self._conn_instance.projects.find({'_id':ObjectId(project_id)})
        projects = []
        for project in projects_cursor:
            projects.append(project)
        if len(projects) > 0:
            return projects[0]
        return None

    def find_all_project_by_username(self,username):
        projects_cursor = self._conn_instance.projects.find({'creator.id': username})
        projects = []
        for project in projects_cursor:
            projects.append(project)
        return projects

    def insert_msg(self, msg):
        self._conn_instance.messages.insert_one(msg)
        return True

    def find_all_messages_for_receiver(self, username):
        msgs_cursor = self._conn_instance.messages.find({'receiver': username})
        msgs = []
        for msg in msgs_cursor:
            msgs.append(msg)
        return msgs

    def update_message_status(self, message_id, status):

        result = self._conn_instance.messages.update_one(
                    {'_id':ObjectId(message_id)},
                    {
                        '$set': {
                            "status":1
                        }
                    }

                )
        return True


class RedisConnection(AbstractConnection):
    __share_state = {}

    def __init__(self):
        AbstractConnection.__init__(self, 'redis')
        self.__share_state['config'] = self.config
        self.__dict__ = self.__share_state
        if not hasattr(self, 'conn_instance'):
            print 'create...'
            self._conn_instance = self._get_instance()

    def _get_instance(self):
        return 'Redis connection'


if __name__ == '__main__':
    test = MongoConnection()
    msgs = test.find_all_messages_for_receiver('1352863')
    print msgs