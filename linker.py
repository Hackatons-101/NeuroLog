from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime
import os.path
import tempfile



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(tempfile.gettempdir(), 'test.db')
db = SQLAlchemy(app) 	



class Patient(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	username = db.Column(db.String(120), unique=True, nullable=False)
	age = db.Column(db.Integer, primary_key=False)
	diaries = db.relationship('Diary', backref='patient', lazy='dynamic')


class Diary(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	diaryInfo = db.Column(db.String(100), nullable=True)
	user_ID = db.Column(db.Integer, db.ForeignKey('patient.id'))


size = db.session.query(Diary).count()
print(size)
db.session.close();

@app.route("/", methods = ["GET"])
def hello():
	return render_template('diary.html')

@app.route("/", methods = ["POST"])
def my_form_post():
	txt = request.form["diary"]
	print(txt)
	newDiary = Diary(diaryInfo = txt)
	db.session.add(newDiary)
	db.session.commit()
	return render_template('diary.html')



if __name__ == "__main__":
    app.run()
