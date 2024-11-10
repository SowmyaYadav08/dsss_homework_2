import unittest
from math_quiz import gen_num, gen_operator, create_math_problem


class TestMathGame(unittest.TestCase):

    def test_gen_num(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = gen_num (min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_gen_operator(self):
        # TODO
        pass

    def test_create_math_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),    #Addition
                (10, 3, '-', '10 - 3', 7),  # Subtraction
                (4, 3, '*', '4 * 3', 12),  # Multiplication
                (0, 5, '+', '0 + 5', 5),  # Edge case with zero
                (6, 6, '-', '6 - 6', 0),  # Edge case with zero result
                (3, 1, '*', '3 * 1', 3),  # Multiplication with one

            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = create_math_problem(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
