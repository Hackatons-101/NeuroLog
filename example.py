import json
import os
from flask import Flask, render_template
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

humanName = "Bob"


tone_analyzer = ToneAnalyzerV3(
    username='0b57ea01-39f5-4365-be78-4c13c960b6df',
    password='jOy2l7J5pn7f',
    version='2016-05-19')


emotions = ["anger", "disgust", "fear", "joy", "sadness"]


parse = json.loads(json.dumps(tone_analyzer.tone(text='sometimes I just do not want to get out of bed.'),
                 indent=2))
things = []

for x in range(0,5):
	things.append(100*(parse['document_tone']['tone_categories'][0]['tones'][x]['score']))


app = Flask(__name__)
 
@app.route("/")

def hello():
	return render_template('index.html', name = humanName, anger= things[0], disgust = things[1], fear= things[2], joy = things[3], sadness = things[4])

 
if __name__ == "__main__":
    app.run()
