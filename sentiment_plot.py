# Zorg dat de map "Plots/" aanwezig is om alles in op te slaan!
import plotly as py
from plotly.graph_objs import *
import datetime

def plot_line(data_list):
    ''' Returns an interactive line plot in the directory Plots/
        Takes as argument one list with at least:
          list[0] = name (str)
          list[1:] = all messages (list)
          list[1:][0] = message (str)
          list[1:][1] = sentiment (list)
          list[1:][1][0] = compound (float)
          list[1:][2] = timestamp (int)'''
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
    ''' Returns an interactive line plot in the directory Plots/
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
        Optional arguments are the colors of the different bars, example:
          color_neg="rgb(149,28,28)" '''
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

def plot_world(data_list, color_neg='rgb(149,28,28)', color_neu='rgb(166,118,42)', color_pos='rgb(154,206,50)'):
    ''' Returns an interactive line plot in the directory Plots/
        Takes as argument a list with:
          list[0] = name (str)
          list[1:] = all messages (list)
          list[1:][0] = message (str)
          list[1:][1] = sentiment (list)
          list[1:][1][0] = compound (float)
          list[1:][2] = timestamp (int)
          list[1:][3] = country_code (str)
        Optional arguments are the colors in the compound-scale, example:
          color_neg="rgb(149,28,28)" '''
    print("ALFA FASE - FUNCTIE NIET AANROEPEN")
    name = data_list[0]
    country_list = [["AFG", 0], ["ALB", 0], ["DZA", 0], ["ASM", 0], ["AND", 0], ["AGO", 0], ["AIA", 0], ["ATG", 0], ["ARG", 0], ["ARM", 0],["ABW", 0], ["AUS", 0], ["AUT", 0], ["AZE", 0], ["BHM", 0], ["BHR", 0], ["BGD", 0], ["BRB", 0], ["BLR", 0], ["BEL" , 0], ["BLZ", 0], ["BEN", 0], ["BMU", 0], ["BTN", 0], ["BOL", 0], ["BIH", 0], ["BWA", 0], ["BRA", 0], ["VGB", 0],["BRN", 0], ["BGR", 0], ["BFA", 0], ["MMR", 0], ["BDI", 0], ["CPV", 0], ["KHM", 0], ["CMR", 0], ["CAN", 0], ["CYM", 0], ["CAF", 0], ["TCD", 0], ["CHL", 0], ["CHN", 0], ["COL", 0], ["COM", 0], ["COD", 0], ["COG", 0], ["COK", 0],["CRI", 0], ["CIV", 0], ["HRV", 0], ["CUB", 0], ["CUW", 0], ["CYP", 0], ["CZE", 0], ["DNK", 0], ["DJI", 0], ["DMA", 0], ["DOM", 0], ["ECU", 0], ["EGY", 0], ["SLV", 0], ["GNQ", 0], ["ERI", 0], ["EST", 0], ["ETH", 0], ["FLK", 0],["FRO", 0], ["FJI", 0], ["FIN", 0], ["FRA", 0], ["PYF", 0], ["GAB", 0], ["GMB", 0], ["GEO", 0], ["DEU", 0], ["GHA", 0], ["GIB", 0], ["GRC", 0], ["GRL", 0], ["GRD", 0], ["GUM", 0], ["GTM", 0], ["GGY", 0], ["GNB", 0], ["GIN", 0],["GUY", 0], ["HTI", 0], ["HND", 0], ["HKG", 0], ["HUN", 0], ["ISL", 0], ["IND", 0], ["IDN", 0], ["IRN", 0], ["IRQ", 0], ["IRL", 0], ["IMN", 0], ["ISR", 0], ["ITA", 0], ["JAM", 0], ["JPN", 0], ["JEY", 0], ["JOR", 0], ["KAZ", 0],["KEN", 0], ["KIR", 0], ["PRK", 0], ["KOR", 0], ["KSV", 0], ["KWT", 0], ["KGZ", 0], ["LAO", 0], ["LVA", 0], ["LBN", 0], ["LSO", 0], ["LBR", 0], ["LBY", 0], ["LIE", 0], ["LTU", 0], ["LUX", 0], ["MAC", 0], ["MKD", 0], ["MDG", 0],["MWI", 0], ["MYS", 0], ["MDV", 0], ["MLI", 0], ["MLT", 0], ["MHL", 0], ["MRT", 0], ["MUS", 0], ["MEX", 0], ["FSM", 0], ["MDA", 0], ["MCO", 0], ["MNG", 0], ["MNE", 0], ["MAR", 0], ["MOZ", 0], ["NAM", 0], ["NPL", 0], ["NLD", 0],["NCL", 0], ["NZL", 0], ["NIC", 0], ["NGA", 0], ["NER", 0], ["NIU", 0], ["MNP", 0], ["NOR", 0], ["OMN", 0], ["PAK", 0], ["PLW", 0], ["PAN", 0], ["PNG", 0], ["PRY", 0], ["PER", 0], ["PHL", 0], ["POL", 0], ["PRT", 0], ["PRI", 0],["QAT", 0], ["ROU", 0], ["RUS", 0], ["RWA", 0], ["KNA", 0], ["LCA", 0], ["MAF", 0], ["SPM", 0], ["VCT", 0], ["WSM", 0], ["SMR", 0], ["STP", 0], ["SAU", 0], ["SEN", 0], ["SRB", 0], ["SYC", 0], ["SLE", 0], ["SGP", 0], ["SXM", 0],["SVK", 0], ["SVN", 0], ["SLB", 0], ["SOM", 0], ["ZAF", 0], ["SSD", 0], ["ESP", 0], ["LKA", 0], ["SDN", 0], ["SUR", 0], ["SWZ", 0], ["SWE", 0], ["CHE", 0], ["SYR", 0], ["TWN", 0], ["TJK", 0], ["TZA", 0], ["THA", 0], ["TLS", 0], ["TGO", 0], ["TON", 0], ["TTO", 0], ["TUN", 0], ["TUR", 0], ["TKM", 0], ["TUV", 0], ["UGA", 0], ["UKR", 0], ["ARE", 0], ["GBR", 0], ["USA", 0], ["URY", 0], ["UZB", 0], ["VUT", 0], ["VEN", 0], ["VNM", 0], ["WBG", 0], ["YEM", 0], ["ZMB", 0], ["ZWE", 0]]
    index = {"AFG": 0, "ALB": 1, "DZA": 2, "ASM": 3, "AND": 4, "AGO": 5, "AIA": 6, "ATG": 7, "ARG": 8, "ARM": 9, "ABW": 10, "AUS": 11, "AUT": 12, "AZE": 13, "BHM": 14, "BHR": 15, "BGD": 16, "BRB": 17, "BLR": 18, "BEL": 19, "BLZ": 20, "BEN": 21, "BMU": 22, "BTN": 23, "BOL": 24, "BIH": 25, "BWA": 26, "BRA": 27, "VGB": 28, "BRN": 29, "BGR": 30, "BFA": 31, "MMR": 32, "BDI": 33, "CPV": 34, "KHM": 35, "CMR": 36, "CAN": 37, "CYM": 38, "CAF": 39, "TCD": 40, "CHL": 41, "CHN": 42, "COL": 43, "COM": 44, "COD": 45, "COG": 46, "COK": 47, "CRI": 48, "CIV": 49, "HRV": 50, "CUB": 51, "CUW": 52, "CYP": 53, "CZE": 54, "DNK": 55, "DJI": 56, "DMA": 57, "DOM": 58, "ECU": 59, "EGY": 60, "SLV": 61, "GNQ": 62, "ERI": 63, "EST": 64, "ETH": 65, "FLK": 66, "FRO": 67, "FJI": 68, "FIN": 69, "FRA": 70, "PYF": 71, "GAB": 72, "GMB": 73, "GEO": 74, "DEU": 75, "GHA": 76, "GIB": 77, "GRC": 78, "GRL": 79, "GRD": 80, "GUM": 81, "GTM": 82, "GGY": 83, "GNB": 84, "GIN": 85, "GUY": 86, "HTI": 87, "HND": 88, "HKG": 89, "HUN": 90, "ISL": 91, "IND": 92, "IDN": 93, "IRN": 94, "IRQ": 95, "IRL": 96, "IMN": 97, "ISR": 98, "ITA": 99, "JAM": 100, "JPN": 101, "JEY": 102, "JOR": 103, "KAZ": 104, "KEN": 105, "KIR": 106, "PRK": 107, "KOR": 108, "KSV": 109, "KWT": 110, "KGZ": 111, "LAO": 112, "LVA": 113, "LBN": 114, "LSO": 115, "LBR": 116, "LBY": 117, "LIE": 118, "LTU": 119, "LUX": 120, "MAC": 121, "MKD": 122, "MDG": 123, "MWI": 124, "MYS": 125, "MDV": 126, "MLI": 127, "MLT": 128, "MHL": 129, "MRT": 130, "MUS": 131, "MEX": 132, "FSM": 133, "MDA": 134, "MCO": 135, "MNG": 136, "MNE": 137, "MAR": 138, "MOZ": 139, "NAM": 140, "NPL": 141, "NLD": 142, "NCL": 143, "NZL": 144, "NIC": 145, "NGA": 146, "NER": 147, "NIU": 148, "MNP": 149, "NOR": 150, "OMN": 151, "PAK": 152, "PLW": 153, "PAN": 154, "PNG": 155, "RY": 156, "PER": 157, "PHL": 158, "POL": 159, "PRT": 160, "PRI": 161, "QAT": 162, "ROU": 163, "RUS": 164, "RWA": 165, "KNA": 166, "LCA": 167, "MAF": 168, "SPM": 169, "VCT": 170, "WSM": 171, "SMR": 172, "STP": 173, "SAU": 174, "SEN": 175, "SRB": 176, "SYC": 177, "SLE": 178, "SGP": 179, "SXM": 180, "SVK": 181, "SVN": 182, "SLB": 183, "SOM": 184, "ZAF": 185, "SSD": 186, "ESP": 187, "LKA": 188, "SDN": 189, "SUR": 190, "SWZ": 191, "SWE": 192, "CHE": 193, "SYR": 194, "TWN": 195, "TJK": 196, "TZA": 197, "THA": 198, "TLS": 199, "TGO": 200, "TON": 201, "TTO": 202, "TUN": 203, "TUR": 204, "TKM": 205, "TUV": 206, "UGA": 207, "UKR": 208, "ARE": 209, "GBR": 210, "USA": 211, "URY": 212, "UZB": 213, "VUT": 214, "VEN": 215, "VNM": 216, "WBG": 217, "YEM": 289, "ZMB": 219, "ZWE": 220}

    for i in range(1, len(data_list)):
        country_list[index[data_list[i][3]]][1] = data_list[i][1][0]

    data = [ dict(
            type = 'choropleth',
            locations = [row[0] for row in country_list],
            z = [row[1] for row in country_list],
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) )
          ) ]
    
    layout = dict(geo = dict(showframe = False, showcoastlines = True, projection = dict( type = 'Mercator')))

    fig = dict( data=data, layout=layout )
    py.offline.plot(fig, validate=False, filename='Plots/sentiment-world.html')

zinloos = ["#kerst", ["het is bijna #kerst", [0.3, 0.2, 0.5, 0.3], 1375432865, 'NLD'], ["heb zin in #kerst", [0.4, 0.1, 0.5, 0.4], 1375433865, 'DEU'], ["ik hou zooo veel van #kerst", [0.8, 0.1, 0.2, 0.7], 1375436864, 'USA'], ["Wat praten we over #kerst in de zomer?", [0.2, 0.1, 0.7, 0.2], 1375458723, 'CHN'], ["Het is #kerst over 145 dagen!", [0.3, 0, 0.6, 0.4], 1375474832, 'FRA'], ["Wat heb ik een hekel aan #kerstmuziek", [-0.6, 0.6, 0.2, 0.2], 1375476592, 'GBR'], ["Zo blij! Ik hoef helemaal niet aan #kerstinkopen te denken", [0.5, 0.1, 0.2, 0.7], 1375476912, 'ITA']]
#plot_line(zinloos)
#plot_bar(zinloos)
plot_world(zinloos)
