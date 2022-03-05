import tkinter
import settings


class Plot(tkinter.Canvas):
    def __init__(self, master=None):
        super(Plot, self).__init__(master, width=700, height=420, bg=settings.PLOT_BG_COLOR)

    def c(self):
        self.create_line(10, 10, 60, 70, fill='red')
