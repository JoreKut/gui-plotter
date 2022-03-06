import tkinter
from settings import *
from plotter import Plot


class App(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=PLOT_BG_COLOR)
        self.pack()

        self.plot = Plot(self)
        self.plot.pack(side='top')

        input_area = tkinter.Frame(self, bg=PLOT_BG_COLOR)
        input_area.pack(side='bottom', pady=25)

        self.entry = tkinter.Entry(input_area, width=30, font=FONT)
        self.entry.pack(side='left')

        self.btn = tkinter.Button(input_area, width=10, text="ADD", bg='green', fg='white', command=self.plot_function_graph)
        self.btn.pack(side='left')

    def plot_function_graph(self):
        print('-', self.entry.get())

