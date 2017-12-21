import plotly as py
from plotly.graph_objs import *
import datetime

def plot_pie(data_list, hot_one=False):
    ''' Returns an interactive line plot in the directory "Plots/"
        Takes as argument a list with:
          list[0] = name (str)
          list[1:] = all messages (list)
          list[1:][0] = message (str)
          list[1:][1] = sentiment (list)
          list[1:][1][0] = compound (float)
          list[1:][2] = timestamp (int)
        Optional argument, switch between two types of classifications: hot_one=
          True: Only the highest value of negative, neutral, positive counts
          False: Takes the fractions of each negative, neutral, positive into account (default) '''
    colors = ['rgb(149,28,28)', 'rgb(166,118,42)', 'rgb(128,192,50)']
    length = len(data_list)-1
    timestamp = [datetime.datetime.fromtimestamp(data_list[1][2]).strftime('%d-%m-%Y (%H:%M)'), datetime.datetime.fromtimestamp(data_list[len(data_list)-1][2]).strftime('%d-%m-%Y (%H:%M)')]
    name = 'Data for '+str(length)+' messages with <b>'+data_list[0]+'</b><br><span style="font-size:64%;"><i>Data between '+timestamp[0]+' and '+timestamp[1]+'</i></span>'
    scores = [0, 0, 0]
    if hot_one:
        for i in range(1, len(data_list)):
            highest = max([data_list[i][1][1], data_list[i][1][2], data_list[i][1][3]])
            print(highest)
            for j in range(3):
                if data_list[i][1][j+1] == highest:
                    scores[j] = scores[j] + 1
    else:
        for i in range(1, len(data_list)):
            scores[0] = scores[0] + data_list[i][1][1]  # Negative
            scores[1] = scores[1] + data_list[i][1][2]  # Neutral
            scores[2] = scores[2] + data_list[i][1][3]  # Positive
    for i in range(len(scores)):
        scores[i] = round(scores[i]/length, 4)

    data = Pie(labels=['Negative','Neutral','Positive'], values=scores, hoverinfo='label+percent', textinfo='percent', textfont=dict(size=20, color='rgb(24,24,24)'), marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    py.offline.plot(dict(data=[data], layout=dict(title=name)), filename='Plots/sentiment-pie.html')
