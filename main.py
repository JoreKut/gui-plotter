import numpy

from component.application import App
from configuration.config import *
from  util.model.vector import Vector
import numpy as np
from util.model.reference_system import ReferenceSystem

if __name__ == '__main__':
    myapp = App()
    myapp.master.title(WINDOW_NAME)
    myapp.master.maxsize(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT)

    myapp.mainloop()

    A = np.array([[1,0],[0,-1]])
    B = np.array([[2,0],[0,3]])
    C = A.dot(B).dot(np.array([[4, 1]]).transpose())

    ex = ReferenceSystem(Vector(1,0), Vector(0,-1))
    inter = ReferenceSystem(Vector(2,0), Vector(0, 3),  Vector(6, 8))
    ex.add_child(inter)

    a = numpy.array([[2, 0],[0, 3]])
    b = numpy.array([[1, 0],[0, -1]])
    c = numpy.array([6, 8]).transpose()
    d = numpy.array([4, 1]).transpose()


    print(inter.transfer_from_root(Vector(14,5)).coord)
