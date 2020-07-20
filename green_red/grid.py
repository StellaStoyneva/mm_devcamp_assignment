from mm_devcamp_assignemnt.green_red.cells import GreenCell, RedCell
from mm_devcamp_assignemnt.green_red.target import Target


class Grid:
    __directions = {'bottom left diagonal': [1, -1], 'bottom right diagonal': [1, 1],
                    'right': [0, 1], 'left': [0, -1],
                    'up': [-1, 0], 'down': [1, 0],
                    'top left diagonal': [-1, -1], 'top right diagonal': [-1, 1]}

    def __init__(self, *args):
        self.cols, self.rows = args
        self.generation_zero = []

    @property
    def cols(self):
        return self.__cols

    @cols.setter
    def cols(self, value):
        if not isinstance(value, int):
            raise TypeError('number of columns should be an integer')
        if value < 1:
            raise ValueError('value for number of columns should be 1 or greater')
        self.__cols = value

    @property
    def rows(self):
        return self.__rows

    @rows.setter
    def rows(self, value):
        if not isinstance(value, int):
            raise TypeError('number of row should be an integer')
        if not isinstance(value, int):
            raise ValueError('value for number of rows should be 1 or greater')
        self.__rows = value



    def create_generation_zero(self, *args):
        for i in range(self.rows):
            data = args[i]
            if self.__data_type_valid(data):
                row = self.__create_row(data)
                self.generation_zero.append(row)
        return self.generation_zero

    def count_times_green(self, target):
        times_green = 0
        for _ in range(target.iterations):
            new_generation = self.__create_new_generation(target)
            target_cell = new_generation[target.row][target.col]
            if target_cell.__class__.__name__ == 'GreenCell':
                times_green += 1
            self.generation_zero = new_generation
            self.__reset_generation_zero(new_generation)
        return times_green

    def __repr__(self):
        self.generation_zero = [x.num for sublist in self.generation_zero for x in sublist]
        return self.generation_zero


    def __data_type_valid(self, data):
        if not isinstance(data, int) and not data.isdigit():
            raise TypeError("args should contain only elements for which isdigit() = True or type is int")
        return True

    def __create_row(self, data):
        data = str(data)
        row = []
        for value in data:
            cell =self.__instantiate_cell(int(value))
            row.append(cell)
        return row

    def __instantiate_cell(self, value):
        if value == 0:
            current_cell = RedCell(value)
        else:
            current_cell = GreenCell(value)
        return current_cell

    def __set_neighbour_row(self, row, direction):
        return row + Grid.__directions[direction][0]

    def __set_neighbour_col(self, col, direction):
        return col + Grid.__directions[direction][1]

    def __neighbour_cell_valid(self, neighbour_row, neighbour_col, j):
        return 0 <= neighbour_row < len(self.generation_zero) and 0 <= neighbour_col < len(self.generation_zero[j])

    def __set_new_neighbour(self, neighbour_row, neighbour_col, j):
        if self.__neighbour_cell_valid(neighbour_row, neighbour_col, j):
            new_neighbour = self.generation_zero[neighbour_row][neighbour_col]
            return new_neighbour

    def __generate_list_green_neighbours(self, row, col, j):
        green_neighbours = []
        for direction in Grid.__directions:
            neighbour_row = self.__set_neighbour_row(row, direction)
            neighbour_col = self.__set_neighbour_col(col, direction)
            new_neighbour = self.__set_new_neighbour(neighbour_row, neighbour_col, j)
            if new_neighbour and new_neighbour.__class__.__name__ == 'GreenCell':
                green_neighbours.append(1)
            else:
                green_neighbours.append(0)
        return green_neighbours

    def __set_new_cell(self, current_cell, green_neighbours_list):
        if sum(green_neighbours_list) in (0, 1, 4, 5, 7, 8) and current_cell.__class__.__name__ == 'GreenCell':
            new_cell = RedCell(0)
        elif sum(green_neighbours_list) in (3, 6) and current_cell.__class__.__name__ == 'RedCell':
            new_cell = GreenCell(1)
        else:
            new_cell = current_cell
        return new_cell


    def __create_new_generation(self, target: Target):
        new_generation = []
        for j in range(len(self.generation_zero)):
            new_row = []
            for i in range(len(self.generation_zero[j])):
                row, col = j, i
                current_cell = self.generation_zero[row][col]
                green_neighbours_list = self.__generate_list_green_neighbours(row, col, j)
                new_cell = self.__set_new_cell(current_cell, green_neighbours_list)
                new_row.append(new_cell)
            new_generation.append(new_row)
        return new_generation

    def __reset_generation_zero(self, new_generation):
        self.generation_zero = new_generation


