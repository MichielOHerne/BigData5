import plotly as py
import datetime

def plot_world(data_list, loc_mode="ISO-3"):
    ''' Returns an interactive world map with the data in the directory "Plots/"
        Takes as argument a list with:
          list[0] = name (str)
          list[1:] = all messages (list)
          list[1:][0] = message (str)
          list[1:][1] = sentiment (list)
          list[1:][1][0] = compound (float)
          list[1:][2] = timestamp (int)
          list[1:][3] = country_code (str) -> No error message when incorrect!
        Optional argument, switch between country names or the three letter name
          loc_mode="country names" or "ISO-3" '''
    colors = ['rgb(149,28,28)', 'rgb(166,118,42)', 'rgb(128,192,50)']
    colors2 = ['rgb(192,248,248)', 'rgb(12,152,152)']
    timestamp = [datetime.datetime.fromtimestamp(data_list[1][2]).strftime('%d-%m-%Y (%H:%M)'), datetime.datetime.fromtimestamp(data_list[len(data_list)-1][2]).strftime('%d-%m-%Y (%H:%M)')]
    name = 'Data for <b>'+data_list[0]+'</b><br><span style="font-size:64%;"><i>'+str(len(data_list)-1)+' messages between '+timestamp[0]+' and '+timestamp[1]+'</i></span>'
    country = []
    compound = []
    nom = []  # number of messages
    info = []
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
        info.append("Messages: "+str(len(compound[i]))+"<br>Compound: "+str(tmp))
        nom.append(len(compound[i]))
        compound[i] = tmp
    # Different data
    data_c = dict(type='choropleth', locations=country, z=compound, text=info, zmin=-1, zmax=1, marker=dict(line=dict(color='rgb(180,180,180)', width=0.5)), colorscale=[[0, colors[0]], [0.5, colors[1]], [1, colors[2]]], colorbar=dict(title="Compound"), hoverinfo='text+location', locationmode=loc_mode)
    data_a = dict(type='choropleth', locations=country, z=nom, text=info, zmin=0, marker=dict(line=dict(color='rgb(180,180,180)', width=0.5)), colorscale=[[0, colors2[0]], [1, colors2[1]]], colorbar=dict(title="Occurrence"), hoverinfo='text+location', locationmode=loc_mode)
    data = [data_c, data_a]
    choose_data = list([dict(active=-1, buttons=list([dict(label='Sentiment', method='update', args=[{'visible': [True, False]}]), dict(label='Occurrence', method='update', args=[{'visible': [False, True]}])]))])
    # Plot
    layout = dict(title=name, geo=dict(showframe=False, showland=True, landcolor="rgb(192, 192, 192)", showcoastlines=True, projection=dict(type='Mercator')), updatemenus=choose_data)
    fig = dict(data=data, layout=layout)
    py.offline.plot(fig, validate=False, filename='Plots/sentiment-world.html')
