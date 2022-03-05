import tkinter
from plotter import Plot


class App(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.graph = Plot(self)
        self.graph.pack(padx=10, pady=10, side='top')
        self.master.minsize(600, 400)
        self.pack()
        self.addInputField()

    def addInputField(self):

        input_zone = tkinter.Frame(self)
        input_zone.pack(padx=10, pady=30, side='bottom')

        self.entry = tkinter.Entry(input_zone, width=50)
        self.entry.pack(side='left')

        self.btn = tkinter.Button(input_zone, width=10, text="ADD", bg='green', fg='white', border=None)
        self.btn.pack(side='left', padx=10)
