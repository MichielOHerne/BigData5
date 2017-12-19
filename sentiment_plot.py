# Make sure that the directory "Plots/" exist to store all the plots!
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


def plot_world(data_list, color_neg='rgb(149,28,28)', color_neu='rgb(166,118,42)', color_pos='rgb(128,192,50)', loc_mode="ISO-3"):
    ''' Returns an interactive world map with the data in the directory "Plots/"
        Takes as argument a list with:
          list[0] = name (str)
          list[1:] = all messages (list)
          list[1:][0] = message (str)
          list[1:][1] = sentiment (list)
          list[1:][1][0] = compound (float)
          list[1:][2] = timestamp (int)
          list[1:][3] = country_code (str) -> No error message when incorrect!
        Optional arguments are the colors in the compound-scale
        Optional argument, switch between country names or the three letter name
          loc_mode="country names" or "ISO-3" '''
    timestamp = [datetime.datetime.fromtimestamp(data_list[1][2]).strftime('%d-%m-%Y (%H:%M)'), datetime.datetime.fromtimestamp(data_list[len(data_list)-1][2]).strftime('%d-%m-%Y (%H:%M)')]
    name = 'Data for <b>'+data_list[0]+'</b><br><span style="font-size:64%;"><i>'+str(len(data_list)-1)+' messages between '+timestamp[0]+' and '+timestamp[1]+'</i></span>'
    country = []
    compound = []
    nom = []  # number of messages
    # Merge messages from the same country
    for i in range(1, len(data_list)):
        duplicate = False
        for j in range(len(country)):
            if country[j] == data_list[i][3]:
                duplicate = True
                compound[j].append(data_list[i][1][0])
                break
        if not duplicate:
            country.append(data_list[i][3])
            compound.append([data_list[i][1][0]])
    # Calculate the average compound for each country
    for i in range(len(compound)):
        tmp = 0
        for j in range(len(compound[i])):
            tmp = tmp + compound[i][j]
        tmp = round(tmp/len(compound[i]), 3)
        nom.append("Messages: "+str(len(compound[i]))+"<br>Compound: "+str(tmp))
        compound[i] = tmp
    data = [dict(type='choropleth', locations=country, z=compound, text=nom, zmin=-1, zmax=1, marker=dict(line=dict(color='rgb(180,180,180)', width=0.5)), colorscale=[[0, color_neg], [0.5, color_neu], [1, color_pos]], colorbar=dict(title="Compound"), hoverinfo='text+location', locationmode=loc_mode)]
    layout = dict(title=name, geo=dict(showframe=False, showland=True, landcolor="rgb(192, 192, 192)", showcoastlines=True, projection=dict(type='Mercator')))
    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, validate=False, filename='Plots/sentiment-world.html')


def plot_pie(data_list, color_neg='rgb(149,28,28)', color_neu='rgb(166,118,42)', color_pos='rgb(128,192,50)', hot_one=False):
    ''' Returns an interactive line plot in the directory "Plots/"
        Takes as argument a list with:
          list[0] = name (str)
          list[1:] = all messages (list)
          list[1:][0] = message (str)
          list[1:][1] = sentiment (list)
          list[1:][1][0] = compound (float)
          list[1:][2] = timestamp (int)
        Optional arguments are the colors in the compound-scale
        Optional argument, switch between two types of classifications: hot_one=
          True: Only the highest value of negative, neutral, positive counts
          False: Takes the fractions of each negative, neutral, positive into account (default) '''
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

    data = Pie(labels=['Negative','Neutral','Positive'], values=scores, hoverinfo='label+percent', textinfo='percent', textfont=dict(size=20, color='rgb(24,24,24)'), marker=dict(colors=[color_neg, color_neu, color_pos], line=dict(color='#000000', width=2)))
    py.offline.plot(dict(data=[data], layout=dict(title=name)), filename='Plots/sentiment-pie.html')

# Example dataset
zinloos = ["#kerst", ["het is bijna #kerst", [0.3, 0.2, 0.5, 0.3], 1375432865, 'NLD'], ["Wat hou ik toch veel van #kerst", [0.5, 0.1, 0.3, 0.6], 1375433124, 'NLD'], ["heb zin in #kerst", [0.4, 0.1, 0.3, 0.6], 1375433865, 'DEU'], ["ik hou zooo veel van #kerst", [0.8, 0.1, 0.1, 0.8], 1375436864, 'ITA'], ["Wat praten we over #kerst in de zomer?", [0.2, 0.1, 0.7, 0.2], 1375458723, 'ITA'], ["Het is #kerst over 145 dagen!", [0.3, 0, 0.6, 0.4], 1375474832, 'FRA'], ["Wat heb ik een hekel aan #kerstmuziek", [-0.6, 0.6, 0.2, 0.2], 1375476592, 'GBR'], ["Zo blij! Ik hoef helemaal niet aan #kerstinkopen te denken", [0.5, 0.1, 0.2, 0.7], 1375476912, 'ITA']]
# Example plots
plot_line(zinloos)
plot_bar(zinloos)
plot_world(zinloos)
plot_pie(zinloos)
# Example to get free help
help(plot_pie)
