import unittest
from mm_devcamp_assignemnt.green_red.cells import GreenCell


class TestRedCell(unittest.TestCase):
    def setUp(self):
        self.green_cell = GreenCell(1)

    def test_upon_init_create_attribute_num(self):
        self.assertEqual(self.green_cell.num, 1)

    def test_num_setter_should_raise_raise_error_if_element_NOT_equalt_to_0(self):
        num = 3
        with self.assertRaises(Exception) as context: self.green_cell.num(num)
        self.assertIsNotNone("red cell can have value only of 0")


if __name__ == "__main__":
    unittest.main()
