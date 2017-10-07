from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Patient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	username = db.Column(db.String(120), unique=True, nullable=False)
	age = db.Column(db.Integer, primary_key=False)
	diaries = db.relationship('Diary', backref='Patient', lazy=True)

	def __repr__(self):
		return '<Patient %r>' % self.title

class Diary(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	diaryInfo = db.Column(db.String(100000), nullable=True)
	user_ID = db.Column(db.Integer, db.ForeignKey('Patient.ID'),
   		nullable=False)

	def __repr__(self):
		return '<Diary %r>' % self.title
