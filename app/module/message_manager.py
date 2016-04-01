from db.factory import MongoFactory

# about message status
# 0 => active
# 1 => expire or handled


class MessageManager:
    def __init__(self):
        self._mongo_conn = MongoFactory().get_connection()

    def add_message(self, msg):
        self._mongo_conn.insert_msg(msg)

    def find_message_for_receiver(self, username):
        messages = self._mongo_conn.find_all_messages_for_receiver(username)
        return messages

    def expire_message(self, message_id):
        result = self._mongo_conn.update_message_status(message_id, status=1)
        return result



