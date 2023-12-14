import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class LagrangeInterpolation:
    """
    Class for performing Lagrangian interpolation and related calculations.
    """

    def __init__(self, x_list, y_list):
        """
        Initializes the LagrangeInterpolation object.

        Parameters:
        - x_list (list): List of X values.
        - y_list (list): List of corresponding Y values related to X.
        """
        if len(x_list) != len(y_list):
            raise ValueError("Lists x and y must have the same length.")

        self.x = np.array(x_list)
        self.y = np.array(y_list)

    def interpolate(self, x_val):
        """
        Performs Lagrangian interpolation for the given X value.

        Parameters:
        - x_val (float): The X value for which interpolation is performed.

        Returns:
        - float: The result of interpolation for the given X value.
        """
        n = len(self.x)
        result = 0

        for i in range(n):
            term = self.y[i]

            for j in range(n):
                if j != i:
                    term *= (x_val - self.x[j]) / (self.x[i] - self.x[j])

            result += term

        return result

    def create_approximation_table(self):
        """
        Creates a table of the approximate function values.

        Returns:
        - pandas.DataFrame: A table with X values and corresponding approximate Y values.
        """
        x_values = np.arange(np.floor(np.min(self.x)), np.ceil(np.max(self.x)) + 0.1, 0.1)
        y_values = np.vectorize(self.interpolate)(x_values)
        approximation_table = pd.DataFrame({'X': x_values, 'Approximated Y': y_values})
        return approximation_table

    def check_convergence(self):
        """
        Checks the convergence of the interpolation process and prints errors.

        Prints:
        - str: A string with information about errors and the convergence of interpolation.
        """
        errors = self.y - np.vectorize(self.interpolate)(self.x)
        print("\n\nErrors:", errors)
        convergence = np.all(np.abs(errors) < 1e-10)
        print("Convergence of the interpolation process:", convergence)

    def plot_interpolation(self):
        """
        Plots the Lagrangian interpolation graph and input points.

        Displays:
        - matplotlib.pyplot.plot: Plot of Lagrangian interpolation and input points.
        """
        x_values = np.arange(np.floor(np.min(self.x)), np.ceil(np.max(self.x)) + 0.1, 0.1)
        y_values = np.vectorize(self.interpolate)(x_values)

        plt.plot(x_values, y_values, label='Lagrangian Interpolation', color='blue')
        plt.scatter(self.x, self.y, label='Input Points', color='red')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Lagrangian Interpolation')
        plt.legend()
        plt.show()

    def print_(self, x_val):
        """
        Prints the interpolation polynomial and its components for the given X value.

        Parameters:
        - x_val (float): The X value for which the interpolation polynomial is printed.

        Returns:
        - float: The result of interpolation for the given X value.
        """
        n = len(self.x)
        result = 0
        d = 0
        print("\nInterpolation polynomial for x =", x_val)
        for i in range(n):
            term = self.y[i]
            print("(", self.y[i], " * L", i, "(", x_val, ")) = ", self.y[i])

            for j in range(n):
                if j != i:
                    term *= (x_val - self.x[j]) / (self.x[i] - self.x[j])
                    print(" * (", x_val, " - ", self.x[j], ") / (", self.x[i], " - ", self.x[j], ")", end="")
                    print("Multiplier:", j, "=", (x_val - self.x[j]) / (self.x[i] - self.x[j]))

            d = term
            print("(", self.y[i], " * L", i, "(", x_val, ")) = ", term)
            result += term

        return result
