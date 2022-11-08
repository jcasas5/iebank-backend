from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kitin2001@localhost/iebank'
db = SQLAlchemy(app)

from iebank_api.models import Account
from iebank_api import routes