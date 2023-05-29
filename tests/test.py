import os
import unittest
from main import app


class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_find_most_common_word(self):
        with open('test.txt', 'w') as f:
            f.write('the quick brown fox jumps over the lazy dog')
        with open('test.txt', 'r') as f:
            data = {'text': f.read()}
        response = self.app.post('/checkFile', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'the': 2})

        os.remove('test.txt')

