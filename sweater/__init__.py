from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'Danila'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Jomangos123@localhost:1234/web'
db = SQLAlchemy(app)
manager = LoginManager(app)

from sweater import models, routes
