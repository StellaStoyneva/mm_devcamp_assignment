class Target:
    def __init__(self, obj, *args):
        self.obj = obj
        self.col, self.row, self.iterations = args

    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, value):
        if not isinstance(value, int):
            raise TypeError('number of target columns should be an integer')
        elif abs(value) > self.obj.cols:
            raise ValueError('number of target columns should not exceed the number of grid columns')
        self.__col = value

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, value):
        if not isinstance(value, int):
            raise TypeError('number of target columns should be an integer')
        elif abs(value) > self.obj.rows:
            raise ValueError('number of target rows should not exceed the number of grid rows')
        self.__row = value


