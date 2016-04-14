import unittest
import authority


class MyTestCase(unittest.TestCase):

    def test_signup(self):
        user = dict(username='tzx', password='hhh')
        result = authority.signup(user['username'], user['password'])
        self.assertEqual(result, False)

    def test_login(self):
        user_wrong = dict(username='tzx', password='hhh')
        result = authority.valid_login(user_wrong['username'], user_wrong['password'])
        self.assertEqual(result, False)
        user_right = dict(username='tzx', password='123')
        result = authority.valid_login(user_right['username'], user_wrong['password'])
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
