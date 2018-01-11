import plotly as py
from plotly.graph_objs import *

def plot_hbar(data_list):
    ''' Returns an interactive horizontal bar graph in the directory "Plots/"
        Takes as argument a list with:
          list[:][0] = hashtag (str)
          list[:][1] = number that hashtag is found '''
    occurances = []
    tags = []
    for item in data_list:
        tags.insert(0, item[0])
        occurances.insert(0, item[1])

    data = [Bar(x=occurances, y=tags, orientation='h', marker=dict(color='rgb(192,248,248)'))]
    layout = dict(title='Collected hashtags', xaxis=dict(title='Occurance'))
    figure = dict(data=data, layout=layout)
    py.offline.plot(figure, filename='Plots/overview-bar.html')
