import plotly as py
from plotly.graph_objs import *
import datetime

def plot_line(data_list):
    name = data_list[0]
    x_axis = []
    y_axis = []
    for i in range(1, len(data_list)):
        x_axis.append(datetime.datetime.fromtimestamp(data_list[i][2]).strftime('%Y-%m-%d %H:%M:%S'))  # Timestamp
        y_axis.append(data_list[i][1][0])  # Compound
    line = Scatter(x=x_axis, y=y_axis, line=dict(shape='linear'))  # linear/ spline
    layout = dict(title = 'Data for <b>' + name +'</b>', xaxis = dict(title = 'Time'), yaxis = dict(title = 'Positive/ Negative compound'))
    figure = dict(data=Data([line]), layout=layout)
    py.offline.plot(figure, filename = 'Plots/sentiment-line.html')

zinloos = ["#kerst", ["het is bijna #kerst", [0.3, 0.2, 0.5, 0.3], 1375432865], ["heb zin in #kerst", [0.2, 0.1, 0.7, 0.2], 1375436351], ["ik hou zooo veel van #kerst", [0.8, 0.1, 0.2, 0.7], 1375436864], ["Wat heb ik een hekel aan #kerstmuziek", [-0.6, 0.6, 0.2, 0.2], 1375476592]]
plot_line(zinloos)
