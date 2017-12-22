from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config
from .api import api

db = SQLAlchemy()

def create_app(config_name):
    """create app"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    
    #register blueprint
    app.register_blueprint(api,url_prefix='/api')
    
    return app
    