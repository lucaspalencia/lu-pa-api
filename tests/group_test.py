import json
import unittest
import os

from src.models import db
from src.app import create_app
from seeds import run_seeds


class TestGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = create_app('test')
        app.app_context().push()
        db.init_app(app)
        cls.request = app.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        run_seeds()

        response = self.request.get(
            '/events/1/groups',
            headers={'x-api-key': os.getenv('API_KEY')}
        )
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 16)
        self.assertEqual(len(data[0]['teams']), 5)
