import random
import tkinter
from configs.config import *


class Plot(tkinter.Canvas):
    def __init__(self, master=None):
        super(Plot, self).__init__(master, width=MIN_WINDOW_WIDTH, height=MIN_WINDOW_HEIGHT, bg=PLOT_BG_COLOR)
        self.bind('<Button-1>', self.make_circle)

    def add(self, function: str):
        pass

    def remove(self, function_index: int):
        pass

    def zoom(self, scale: float):
        pass

    def move(self, dx, dy):
        pass

    def make_circle(self, event):
        x = random.randint(10, 400)
        y = random.randint(10, 400)
        self.create_oval(x, y, x + 30, y + 30, fill='red')
