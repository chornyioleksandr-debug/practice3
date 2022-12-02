import unittest
import app as tested_app
import json

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = tested_app.Flask_App.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r._status_code, 200)

if __name__ == '__main__':
    unittest.main()
