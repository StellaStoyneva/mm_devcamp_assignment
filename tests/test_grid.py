import unittest
from mm_devcamp_assignemnt.green_red.grid import Grid
from mm_devcamp_assignemnt.green_red.target import Target


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid(4, 4)

    def test_upon_init_create_attributes(self):
        self.assertEqual(self.grid.cols, 4)
        self.assertEqual(self.grid.rows, 4)

    def test_col_setter_raiser_type_error_if_value_not_int(self):
        col = 'a'
        with self.assertRaises(Exception) as context: self.grid.cols(col)
        self.assertIsNotNone("number of columns should be an integer")

    def test_col_setter_raiser_value_error_if_value_less_than_1(self):
        col = -3
        with self.assertRaises(Exception) as context: self.grid.cols(col)
        self.assertIsNotNone("value for number of columns should be 1 or greater")

    def test_row_setter_raiser_type_error_if_value_not_int(self):
        row = 'a'
        with self.assertRaises(Exception) as context: self.grid.rows(row)
        self.assertIsNotNone("number of rows should be an integer")

    def test_row_setter_raiser_value_error_if_value_less_than_1(self):
        row = -3
        with self.assertRaises(Exception) as context: self.grid.rows(row)
        self.assertIsNotNone("value for number of rows should be 1 or greater")

    def test_func_create_generation_zero(self):
        self.grid.create_generation_zero('1001', '1111', '0100', '1010')
        expected = (self.grid.generation_zero[0][0].num, self.grid.generation_zero[1][1].num, self.grid.generation_zero[1][3].num)
        self.assertEqual(expected, (1, 1, 1))

    def test_func_create_generation_zero_raises_type_error(self):
        with self.assertRaises(TypeError) as g:
            self.grid.create_generation_zero('b', 'a', '0100', '1010')
        self.assertEqual(str(g.exception),
                         "args should contain only elements for which isdigit() = True or type is int")

    def test_func_count_times(self):
        self.grid.create_generation_zero('1001', '1111', '0100', '1010')
        target = Target(self.grid, 2, 2, 15)
        times_green = self.grid.count_times_green(target)
        self.assertEqual(times_green, 14)


if __name__ == '__main__':
    unittest.main()

