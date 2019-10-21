from datetime import datetime
from flask_restful import Resource
from flask.json import jsonify
from http import HTTPStatus
from src.models import db

import logging

HEALTH_UP = 'up'
HEALTH_DOWN = 'down'



class HealthCheckController(Resource):
    def get(self):
        database_health_check = self.__database_status()

        is_all_up = all([
            health_check.get('status', '') == HEALTH_UP for health_check in [
                database_health_check
            ]
        ])

        response = jsonify({
            'status': HEALTH_UP if is_all_up else HEALTH_DOWN,
            'timestamp': datetime.now().astimezone(),
            'database': database_health_check
        })

        response.status_code = HTTPStatus.OK if is_all_up \
            else HTTPStatus.SERVICE_UNAVAILABLE

        return response

    def __database_status(self):
        try:
            now = datetime.now().astimezone()
            timestamp = db.session.execute('SELECT now()') \
                .fetchone()[0]
            latency = timestamp - now

            return {
                'status': HEALTH_UP,
                'timestamp': timestamp,
                'latency': latency.total_seconds()
            }
        except Exception as ex:
            logging.debug(ex)
            logging.error(ex)
            return {
                'status': HEALTH_DOWN,
                'error': ex.__class__.__name__
            }
