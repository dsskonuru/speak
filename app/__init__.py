# FLASK APPLICATION INSTANCE

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# application object as an instance of class Flask
app = Flask(__name__) # name is a predefined variable
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app, db)

# importing the route module
from app import routes
