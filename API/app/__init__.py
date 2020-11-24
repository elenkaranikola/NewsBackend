# -*- coding: utf-8 -*-
from flask import Flask
from config import Config
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes, models