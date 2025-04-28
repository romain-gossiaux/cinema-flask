from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '776d09f67994a3fb15c5f66f147ebec9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:postgresql://localhost:5432/cinema'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anonyme:anonyme@localhost/cinema'
db = SQLAlchemy(app)

from . import routes