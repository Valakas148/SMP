import unittest
import sys
sys.path.append('G:\Ilya\interpolation_pkg')  # Додайте шлях до верхнього рівня папки (або кореневої папки) вашого проекту
from interpolation.newton import NewtonInterpolation

class TestNewtonInterpolation(unittest.TestCase):
    def setUp(self):
        self.x_data = [0, 0.5, 1, 2, 3.5, 4, 5]
        self.y_data = [12.234, 9.239, 8.567, -1.098, 5.756, 7.345, 5.678]
        self.x_interp_value = 5
        self.newton_interp = NewtonInterpolation(self.x_data, self.y_data)

    def test_compute_diffs(self):
        result = self.newton_interp.compute_diffs()
        self.assertEqual(result["diffs"].shape, (len(self.x_data), len(self.x_data)))


    def test_print_diff_table(self):
        result = self.newton_interp.compute_diffs()
        self.newton_interp.print_diff_table(result["diffs"])

    def test_plot_interpolation(self):
        self.newton_interp.plot_interpolation(self.x_interp_value)

if __name__ == '__main__':
    unittest.main()
