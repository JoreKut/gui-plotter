import tkinter
from configuration.config import *
from util.model.point import Point
from util.model.function import Function
from util.model.reference_system import ReferenceSystem
from util.model.vector import Vector


class Plot(tkinter.Canvas):
    def __init__(self, master=None):
        super(Plot, self).__init__(master, width=PLOT_WIDTH, height=PLOT_HEIGHT, bg=PLOT_BG_COLOR)
        self.functions = []
        self.center = Vector(x=0 / 2, y=0 / 2)
        self.create_oval(self.center.x, self.center.y, self.center.x, self.center.y)
        self.config(bg='#343')
        self.draw_grid()

        self.external_system = ReferenceSystem(Vector(1, 0), Vector(0, -1))
        self.internal_system = ReferenceSystem(Vector(1, 0), Vector(0, -1), self.center)
        self.external_system.add_child(self.internal_system)

        f = Function("x")
        self.draw_function(f)

    def add(self, function: str):
        pass

    def remove(self, function_index: int):
        pass

    def zoom(self, scale: float):
        pass

    def move(self, dx, dy):
        self.center.move(dx, dy)

    def external_into_internal(self, x_e, y_e) -> (float, float):
        pass

    def draw_function(self, function: Function):

        for x1 in range(PLOT_WIDTH):
            v_ex = Vector(x1, 0)
            v_in = self.internal_system.transfer_from_root(v_ex)
            y_ex = function.value_at(v_in.x)
            v_ex.y = y_ex
            self.create_oval(v_ex.x-2, v_ex.y-2, v_ex.x+2, v_ex.y+2, fill='red')


    def draw_grid(self):
        for i in range(0, PLOT_WIDTH, int(PLOT_WIDTH / 10)):
            self.create_line(i, 0, i, PLOT_HEIGHT)
        for i in range(0, PLOT_WIDTH, int(PLOT_HEIGHT / 10)):
            self.create_line(0, i, PLOT_WIDTH, i)
