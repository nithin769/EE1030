import matplotlib.pyplot as plt
import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./lib.so')

# Define argument and return types for the C function
lib.calculate_y.argtypes = [ctypes.c_int, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
lib.calculate_y.restype = None

def calculate_y(n, h):
    y = np.zeros(n, dtype=np.double)
    lib.calculate_y(n, h, y.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
    return y

# Parameters
n = 500 # Number of points
h = 0.01 # Step size

# Compute y values
y_itr = calculate_y(n, h)
x_itr = np.linspace(0, n*h, n)

# Theoretical Solution
def theo_result(x):
    return -(x*x)/2.0

# Calculating values
x_theory = np.linspace(0, n*h, 1000)  # Range of x for plotting
y_theory = theo_result(x_theory)

# Plot the results
plt.plot(x_itr, y_itr, label = "Sim" , color="red")
plt.plot(x_theory, y_theory, label = "Theory" , color="green", linestyle = "--")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.savefig('../figs/fig.png')
plt.show()


