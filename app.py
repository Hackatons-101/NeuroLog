from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime
import os.path
import tempfile
from linker import main

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello():
	return render_template('index.html')

@app.route("/", methods = ["POST"])
def my_form_post():
	main()
	return render_template('diary.html')



if __name__ == "__main__":
    app.run()
