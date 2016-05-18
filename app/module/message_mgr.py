from datetime import datetime
import time
from application import ApplicationManager
from pydb import get_db

# about message status
# 0 => active
# 1 => expire or handled


class MessageManager():
    def __init__(self):
        self._mongo_conn = get_db()

    def add_message(self, msg):
        self._mongo_conn.insert_msg(msg)
        return True

    def find_message_for_receiver(self, username):
        messages = self._mongo_conn.find_all_messages_for_receiver(username)
        messages = map(get_attachment, messages)
        messages = map(convert_message_bson_type, messages)
        return messages

    def expire_message(self, message_id):
        result = self._mongo_conn.update_message_status(message_id, status=1)
        return result


def convert_message_bson_type(message):
    message['created_time'] = time.mktime(message['created_time'].timetuple())
    message['_id'] = str(message['_id'])
    return message


def get_attachment(message):
    if message['type'] == 0:
        message['attachment']['application'] = ApplicationManager().find_application_by_id(
            message['attachment']['application'])
    return message