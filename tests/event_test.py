import json
import unittest
import os

from src.models import Event
from src.models import db
from src.app import create_app


class TestEvent(unittest.TestCase):
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
        event = Event(
            id=1,
            name='Campeonato teste',
            start_date='2019-10-17 06:09:38',
            end_date='2019-11-17 06:09:38',
        )

        db.session.add(event)
        db.session.commit()

        response = self.request.get(
            '/events/1',
            headers={'x-api-key': os.getenv('API_KEY')}
        )
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Campeonato teste')
