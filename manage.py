# -*- coding: UTF-8 -*-
import os
from flask_script import Manager, Shell, Server
from app import create_app,db
from log import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()

manager = Manager(app)
manager.add_command('runserver', Server(use_debugger=False))

@manager.command
def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    logging.info('start server...')
    manager.run(default_command='runserver')