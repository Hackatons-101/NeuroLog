import json
import math
import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3
import tempfile
from linker import Diary
import plotly.plotly as py
import plotly.graph_objs as go

from io import BytesIO

# MatPlotlib
import matplotlib.pyplot as plt, mpld3
from matplotlib import pylab

# Scientific libraries
from numpy import arange,array,ones
import pandas

app = Flask(__name__) 


textInput = Diary.query.order_by(Diary.time)[-1]
inputText = textInput.diaryInfo
humanName = "Cathy" 

tone_analyzer = ToneAnalyzerV3(
    username='0b57ea01-39f5-4365-be78-4c13c960b6df',
    password='jOy2l7J5pn7f',
    version='2016-05-19')


emotions = ["anger", "disgust", "fear", "joy", "sadness"]

inputList = []
parseList = []
for x in range(0,5):
	textInputter = Diary.query.order_by(Diary.time)[-5+x]
	inputTextter = textInputter.diaryInfo
	inputList.append(inputTextter)
	parseList.append(json.loads(json.dumps(tone_analyzer.tone(text= inputTextter),
                 indent=2))) 


parse = json.loads(json.dumps(tone_analyzer.tone(text= inputText),
                 indent=2))

things = []
thingsPastFive = []
meanSadness = 0

for x in range(0,5):
	thingsPastFive.append(100*(parseList[x]['document_tone']['tone_categories'][0]['tones'][1]['score']))
	meanSadness = meanSadness+(thingsPastFive[x])

meanSadness= meanSadness/5


temp = 0
for x in range(0,5):
	temp = temp + (x-meanSadness)*(x-meanSadness)


standardDeviation = math.sqrt(temp/5)

weightedAverage = (6*thingsPastFive[4] + 3*thingsPastFive[3])/9


warningText = ""
if(weightedAverage > standardDeviation+ meanSadness):
	warningText = "We have detected an irregular level of sadness. We recommend looking into this patient."
else:
	warningText = "This patient is doing fine."

for x in range(0,5):
	things.append(100*(parse['document_tone']['tone_categories'][0]['tones'][x]['score']))

linearPlot = plt.plot(thingsPastFive, 'ks-', mec='w', mew=5, ms=20)






@app.route("/analyze", methods=['GET', 'POST'])
def hello():
	return render_template('psychologistView.html', name = humanName, anger= things[0], disgust = things[1], fear= things[2], joy = things[3], sadness = things[4],
			day0 = thingsPastFive[0], day1 = thingsPastFive[1], day2 = thingsPastFive[2], day3 = thingsPastFive[3], day4 = thingsPastFive[4], meanSadness = meanSadness,
			warningText = warningText)

 
if __name__ == "__main__":
    app.run()
