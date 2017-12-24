# -*- coding: UTF-8 -*-
import os
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate,MigrateCommand
from app import create_app
from app.models import *
from log import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager.add_command('runserver', Server(use_debugger=True))

if __name__ == '__main__':
    logging.info('start server...')
    manager.run()