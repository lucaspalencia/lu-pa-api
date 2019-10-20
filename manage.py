import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from src.app import create_app
from src.models import db
from seeds import run_seeds

app = create_app(os.getenv('ENVIRONMENT') or 'dev')
db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0')


@manager.command
def seed():
    run_seeds()


if __name__ == '__main__':
    manager.run()
