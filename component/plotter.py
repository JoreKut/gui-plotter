import tkinter
from configuration.config import *
from util.model.function import Function
from util.model.vector import Vector

class Plot(tkinter.Canvas):
    def __init__(self, master=None):
        super(Plot, self).__init__(master, width=PLOT_WIDTH, height=PLOT_HEIGHT, bg=PLOT_BG_COLOR)
        self.functions = []
        self.center = Vector(x=PLOT_WIDTH / 2, y=PLOT_HEIGHT / 2)
        self.create_oval(self.center.x, self.center.y, self.center.x, self.center.y, fill='red')
        self.config(bg='#222')
        self.draw_grid()

        self.i_vec = 50
        self.j_vec = 50

        self.i_scale = 1
        self.j_scale = 1

        self.show()

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

    def draw_function(self, f: Function):

        for xi in range(0, PLOT_WIDTH, 2):
            k_x = self.i_scale / self.i_vec
            k_y = self.j_scale / self.j_vec
            # x0 -> x1 -> x0
            # (x, 0) -> (x1, y1) -> (x0, y0)
            v = (xi - self.center.x) / self.i_vec * self.i_scale
            try:
                y = -(f.value_at(v) * self.j_vec / self.j_scale - self.center.y)
            except Exception:
                continue

            f.vertex_set.append(Vector(xi, y))

        for i in range(len(f.vertex_set) - 1):
            if not -PLOT_HEIGHT <= f.vertex_set[i].y - f.vertex_set[i+1].y <= PLOT_HEIGHT :
                continue
            self.create_line(f.vertex_set[i].x, f.vertex_set[i].y, f.vertex_set[i+1].x, f.vertex_set[i+1].y, fill='#2d2')


    def draw_grid(self):
        self.draw_vertex(self.center)


    def draw_vertex(self, v: Vector, clr='black', brush=2):
        self.create_oval(v.x-brush, v.y-brush, v.x+brush, v.y+brush, fill=clr)


    def show(self):
        x_i = self.center.x % self.i_vec
        while x_i < PLOT_WIDTH:
            col = '#888'
            if x_i == self.center.x:
                col = 'red'
            self.create_line(x_i, 0, x_i, PLOT_HEIGHT, fill=col)
            x_i += self.i_vec
        y_i = self.center.y % self.j_vec
        while y_i < PLOT_HEIGHT:
            col = '#888'
            if y_i == self.center.y:
                col = 'red'
            self.create_line(0, y_i,  PLOT_WIDTH, y_i, fill=col)
            y_i += self.j_vec
