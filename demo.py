from flask import Flask
from flask_sqlalchemy import SQLAlchemy


demo = Flask(__name__)
demo.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgrsql:password@localhost:5432/postgreql'
db=SQLAlchemy(demo)
@demo.route('/')

def index():
    return "Hellow world Great yay!"