import unittest
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('G:\Ilya\interpolation_pkg')
from interpolation.splain import CubicSplineInterpolator

class TestCubicSplineInterpolation(unittest.TestCase):
    def test_interpolation(self):
        x_values = [0, 0.5, 1, 2, 3.5, 4, 5]
        y_values = [12.234, 9.239, 8.567, -1.098, 5.756, 7.345, 5.678]

        spline = CubicSplineInterpolator(x_values, y_values)

        result = spline.interpolate(5)
        print("Result for x = 5:", result)

        
        spline.plot_spline_interpolation()
        

if __name__ == "__main__":
    unittest.main()
