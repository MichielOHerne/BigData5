# Zorg dat de map "Plots/" aanwezig is om alles in op te slaan!
import plotly as py
from plotly.graph_objs import *
import datetime

def plot_line(data_list):
    name = data_list[0]
    x_axis = []
    y_axis = []
    messages = []
    total = 0
    for i in range(1, len(data_list)):
        x_axis.append(datetime.datetime.fromtimestamp(data_list[i][2]).strftime('%Y-%m-%d %H:%M:%S'))  # Timestamp
        y_axis.append(data_list[i][1][0])  # Compound
        messages.append(data_list[i][0])   # Message
        total = total + data_list[i][1][0]
    line = Scatter(x=x_axis, y=y_axis, text=messages, line=dict(shape='linear'), name='Positive/ Negative compound')
    avg = total/(len(data_list)-1)
    avg_ref = Scatter(x=[x_axis[0], x_axis[len(x_axis)-1]], y=[avg]*2, text=['Average']*2, line=dict(shape='spline'), name='Average')
    layout = dict(title = 'Data for <b>' + name +'</b>', xaxis = dict(title = 'Time'), yaxis = dict(title = 'Positive/ Negative compound'))
    figure = dict(data=Data([line, avg_ref]), layout=layout)
    py.offline.plot(figure, filename = 'Plots/sentiment-line.html')

zinloos = ["#kerst", ["het is bijna #kerst", [0.3, 0.2, 0.5, 0.3], 1375432865], ["heb zin in #kerst", [0.2, 0.1, 0.7, 0.2], 1375433865], ["ik hou zooo veel van #kerst", [0.8, 0.1, 0.2, 0.7], 1375436864], ["Wat heb ik een hekel aan #kerstmuziek", [-0.6, 0.6, 0.2, 0.2], 1375476592]]
plot_line(zinloos)
