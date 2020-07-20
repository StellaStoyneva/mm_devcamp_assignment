import unittest

from mm_devcamp_assignemnt.green_red.grid import Grid
from mm_devcamp_assignemnt.green_red.target import Target


class TestTarget(unittest.TestCase):

    def setUp(self):
        grid = Grid(4, 4)
        self.target = Target(grid, 2, 2, 15)

    def test_upon_init_create_attributes(self):
        self.assertEqual(self.target.col, 2)
        self.assertEqual(self.target.row, 2)
        self.assertEqual(self.target.iterations, 15)

    def test_col_setter_should_raise_error_if_abs_target_col_greater_than_grid_col(self):
        col = 5
        with self.assertRaises(Exception) as context: self.target.col(col)
        self.assertIsNotNone("number of target columns should not exceed the number of grid columns")

    def test_col_setter_should_raise_error_if_target_col_value_not_int(self):
        col = 'a'
        with self.assertRaises(Exception) as context: self.target.col(col)
        self.assertIsNotNone("number of target columns should be an integer")

    def test_row_setter_should_raise_error_if_abs_target_row_greater_than_grid_row(self):
        row = 5
        with self.assertRaises(Exception) as context: self.target.row(row)
        self.assertIsNotNone("number of target rows should not exceed the number of grid columns")

    def test_row_setter_should_raise_error_if_target_row_value_not_int(self):
        row = 'a'
        with self.assertRaises(Exception) as context: self.target.row(row)
        self.assertIsNotNone("number of target rows should be an integer")


if __name__ == '__main__':
    unittest.main()
