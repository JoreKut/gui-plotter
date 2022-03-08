import tkinter
from configuration.config import *
from component.plotter import Plot
from util.model.function import Function

class App(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg=PLOT_BG_COLOR)
        self.pack()

        top_area = tkinter.Frame(self, width=INPUT_WIDTH, height=PLOT_HEIGHT)
        input_area = tkinter.Frame(self, width=INPUT_WIDTH, height=INPUT_HEIGHT, bg='#333'
                                   , pady=20, padx=300)
        self.plot = Plot(top_area)
        self.info = tkinter.Frame(top_area, bg='#555', width=INFO_WIDTH, height=INFO_HEIGHT)
        self.entry = tkinter.Entry(input_area, width=30, font=FONT)
        self.btn = tkinter.Button(input_area, width=10, text="ADD", bg='#475', fg='white',
                                  command=self.plot_function_graph)

        top_area.pack()
        input_area.pack()
        self.plot.pack(side='left')
        self.info.pack(side='left')
        self.entry.pack(side='left')
        self.btn.pack(side='left')

    def plot_function_graph(self):
        print('-', self.entry.get())
