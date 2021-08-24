import pandas as pd
import csv
import plotly.figure_factory as ff
import random
import statistics
import plotly.graph_objects as go

df = pd.read_csv("pro/sampleDistribution/medium_data.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
stdDev = statistics.stdev(data)

print("Population Mean Is",mean)
print("Population Standard Deviation Is",stdDev)

def randomSetOfMean(counter):
    dataSet = []
    for i in range(1,counter):
        data_index = random.randint(0,len(data)-1)
        value = data[data_index]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def showFigure(meanList):
    dataFile = meanList
    fig = ff.create_distplot([dataFile],["Temperature"],show_hist=False)
    fig.show()

def main():
    meanList = []
    for i in range(0,1000):
        meanSet = randomSetOfMean(100)
        meanList.append(meanSet)
    showFigure(meanList)
    print("Sampling Mean = ",statistics.mean(meanList))
main()