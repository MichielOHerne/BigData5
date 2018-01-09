from tkinter import *
from plot_line import *
from plot_bar import *
from plot_world import *
from plot_pie import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.mes_count = 0
        self.datastorage = list()

        self.instruction = Label(self, text = "===== COLLECTING DATA =====")
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.instruction = Label(self, text = "Seconds to stream: ")
        self.instruction.grid(row = 1, column = 0, columnspan = 2, sticky = W)

        self.input = Entry(self, width = 10)
        self.input.grid(row = 1, column = 1, sticky = W)

        self.make_button = Button(self, text = "Collect data", command = self.collect_hts)
        self.make_button.grid(row = 3, column = 0, sticky = W)


        self.instruction = Label(self, text = "===== DISPLAY DATA =====")
        self.instruction.grid(row = 0, column = 2, sticky = W)
        self.make_button = Button(self, text = "Plot Line graph", command = self.execute_a)
        self.make_button.grid(row = 1, column = 2, sticky = W)
        self.make_button = Button(self, text = "Plot Bar-chart", command = self.execute_b)
        self.make_button.grid(row = 2, column = 2, sticky = W)
        self.make_button = Button(self, text = "Plot Pie-chart", command = self.execute_c)
        self.make_button.grid(row = 3, column = 2, sticky = W)
        self.make_button = Button(self, text = "Plot World-map", command = self.execute_d)
        self.make_button.grid(row = 4, column = 2, sticky = W)

        self.instruction = Label(self, text = "===== DISPLAY OPTIONS =====")
        self.instruction.grid(row = 0, column = 3, columnspan = 2, sticky = W)
        self.hopie = BooleanVar()
        self.add_settings = Label(self, text = "Pie-chart hot-one mode: ")
        self.add_settings.grid(row = 1, column = 3, columnspan = 2, sticky = W)
        Radiobutton(self, text = "Enable", value = True, variable = self.hopie).grid(row = 2, column = 3, sticky = W)
        Radiobutton(self, text = "Disable", value = False, variable = self.hopie).grid(row = 3, column = 3, sticky = W)

        self.instruction = Label(self, text = "===== STATUS =====")
        self.instruction.grid(row = 5, column = 0, columnspan = 5, sticky = W)

        self.text = Text(self, width = 74, height = 12, wrap = WORD)
        self.text.grid(row = 6, column = 0, columnspan = 5, sticky = W)


        self.text.insert(0.0, str(self.mes_count) + "\tReady\n\tCollect first the data")
        self.mes_count = self.mes_count + 1

    def collect_hts(self):
        time = int(self.input.get())
        message = str(self.mes_count) + "\tCollecting data (" + str(time) + "s)\n"
        self.text.insert(0.0, message)
        self.mes_count = self.mes_count + 1
        self.datastorage = ["#kerst", ["het is bijna #kerst", [0.3, 0.2, 0.5, 0.3], 1375432865, 'NLD'], ["Wat hou ik toch veel van #kerst", [0.5, 0.1, 0.3, 0.6], 1375433124, 'NLD'], ["heb zin in #kerst", [0.4, 0.1, 0.3, 0.6], 1375433865, 'DEU'], ["ik hou zooo veel van #kerst", [0.8, 0.1, 0.1, 0.8], 1375436864, 'ITA'], ["Wat praten we over #kerst in de zomer?", [0.2, 0.1, 0.7, 0.2], 1375458723, 'ITA'], ["Het is #kerst over 145 dagen!", [0.3, 0, 0.6, 0.4], 1375474832, 'FRA'], ["Wat heb ik een hekel aan #kerstmuziek", [-0.6, 0.6, 0.2, 0.2], 1375476592, 'GBR'], ["Zo blij! Ik hoef helemaal niet aan #kerstinkopen te denken", [0.5, 0.1, 0.2, 0.7], 1375476912, 'ITA']]
        self.text.insert(0.0, str(self.mes_count) + "\tData imported\n")
        self.mes_count = self.mes_count + 1
        

    def execute_a(self):
        if self.checkdata():
            message = str(self.mes_count) + "\tPlotting Line graph\n"
            self.text.insert(0.0, message)
            self.mes_count = self.mes_count + 1
            plot_line(self.datastorage)
            self.text.insert(0.0, str(self.mes_count) + "\tDone. Ready\n")
            self.mes_count = self.mes_count + 1
        else:
            self.text.insert(0.0, str(self.mes_count) + "\tNo data available. Failed\n")
            self.mes_count = self.mes_count + 1

    def execute_b(self):
        if self.checkdata():
            message = str(self.mes_count) + "\tPlotting Bar-chart\n"
            self.text.insert(0.0, message)
            self.mes_count = self.mes_count + 1
            plot_bar(self.datastorage)
            self.text.insert(0.0, str(self.mes_count) + "\tDone. Ready\n")
            self.mes_count = self.mes_count + 1
        else:
            self.text.insert(0.0, str(self.mes_count) + "\tNo data available. Failed\n")
            self.mes_count = self.mes_count + 1

    def execute_c(self):
        if self.checkdata():
            message = str(self.mes_count) + "\tPlotting Pie-chart\n"
            self.text.insert(0.0, message)
            self.mes_count = self.mes_count + 1
            plot_pie(self.datastorage, hot_one=self.hopie.get())
            self.text.insert(0.0, str(self.mes_count) + "\tDone. Ready\n")
            self.mes_count = self.mes_count + 1
        else:
            self.text.insert(0.0, str(self.mes_count) + "\tNo data available. Failed\n")
            self.mes_count = self.mes_count + 1

    def execute_d(self):
        if self.checkdata():
            message = str(self.mes_count) + "\tPlotting World-map\n"
            self.text.insert(0.0, message)
            self.mes_count = self.mes_count + 1
            plot_world(self.datastorage)
            self.text.insert(0.0, str(self.mes_count) + "\tDone. Ready\n")
            self.mes_count = self.mes_count + 1
        else:
            self.text.insert(0.0, str(self.mes_count) + "\tNo data available. Failed\n")
            self.mes_count = self.mes_count + 1

    def checkdata(self):
        if len(self.datastorage) > 1:
            return True
        return False

root = Tk()
root.title("Give the little animal a name")
root.geometry("640x360")

app = Application(root)

root.mainloop()
