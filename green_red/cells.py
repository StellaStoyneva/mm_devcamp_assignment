class RedCell:
    def __init__(self, num):
        self.num = num

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if value != 0:
            raise ValueError('red cell can have value only of 0')
        self.__num = value

class GreenCell:
    def __init__(self, num):
        self.num = num

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if value != 1:
            raise ValueError('cell can have value only of 1')
        self.__num = value