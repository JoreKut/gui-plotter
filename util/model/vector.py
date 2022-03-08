import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coord = [x, y]
        self.length = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy