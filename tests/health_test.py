import json
import unittest

from src.models import db
from src.app import create_app


class TestHealth(unittest.TestCase):
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
        response = self.request.get('/health')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['database']['status'], 'up')
        self.assertEqual(data['status'], 'up')
