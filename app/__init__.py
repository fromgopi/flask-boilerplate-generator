import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail 

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')

db = SQLSchema()
ma = Marshmallow()
bcrypt = Bcrypt()
migrate = Migrate()
seeder = seeder()
jwt = JWTManager()
mail = Mail()
cors = CORS()

""" Fuction that creates Flask instance and returns it.
    @Param: None
    @return: Flask Instance.
    @raise: None
"""
def create_app():
    app = Flask(__name__)
    load_dotenv(os.path.join(APP_ROOT, '.env'))


"""A private function to config all the required config items
   @Param: Instance of Flask
   @return: None
   @raise: unable to load .env file.500 
"""
def config_env(app):
    pass
