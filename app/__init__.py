# FLASK APPLICATION INSTANCE

from flask import Flask
from config import Config

# application object as an instance of class Flask
app = Flask(__name__) # name is a predefined variable
app.config.from_object(Config)

# importing the route module
from app import routes
