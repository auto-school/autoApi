import unittest
from module import authority


class MyTestCase(unittest.TestCase):
    def test_signup_already_exist(self):
        self.assertEqual(authority.signup('tzx', '123'), False)

    def test_signup_no_exist(self):
        self.assertEqual(authority.signup('tzxe', '1234'), True)

if __name__ == '__main__':
    unittest.main()
