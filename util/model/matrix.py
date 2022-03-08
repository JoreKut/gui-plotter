def get_empty_matrix(rows, columns):
    return [[0 for i in range(columns)] for i in range(rows)]

class Matrix:

    def __init__(self, rows, columns, mtx=None):
        self.rows = rows
        self.column = columns
        self.mtx = mtx if mtx is not None else [ [0 for i in range(columns)] for i in range(rows)]

    def set_row(self, index, row):
        self.mtx[index] = row
