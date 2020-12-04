# -*- coding: utf-8 -*-
from flask import Flask
from config import Config
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_babel import lazy_gettext as _l

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes, models