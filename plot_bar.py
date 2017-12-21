import plotly as py
import datetime

def plot_bar(data_list, color_neg='rgb(149,28,28)', color_neu='rgb(166,118,42)', color_pos='rgb(128,192,50)'):
    ''' Returns an interactive bar graph in the directory "Plots/"
        Takes as argument a list with:
          list[0] = name (str)
          list[1:] = all messages (list)
          list[1:][0] = message (str)
          list[1:][1] = sentiment (list)
          list[1:][1][0] = compound (float)
          list[1:][1][1] = negative (float)
          list[1:][1][2] = neutral (float)
          list[1:][1][3] = positive (float)
          list[1:][2] = timestamp (int)
        Optional arguments are the colors of the different bars '''
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

    layout = dict(title='Data for <b>' + data_list[0] + '</b>', xaxis=dict(title='Time'), yaxis=dict(title='Sentiment'), barmode='relative')
    figure = dict(data=[neg, neu, pos], layout=layout)
    py.offline.plot(figure, filename='Plots/sentiment-bar.html')
