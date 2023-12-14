import numpy as np
import matplotlib.pyplot as plt

class NewtonInterpolation:
    def __init__(self, x, y):
        """
        Initialize the NewtonInterpolation class with input data.

        Parameters:
        - x: array-like, x-coordinates of data points
        - y: array-like, y-coordinates of data points
        """
        self.x = np.array(x)
        self.y = np.array(y)
        self.coeffs = self.newton_coefficients()

    def compute_diffs(self, x, y):
        """
        Compute differences table for Newton interpolation.

        Parameters:
        - x: array-like, x-coordinates of data points
        - y: array-like, y-coordinates of data points

        Returns:
        - dict: {"diffs": differences table, "F": divided differences}
        """
        deltas = [np.diff(y)]
        j = 2
        while len(deltas[-1]) > 1:
            deltas.append(np.diff(deltas[-1]))
            j += 1

        n = len(y)
        diffs = np.zeros((n, n))
        F = np.zeros((n, n))

        for j in range(len(deltas)):
            for i in range(1, n - j):
                diffs[i, j + 1] = deltas[j][i - 1]
                if (x[i + j] - x[i]) != 0:
                    F[i, j + 1] = diffs[i, j + 1] / (x[i + j] - x[i])
                else:
                    F[i, j + 1] = np.nan 


        return {"diffs": diffs, "F": F}

    def newton_coefficients(self):
        """
        Compute Newton interpolation coefficients.

        Returns:
        - array: Newton interpolation coefficients
        """
        n = len(self.x)
        coeffs = np.zeros(n)

        for i in range(n):
            coeffs[i] = self.y[i]

        print("Newton Interpolation Coefficients:")
        for j in range(2, n + 1):
            for i in range(n, j - 1, -1):
                coeffs[i - 1] = (coeffs[i - 1] - coeffs[i - 2]) / (self.x[i - 1] - self.x[i - j])

            print(f"a{j - 1} =", "{:.4f}".format(coeffs[j - 1]))

        return coeffs

    def newton_interpolation_safe(self, x_interp):
        """
        Perform Newton interpolation at a given x value.

        Parameters:
        - x_interp: float, x value for interpolation

        Returns:
        - float: Interpolated y value
        """
        n = len(self.x)
        result = np.nan if x_interp < min(self.x) or x_interp > max(self.x) else self.coeffs[-1]

        for i in range(n - 2, -1, -1):
            result = np.nan if x_interp < min(self.x) or x_interp > max(self.x) else result * (x_interp - self.x[i]) + self.coeffs[i]

        return result


    def print_diff_table(self, diffs):
        """
        Print the differences table.

        Parameters:
        - diffs: array-like, differences table
        """
        print("x\ty", end="")
        for i in range(1, np.shape(diffs)[1]):
            print(f"\tΔy{i}", end="")
        print()

        for i in range(len(self.x)):
            print("{:.3f}\t{:.3f}".format(self.x[i], self.y[i]), end="")
            for j in range(1, np.shape(diffs)[1]):
                if i + j - 1 < len(self.x):
                    print("\t{:.4f}".format(diffs[i, j]), end="")
                else:
                    print("\t", end="")
            print()

    def format_polynomial(self):
        """
        Format the Newton interpolation polynomial.

        Returns:
        - str: Formatted polynomial as a string
        """
        n = len(self.coeffs)
        terms = []

        for i in range(n):
            term = ""
            if i == 0:
                term = "{:.4f}".format(self.coeffs[i])
            else:
                if self.coeffs[i] >= 0:
                    term = "+{:.4f}".format(self.coeffs[i])
                else:
                    term = "-{:.4f}".format(abs(self.coeffs[i]))

                if i > 1:
                    term += "(" + "*".join(f"(x - {xi:.3f})" for xi in self.x[:i - 1]) + ")"
                else:
                    term += "(x - {:.3f})".format(self.x[i - 1])

            terms.append(term)

        return " ".join(terms)

    def plot_interpolation(self, x_interp):
        """
        Plot the Newton interpolation polynomial and data points.

        Parameters:
        - x_interp: array-like, x values for interpolation
        """
        x_interp_plot = np.linspace(min(self.x), max(self.x), 1000)
        y_interp_plot = [self.newton_interpolation_safe(x_val) for x_val in x_interp_plot]

        plt.scatter(self.x, self.y, color="blue", s=30, label="Data Points")
        plt.plot(x_interp_plot, y_interp_plot, color="red", linewidth=2, label="Interpolation Polynomial")
        plt.title("Newton Interpolation Polynomial")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.show()

        value_at_x_interp = self.newton_interpolation_safe(x_interp)
        print(f"Interpolated value at x = {x_interp:.3f}: {value_at_x_interp:.4f}")

        print("Interpolation Polynomial Equation:")
        print(self.format_polynomial())


"""
# Example usage
x_data = [0, 0.5, 1, 2, 3.5, 4, 5]
y_data = [12.234, 9.239, 8.567, -1.098, 5.756, 7.345, 5.678]
x_interp_value = 5

# Create NewtonInterpolation object
newton_interp = NewtonInterpolation(x_data, y_data)

# Compute differences table
result = newton_interp.compute_diffs(x_data, y_data)

# Print differences table
newton_interp.print_diff_table(result["diffs"])

# Plot interpolation and print results
newton_interp.plot_interpolation(x_interp_value)
"""