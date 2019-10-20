import unittest

import my_functions


class TestMyFunctions(unittest.TestCase):
    def test_add_intiger(self):
        self.assertEqual(my_functions.add(3, 4), 7)
        self.assertEqual(my_functions.add(-3, 4), 1)
        self.assertEqual(my_functions.add(0, 0), 0)

    def test_add_float(self):
        self.assertAlmostEqual(my_functions.add(3.2, 5.0), 8.2)
        self.assertAlmostEqual(my_functions.add(0.0, 0.0), 0.0)
        self.assertAlmostEqual(my_functions.add(-3.5, 5.0), 1.5)

    def test_add_string(self):
        self.assertEqual(my_functions.add("aa", "bb"), "aabb")
        self.assertEqual(my_functions.add("",""),"")

class TestDivide(unittest.TestCase):
    def test_value_error(self):
        self.assertRaises(ValueError, my_functions.divide, 3 , 0)
        self.assertRaises(ValueError, my_functions.divide, 0 , 0)


if __name__ == "__main__":
    unittest.main()

#Zadanie
#Pokrycie testami 100%