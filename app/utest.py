import unittest
from module.db.factory import MongoFactory


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self._mongo_conn = MongoFactory().get_connection()

    def test_mongo_find_by_id(self):
        project = self._mongo_conn.find_project_by_id('56e6a9c9c1f2b40be3239f65')
        print project
        self.assertEqual(type(project), dict)
        project = self._mongo_conn.find_project_by_id('56e6a9c9c1f2b40be3239f64')
        self.assertEqual(project, None)


if __name__ == '__main__':
    unittest.main()
