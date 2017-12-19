# Zorg dat de map "Plots/" aanwezig is om alles in op te slaan!
import plotly as py
from plotly.graph_objs import *
import datetime

def plot_line(data_list):
    name = data_list[0]
    x_axis = []
    y_axis = []
    x_moving_avg = []
    y_moving_data = []
    messages = []
    total = 0
    for i in range(1, len(data_list)):
        timestamp_e = datetime.datetime.fromtimestamp(data_list[i][2]).strftime('%Y-%m-%d %H:%M:%S') # Extended timestamp
        timestamp_s = datetime.datetime.fromtimestamp(data_list[i][2]).strftime('%Y-%m-%d %H:30') # Short timestamp
        x_axis.append(timestamp_e)
        y_axis.append(data_list[i][1][0])  # Compound
        messages.append("<i>\"" + str(data_list[i][0]) + "\"</i>")   # Message
        total = total + data_list[i][1][0] # Total compound
        # Moving average data
        if (timestamp_s in x_moving_avg):
            y_moving_data[len(y_moving_data)-1].append(data_list[i][1][0])
        else:
            x_moving_avg.append(timestamp_s)
            y_moving_data.append([data_list[i][1][0]])
    avg = round(total/(len(data_list)-1),3)
    # Moving average
    y_moving_avg = []
    for moment in y_moving_data:
        sum = 0
        for item in moment:
            sum = sum + item
        y_moving_avg.append(round(sum/len(moment),2))
    # Lines
    line = Scatter(x=x_axis, y=y_axis, text=messages, mode='markers', name='Individual message', hoverinfo='y+text', line=dict(color='rgb(80,80,80)'))
    avg_ref = Scatter(x=[x_axis[0], x_axis[len(x_axis)-1]], y=[avg]*2, text=['Average: ' + str(avg)]*2, line=dict(shape='linear', dash = 'dash', color='rgb(240,192,48)'), name="Total average: "+ str(avg), hoverinfo='text')
    mov_avg = Scatter(x=x_moving_avg, y=y_moving_avg, text=['Moving average']*len(x_moving_avg), line=dict(shape='spline', color='rgb(24,192,24)'), name='Moving average (hour)', hoverinfo='y+text')
    layout = dict(title = 'Data for <b>' + name +'</b>', xaxis = dict(title = 'Time'), yaxis = dict(title = 'Compound', range = [-1, 1]))
    figure = dict(data=Data([line, mov_avg, avg_ref]), layout=layout)
    py.offline.plot(figure, filename = 'Plots/sentiment-line.html')

def plot_bar(data_list, color_neg='rgb(149,28,28)', color_neu='rgb(166,118,42)', color_pos='rgb(154,206,50)'):
    name = data_list[0]
    x_axis = []
    neg_bar, neu_bar, pos_bar = [], [], []
    messages = []
    for i in range(1, len(data_list)):
        x_axis.append(datetime.datetime.fromtimestamp(data_list[i][2]).strftime('%Y-%m-%d %H:%M:%S'))  # Timestamp
        neg_bar.append(data_list[i][1][1])  # Negative
        neu_bar.append(data_list[i][1][2])  # Neutral
        pos_bar.append(data_list[i][1][3])  # Positive
        messages.append(data_list[i][0])    # Message

    neg = {'x': x_axis, 'y': neg_bar, 'name': 'Negative', 'type': 'bar', 'marker': dict(color=color_neg)}
    neu = {'x': x_axis, 'y': neu_bar, 'name': 'Neutral', 'type': 'bar', 'marker': dict(color=color_neu)}
    pos = {'x': x_axis, 'y': pos_bar, 'text': messages, 'name': 'Positive', 'type': 'bar', 'marker': dict(color=color_pos)}

    layout = dict(title = 'Data for <b>' + name +'</b>', xaxis = dict(title = 'Time'), yaxis = dict(title = 'Sentiment'), barmode = 'relative')
    figure = dict(data=[neg, neu, pos], layout=layout)
    py.offline.plot(figure, filename = 'Plots/sentiment-bar.html')


zinloos = ["#kerst", ["het is bijna #kerst", [0.3, 0.2, 0.5, 0.3], 1375432865], ["heb zin in #kerst", [0.4, 0.1, 0.5, 0.4], 1375433865], ["ik hou zooo veel van #kerst", [0.8, 0.1, 0.2, 0.7], 1375436864], ["Wat praten we over #kerst in de zomer?", [0.2, 0.1, 0.7, 0.2], 1375458723], ["Het is #kerst over 145 dagen!", [0.3, 0, 0.6, 0.4], 1375474832], ["Wat heb ik een hekel aan #kerstmuziek", [-0.6, 0.6, 0.2, 0.2], 1375476592], ["Zo blij! Ik hoef helemaal niet aan #kerstinkopen te denken", [0.5, 0.1, 0.2, 0.7], 1375476912]]
plot_line(zinloos)
plot_bar(zinloos)
