from tkinter import *
from plot_line import *
from plot_bar import *
from plot_world import *
from plot_pie import *
from plot_overview import *
from sort_for_graphing import open_json, open_json_for_hashtag
from importingtwitterdata_new import import_data, set_max_time

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
        self.input.grid(row = 2, column = 0, sticky = W)

        self.make_button = Button(self, text = "Collect data", command = self.collect_hts)
        self.make_button.grid(row = 3, column = 0, sticky = W)

        self.make_button = Button(self, text = "Plot popular tags", command = self.plot_popular)
        self.make_button.grid(row = 4, column = 0, sticky = W)


        self.instruction = Label(self, text = "===== DISPLAY DATA =====")
        self.instruction.grid(row = 0, column = 2, sticky = W)
        self.instruction = Label(self, text = "Enter hashtag to display: ")
        self.instruction.grid(row = 1, column = 2, columnspan = 2, sticky = W)
        self.input2 = Entry(self, width = 24)
        self.input2.grid(row = 2, column = 2, sticky = W)
        self.make_button = Button(self, text = "Plot Line graph", command = self.execute_a)
        self.make_button.grid(row = 3, column = 2, sticky = W)
        self.make_button = Button(self, text = "Plot Bar-chart", command = self.execute_b)
        self.make_button.grid(row = 4, column = 2, sticky = W)
        self.make_button = Button(self, text = "Plot Pie-chart", command = self.execute_c)
        self.make_button.grid(row = 5, column = 2, sticky = W)
        self.make_button = Button(self, text = "Plot World-map", command = self.execute_d)
        self.make_button.grid(row = 6, column = 2, sticky = W)

        self.instruction = Label(self, text = "===== DISPLAY OPTIONS =====")
        self.instruction.grid(row = 0, column = 3, columnspan = 2, sticky = W)
        self.hopie = BooleanVar()
        self.add_settings = Label(self, text = "Pie-chart hot-one mode: ")
        self.add_settings.grid(row = 1, column = 3, columnspan = 2, sticky = W)
        Radiobutton(self, text = "Enable", value = True, variable = self.hopie).grid(row = 2, column = 3, sticky = W)
        Radiobutton(self, text = "Disable", value = False, variable = self.hopie).grid(row = 3, column = 3, sticky = W)

        self.instruction = Label(self, text = "===== STATUS =====")
        self.instruction.grid(row = 9, column = 0, columnspan = 5, sticky = W)

        self.text = Text(self, width = 74, height = 12, wrap = WORD)
        self.text.grid(row = 10, column = 0, columnspan = 5, sticky = W)


        self.text.insert(0.0, str(self.mes_count) + "\tReady\n\tCollect first the data")
        self.mes_count = self.mes_count + 1

    def collect_hts(self):
        try:
            time = int(self.input.get())
        except ValueError:
            time = 0
            self.text.insert(0.0, str(self.mes_count) + "\tPlease enter a integer value\n")
            self.mes_count = self.mes_count + 1
        message = str(self.mes_count) + "\tCollecting data (" + str(time) + "s)\n"
        self.text.insert(0.0, message)
        self.mes_count = self.mes_count + 1
        max_time = set_max_time(time)
        data = import_data()
        self.text.insert(0.0, str(self.mes_count) + "\tData imported\n")
        self.mes_count = self.mes_count + 1

    def plot_popular(self):
        message = str(self.mes_count) + "\tPlotting overview of most common tags\n"
        self.text.insert(0.0, message)
        self.mes_count = self.mes_count + 1
        all_hashtags = open_json_for_hashtag("twitterdata.json")
        sorted_all_hashtags = self.sort_hash(all_hashtags, 1)
        plot_hbar(sorted_all_hashtags[0:16])

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
        self.select_ht()
        if len(self.datastorage) > 1:
            return True
        return False

    def sort_hash(self, data, col):
        new_data = []
        new_data.extend(sorted(data[0:], key=lambda data: -data[col]))
        return new_data

    def select_ht(self):
        hashtag = ["#" + self.input2.get()]
        self.datastorage = open_json("twitterdata.json", hashtag)


root = Tk()
root.title("Give the little animal a name")
root.geometry("640x360")

app = Application(root)

root.mainloop()