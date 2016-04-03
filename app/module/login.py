import unittest
import authority


class MyTestCase(unittest.TestCase):
    def test_login(self):
        self.assertEqual(authority.valid_login('tzx', '2131'), True)


if __name__ == '__main__':
    unittest.main()
