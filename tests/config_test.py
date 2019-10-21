from src.config import config_by_environment
from src.app import create_app

app = create_app('test')


def test_development_config():
    app.config.from_object(config_by_environment['dev'])
    assert app.config['DEBUG']


def test_testing_config():
    app.config.from_object(config_by_environment['test'])
    assert app.config['DEBUG']


def test_production_config():
    app.config.from_object(config_by_environment['prod'])
    assert not app.config['DEBUG']
