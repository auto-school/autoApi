from datetime import datetime
import time
from conn import Connection
import application
import project
# about message status
# 0 => active
# 1 => expire or handled

mongo_conn = Connection()


def add_message(msg):
    mongo_conn.insert_msg(msg)
    return True


def find_message_for_receiver(username):
    messages = mongo_conn.find_all_messages_for_receiver(username)
    messages = map(get_attachment, messages)
    messages = map(convert_message_bson_type, messages)
    return messages


def expire_message(message_id):
    result = mongo_conn.update_message_status(message_id, status=1)
    return result


def convert_message_bson_type(message):
    message['created_time'] = time.mktime(message['created_time'].timetuple())
    message['_id'] = str(message['_id'])
    return message


def get_attachment(message):
    if message['type'] == 0:
        message['attachment'] = application.ApplicationManager.find_application_by_id(message['attachment']['project']['id'])
    return message