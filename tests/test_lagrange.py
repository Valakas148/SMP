import unittest
import sys
sys.path.append('G:\Ilya\interpolation_pkg')  # Add the path to the top-level folder (or the root folder of your project)
from interpolation.lagrange import LagrangeInterpolation
from unittest.mock import patch

class TestLagrangeInterpolation(unittest.TestCase):
    """
    Test class for LagrangeInterpolation class methods.
    """

    def setUp(self):
        """
        Set up the test data and LagrangeInterpolation instance.
        """
        self.x_values = [0, 0.5, 1, 2, 3.5, 4, 5]
        self.y_values = [12.234, 9.239, 8.567, -1.098, 5.756, 7.345, 5.678]
        self.lagrange = LagrangeInterpolation(self.x_values, self.y_values)

    def test_interpolation(self):
        """
        Test the interpolation method and print the result.
        """
        result1 = self.lagrange.print_(5)
        print("Result for x = 5:", result1)

    def test_plot_and_table(self):
        """
        Test the creation of the approximation table, check convergence, and plot interpolation.
        """
        table = self.lagrange.create_approximation_table()
        print("Approximation Table:")
        print(table)

        # Check the convergence of the interpolation process
        self.lagrange.check_convergence()

        self.lagrange.plot_interpolation()

if __name__ == '__main__':
    unittest.main()
    