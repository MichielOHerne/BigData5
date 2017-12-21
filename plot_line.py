import plotly as py
from plotly.graph_objs import *
import datetime

def plot_line(data_list):
    ''' Returns an interactive line plot in the directory "Plots/"
        Takes as argument one list with at least:
          list[0] = name (str)
          list[1:] = all messages (list)
          list[1:][0] = message (str)
          list[1:][1] = sentiment (list)
          list[1:][1][0] = compound (float)
          list[1:][2] = timestamp (int) '''
    x_axis = []
    y_axis = []
    x_moving_avg = []
    y_moving_data = []
    messages = []
    total = 0
    for i in range(1, len(data_list)):
        timestamp_e = datetime.datetime.fromtimestamp(data_list[i][2]).strftime('%Y-%m-%d %H:%M:%S')    # Extended timestamp
        timestamp_s = datetime.datetime.fromtimestamp(data_list[i][2]).strftime('%Y-%m-%d %H:30')       # Short timestamp
        x_axis.append(timestamp_e)
        y_axis.append(data_list[i][1][0])   # Compound
        messages.append("Compound: " + str(data_list[i][1][0]) + "<br><i>\"" + str(data_list[i][0]) + "\"</i>")   # Message
        total = total + data_list[i][1][0]  # Total compound
        # Moving average data
        if timestamp_s in x_moving_avg:
            y_moving_data[len(y_moving_data)-1].append(data_list[i][1][0])
        else:
            x_moving_avg.append(timestamp_s)
            y_moving_data.append([data_list[i][1][0]])
    avg = round(total/(len(data_list)-1), 3)
    # Moving average
    y_moving_avg = []
    for moment in y_moving_data:
        sum = 0
        for item in moment:
            sum = sum + item
        y_moving_avg.append(round(sum/len(moment), 2))
    # Lines
    line = Scatter(x=x_axis, y=y_axis, text=messages, mode='markers', name='Individual message', hoverinfo='text', line=dict(color='rgb(80,80,80)'))
    avg_ref = Scatter(x=[x_axis[0], x_axis[len(x_axis)-1]], y=[avg]*2, text=['Average: ' + str(avg)]*2, line=dict(shape='linear', dash='dash', color='rgb(240,192,48)'), name="Total average: " + str(avg), hoverinfo='text')
    mov_avg = Scatter(x=x_moving_avg, y=y_moving_avg, text=['Moving average']*len(x_moving_avg), line=dict(shape='spline', color='rgb(24,192,24)'), name='Moving average (hour)', hoverinfo='y+text')
    layout = dict(title='Data for <b>' + data_list[0] + '</b>', xaxis=dict(title='Time'), yaxis=dict(title='Compound', range=[-1, 1]))
    figure = dict(data=Data([line, mov_avg, avg_ref]), layout=layout)
    py.offline.plot(figure, filename='Plots/sentiment-line.html')
