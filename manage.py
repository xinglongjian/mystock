# -*- coding: UTF-8 -*-
import os
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate,MigrateCommand
from app import create_app
from app.models import *
from log import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def createall():
    db.create_all()

manager = Manager(app)
manager.add_command('runserver', Server(use_debugger=True))
manager.add_command("db", MigrateCommand)
manager.add_command("dbcreate", createall())

# @manager.command
# def make_shell_context():
#     return dict(app=app, db=db)
# manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    logging.info('start server...')
    manager.run()