import unittest
from mm_devcamp_assignemnt.green_red.cells import RedCell


class TestRedCell(unittest.TestCase):
    def setUp(self):
        self.red_cell = RedCell(0)


    def test_upon_init_create_attribute_num(self):
        self.assertEqual(self.red_cell.num, 0)

    def test_num_setter_should_raise_raise_error_if_element_NOT_equalt_to_0(self):
       num = 3
       with self.assertRaises(Exception) as context: self.red_cell.num(num)
       self.assertIsNotNone("red cell can have value only of 0")


if __name__ == "__main__":
    unittest.main()
