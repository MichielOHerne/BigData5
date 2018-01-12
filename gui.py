from tkinter import *
from plot_line import *
from plot_bar import *
from plot_world import *
from plot_pie import *
from plot_overview import *
from main import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.mes_count = 0
        self.datastorage = list()
        self.sorted_all_hashtags = list()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text=" ")  # Space
        self.instruction.grid(row=0, column=0, columnspan=1, sticky=W)

        self.instruction = Label(self, text=" ===== COLLECTING DATA =====    ")
        self.instruction.grid(row=0, column=1, columnspan=1, sticky=W)
        self.instruction = Label(self, text="Seconds to stream: ")
        self.instruction.grid(row=1, column=1, columnspan=1, sticky=W)
        self.input = Entry(self, width=10)
        self.input.grid(row=2, column=1, sticky=W)

        self.make_button = Button(self, text="Collect data", command=self.collect_hts, width=14)
        self.make_button.grid(row=3, column=1, sticky=W)

        self.make_button = Button(self, text="Plot popular tags", command=self.plot_popular, width=14)
        self.make_button.grid(row=4, column=1, sticky=W)

        self.make_button = Button(self, text="Print popular tags", command=self.print_popular, width=14)
        self.make_button.grid(row=5, column=1, sticky=W)

        self.instruction = Label(self, text=" ===== DISPLAY DATA =====   ")
        self.instruction.grid(row=0, column=3, sticky=W)
        self.instruction = Label(self, text="Enter hashtag to display: ")
        self.instruction.grid(row=1, column=3, columnspan=1, sticky=W)
        self.input2 = Entry(self, width=24)
        self.input2.grid(row=2, column=3, sticky=W)
        self.make_button = Button(self, text="Plot Line graph", command=self.execute_a, width=12)
        self.make_button.grid(row=3, column=3, sticky=W)
        self.make_button = Button(self, text="Plot Bar chart", command=self.execute_b, width=12)
        self.make_button.grid(row=4, column=3, sticky=W)
        self.make_button = Button(self, text="Plot Pie chart", command=self.execute_c, width=12)
        self.make_button.grid(row=5, column=3, sticky=W)
        self.make_button = Button(self, text="Plot World map", command=self.execute_d, width=12)
        self.make_button.grid(row=6, column=3, sticky=W)

        self.instruction = Label(self, text=" ===== DISPLAY OPTIONS ===== ")
        self.instruction.grid(row=0, column=2, sticky=W)
        self.hopie = StringVar()
        self.hopie.set("norm")
        self.mal = StringVar()
        self.mal.set("hour")
        self.add_settings = Label(self, text="Line graph moving average:")
        self.add_settings.grid(row=1, column=2, sticky=W)
        Radiobutton(self, text="Minute", value="minute", variable=self.mal).grid(row=2, column=2, sticky=W)
        Radiobutton(self, text="Hour", value="hour", variable=self.mal).grid(row=3, column=2, sticky=W)
        self.add_settings = Label(self, text="Pie chart mode:")
        self.add_settings.grid(row=4, column=2, sticky=W)
        Radiobutton(self, text="Normal", value="norm", variable=self.hopie).grid(row=5, column=2, sticky=W)
        Radiobutton(self, text="Hot one", value="ho", variable=self.hopie).grid(row=6, column=2, sticky=W)
        Radiobutton(self, text="Hot one (ignore neutral)", value="hoin", variable=self.hopie).grid(row=7, column=2, sticky=W)

        self.instruction = Label(self, text=" ========   STATUS   ======== ")
        self.instruction.grid(row=9, column=1, columnspan=4, sticky=W)
        self.text = Text(self, width=74, height=12, wrap=WORD)
        self.text.grid(row=10, column=1, columnspan=5, sticky=W)
        self.instruction = Label(self, text="\t\t\t        Tim Al, Michiel O'Herne, Casper Spronk")
        self.instruction.grid(row=11, column=2, columnspan=2, sticky=W)

        self.text.insert(0.0, str(self.mes_count) + "\tReady\n\tCollect first the data")
        self.mes_count = self.mes_count + 1

    def collect_hts(self):
        try:
            time = int(self.input.get())
            if time < 0:
                raise ValueError
            message = str(self.mes_count) + "\tCollecting data (" + str(time) + "s)\n"
            self.text.insert(0.0, message)
            self.mes_count = self.mes_count + 1
            data = import_time(time)
            self.text.insert(0.0, str(self.mes_count) + "\tData imported. Ready\n")
            self.mes_count = self.mes_count + 1
            self.sorted_all_hashtags = sort_hashtags("twitterdata.json")
            if len(self.sorted_all_hashtags) == 0:
                self.text.insert(0.0, str(self.mes_count) + "\tNothing received. Please try again\n")
            else:
                counter = 0
                for item in self.sorted_all_hashtags:
                    counter = counter + len(item[0])
                self.text.insert(0.0, str(self.mes_count) + "\tReceived " + str(counter) + " messages\n")
            self.mes_count = self.mes_count + 1
            self.input2.delete(0, END)
            self.input2.insert(0, str(self.sorted_all_hashtags[0][0]))
        except ValueError:
            self.text.insert(0.0, str(self.mes_count) + "\tPlease enter a positive integer\n")
            self.mes_count = self.mes_count + 1
            self.input.delete(0, END)

    def plot_popular(self):
        message = str(self.mes_count) + "\tPlotting overview of most common tags\n"
        self.text.insert(0.0, message)
        self.mes_count = self.mes_count + 1
        plot_hbar(self.sorted_all_hashtags[0:16])

    def print_popular(self):
        message = str(self.mes_count) + "\tPrinting the five most common tags\n"
        for i in range(0, min(5, len(self.sorted_all_hashtags)-1)):
            message = message + ("\t(" + str(self.sorted_all_hashtags[i][1]) + ")\t" + self.sorted_all_hashtags[i][0] + "\n")
        self.text.insert(0.0, message)
        self.mes_count = self.mes_count + 1

    def execute_a(self):
        if self.checkdata():
            message = str(self.mes_count) + "\tPlotting Line graph\n"
            self.text.insert(0.0, message)
            self.mes_count = self.mes_count + 1
            plot_line(self.datastorage, mai=self.mal.get())
            print(self.mal)
            self.text.insert(0.0, str(self.mes_count) + "\tDone. Ready\n")
            self.mes_count = self.mes_count + 1
        else:
            self.text.insert(0.0, str(self.mes_count) + "\tNo data available. Failed\n")
            self.mes_count = self.mes_count + 1

    def execute_b(self):
        if self.checkdata():
            message = str(self.mes_count) + "\tPlotting Bar chart\n"
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
            message = str(self.mes_count) + "\tPlotting Pie chart\n"
            self.text.insert(0.0, message)
            self.mes_count = self.mes_count + 1
            plot_pie(self.datastorage, mode=self.hopie.get())
            self.text.insert(0.0, str(self.mes_count) + "\tDone. Ready\n")
            self.mes_count = self.mes_count + 1
        else:
            self.text.insert(0.0, str(self.mes_count) + "\tNo data available. Failed\n")
            self.mes_count = self.mes_count + 1

    def execute_d(self):
        if self.checkdata():
            message = str(self.mes_count) + "\tPlotting World map\n"
            self.text.insert(0.0, message)
            self.mes_count = self.mes_count + 1
            plot_world(self.datastorage, "country names")
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
        self.datastorage = []
        hashtag = ["#" + self.input2.get()]
        self.datastorage = filter_hashtags(hashtag)

create_dirs()
root = Tk()
root.title("Give the little animal a name")
root.geometry("616x432")

app = Application(root)

root.mainloop()
