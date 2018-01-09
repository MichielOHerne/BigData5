# Make sure that the directory "Plots/" exist to store all the plots!

from plot_line import *
from plot_bar import *
from plot_world import *
from plot_pie import *
from plot_overview import *

# Example dataset
zinloos = ["#kerst", ["het is bijna #kerst", [0.3, 0.2, 0.5, 0.3], 1375432865, 'NLD'], ["Wat hou ik toch veel van #kerst", [0.5, 0.1, 0.3, 0.6], 1375433124, 'NLD'], ["heb zin in #kerst", [0.4, 0.1, 0.3, 0.6], 1375433865, 'DEU'], ["ik hou zooo veel van #kerst", [0.8, 0.1, 0.1, 0.8], 1375436864, 'ITA'], ["Wat praten we over #kerst in de zomer?", [0.2, 0.1, 0.7, 0.2], 1375458723, 'ITA'], ["Het is #kerst over 145 dagen!", [0.3, 0, 0.6, 0.4], 1375474832, 'FRA'], ["Wat heb ik een hekel aan #kerstmuziek", [-0.6, 0.6, 0.2, 0.2], 1375476592, 'GBR'], ["Zo blij! Ik hoef helemaal niet aan #kerstinkopen te denken", [0.5, 0.1, 0.2, 0.7], 1375476912, 'ITA']]
onzinnig = [["Henk", 12], ["Inge", 10], ["Klaas", 10], ["Joop", 9], ["Piet", 7], ["Edwin", 5], ["Rick", 5], ["Niels", 4], ["Frank", 3], ["Jelte", 2], ["Albert", 1]]
# Example plots
plot_hbar(onzinnig)
plot_line(zinloos)
plot_bar(zinloos)
plot_world(zinloos)
plot_pie(zinloos)
# Example to get free help
help(plot_world)
