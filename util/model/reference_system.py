import numpy

from util.model.vector import Vector


class ReferenceSystem:

    def __init__(self, i_vec: Vector, j_vec: Vector, center=Vector(0, 0)):
        self.i_vec = i_vec
        self.j_vec = j_vec
        self.center = center
        self.root = None

    def add_child(self, system):
        system.root = self

    def transfer_to_root(self, v: Vector) -> Vector:
        center = numpy.array(self.center.coord).transpose()
        C_ex = numpy.array([self.root.i_vec.coord, self.root.j_vec.coord]).transpose()
        C_in = numpy.array([self.i_vec.coord, self.j_vec.coord]).transpose()
        v_in = numpy.array(v.coord).transpose()

        V_ex = center + C_ex.dot(C_in).dot(v_in)

        return Vector(V_ex[0], V_ex[1])

    def transfer_from_root(self, v: Vector) -> Vector:
        center = numpy.array(self.center.coord)
        C_ex = numpy.array([self.root.i_vec.coord, self.root.j_vec.coord]).transpose()
        C_in = numpy.array([self.i_vec.coord, self.j_vec.coord]).transpose()
        V_ex = numpy.array(v.coord).transpose()

        v_in = numpy.linalg.inv(C_in.dot(C_ex)).dot(V_ex - center)

        return Vector(v_in[0], v_in[1])
