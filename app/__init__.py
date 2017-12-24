# -*- coding: UTF-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

def create_app(config_name):
    """create app"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    db.create_all(app=app)
    
    #register blueprint
    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint,url_prefix='/api')
    
    return app
    