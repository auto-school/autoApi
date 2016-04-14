import unittest
from conn import Connection


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = Connection()

    def test_mongo_search_user(self):
        users = self.conn.find_user_by_username('tzx')
        print users

if __name__ == '__main__':
    unittest.main()
