import time

from db.pydb import get_db
from application import ApplicationManager
from bson.objectid import ObjectId


# about message status
# 0 => active
# 1 => expire or handled


class MessageManager():
    def __init__(self):
        self.conn = get_db()

    def add_message(self, msg):
        self.conn.messages.insert_one(msg)
        return True

    def find_messages_for_receiver(self, username):
        messages = list(self.conn.messages.find({'receiver': username}))
        messages = map(get_attachment, messages)
        messages = map(convert_message_bson_type, messages)
        return messages

    def find_message_by_id(self, mid):
        msg = self.conn.messages.find_one({'_id':ObjectId(mid)})
        msg = get_attachment(msg)
        msg = convert_message_bson_type(msg)
        return msg

    def expire_message(self, message_id):
        self.conn.messages.update_one(
            {'_id': ObjectId(message_id)},
            {
                '$set': {
                    "status": 1
                }
            }

        )
        return True


def convert_message_bson_type(message):
    message['created_time'] = time.mktime(message['created_time'].timetuple())
    message['_id'] = str(message['_id'])
    return message


def get_attachment(message):
    if message['type'] == 0:
        message['attachment']['application'] = ApplicationManager().find_application_by_id(
            message['attachment']['application'])
    return message