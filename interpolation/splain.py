import numpy as np
import matplotlib.pyplot as plt

class CubicSplineInterpolator:
    class SplineTuple:
        def __init__(self, a, b, c, d, x):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.x = x

    def __init__(self, x_values, y_values):
        self.x_values = np.array(x_values)
        self.y_values = np.array(y_values)
        self.spline_result = self.build_spline()

    def build_spline(self):
        n = len(self.x_values)
        splines = [self.SplineTuple(0, 0, 0, 0, 0) for _ in range(n)]

        for i in range(n):
            splines[i].x = self.x_values[i]
            splines[i].a = self.y_values[i]

        splines[0].c = splines[n - 1].c = 0.0

        alpha = np.zeros(n - 1)
        beta = np.zeros(n - 1)

        for i in range(1, n - 1):
            hi = self.x_values[i] - self.x_values[i - 1]
            hi1 = self.x_values[i + 1] - self.x_values[i]
            A = hi
            C = 3.0 * (hi + hi1)
            B = hi1
            F = 6.0 * ((self.y_values[i + 1] - self.y_values[i]) / hi1 - (self.y_values[i] - self.y_values[i - 1]) / hi)
            z = A * alpha[i - 1] + C
            alpha[i] = -B / z
            beta[i] = (F - A * beta[i - 1]) / z

        for i in range(n - 2, 0, -1):
            splines[i].c = alpha[i] * splines[i + 1].c + beta[i]

        for i in range(n - 1, 0, -1):
            hi = self.x_values[i] - self.x_values[i - 1]
            splines[i].d = (splines[i].c - splines[i - 1].c) / hi
            splines[i].b = hi * (2.0 * splines[i].c + splines[i - 1].c) / 6.0 + (self.y_values[i] - self.y_values[i - 1]) / hi

        return splines

    def interpolate(self, x):
        if not self.spline_result:
            return None

        n = len(self.spline_result)
        s = self.SplineTuple(0, 0, 0, 0, 0)

        if x <= self.spline_result[0].x:
            s = self.spline_result[0]
        elif x >= self.spline_result[n - 1].x:
            s = self.spline_result[n - 1]
        else:
            i, j = 0, n
            while i + 1 < j:
                k = i + (j - i) // 2
                if x <= self.spline_result[k].x:
                    j = k
                else:
                    i = k
            s = self.spline_result[j]
        dx = x - s.x
        return s.a + (s.b + (s.c / 2.0 + s.d * dx / 6.0) * dx) * dx

    def plot_spline_interpolation(self):
        curve_points = np.linspace(min(self.x_values), max(self.x_values), 100)
        spline_values = [self.interpolate(pt) for pt in curve_points]

        plt.plot(curve_points, spline_values, label='Spline', color='blue')
        plt.scatter(self.x_values, self.y_values, label='Data Points', color='red')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Cubic Spline Interpolation')
        plt.legend()
        plt.show()


"""
# Вхідні дані
x_values = np.array([0, 0.5, 1, 2, 3.5, 4, 5])
y_values = np.array([12.234, 9.239, 8.567, -1.098, 5.756, 7.345, 5.678])
new_x_value = 5

# Створення об'єкта класу CubicSplineInterpolator
spline_interpolator = CubicSplineInterpolator(x_values, y_values)

# Виведення значення функції при x = 5
result_value = spline_interpolator.interpolate(new_x_value)
print(f'Значення функції при x = {new_x_value}: {result_value}')

# Графічне відображення кубічного сплайну
spline_interpolator.plot_spline_interpolation()
"""