import unittest
import random

from calc import add as add_, sub as sub_, div as div_, mul as mul_


class MyTestClass(unittest.TestCase):

    def test_add_valid(self):
        a, b = random.randint(1, 1000), random.randint(1, 1000)
        self.assertEquals(a + b, add_(a, b), "Sum value is not valid. Correct answer is: " + str(a + b))

    def test_sub_valid(self):
        a, b = random.randint(1, 1000), random.randint(1, 1000)
        self.assertEquals(a - b, sub_(a, b), "Subtraction value is not valid. Correct answer is: " + str(a - b))

    def test_div_valid(self):
        a, b = random.randint(1, 1000), random.randint(1, 1000)
        self.assertEquals(a // b, div_(a, b), "Floor division value is not valid. Correct answer is: " + str(a // b))

    def test_mul_valid(self):
        a, b = random.randint(1, 1000), random.randint(1, 1000)
        self.assertEquals(a * b, mul_(a, b), "Multiply value is not valid. Correct answer is: " + str(a * b))

    def test_div_zero(self):
        a, b = random.randint(1, 1000), 0
        with self.assertRaises(ZeroDivisionError, msg="Zero division is prohibited!"):
            div_(a, b)

    def test_add_type(self):
        a, b = random.uniform(-1000, 1000), random.uniform(-1000, 1000)
        with self.assertRaises(TypeError, msg="Type error!"):
            add_(a, b)

    def test_sub_type(self):
        a, b = random.uniform(-1000, 1000), random.uniform(-1000, 1000)
        with self.assertRaises(TypeError, msg="Type error!"):
            sub_(a, b)

    def test_div_type(self):
        a, b = random.uniform(-1000, 1000), random.uniform(1, 1000)
        with self.assertRaises(TypeError, msg="Type error!"):
            div_(a, b)

    def test_mul_type(self):
        a, b = random.uniform(-1000, 1000), random.uniform(-1000, 1000)
        with self.assertRaises(TypeError, msg="Type error!"):
            mul_(a, b)


if __name__ == "__main__":
    unittest.main()
