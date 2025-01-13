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

# Parameters for C library computation
n_c = 500  # Number of points
h_c = 0.01  # Step size

# Compute y values from the C library
y_itr = calculate_y(n_c, h_c)
x_itr = np.linspace(0, n_c * h_c, n_c)

# Parameters for Python simulation
h = 0.01  # Step size
coeff = -(h / 2)**3  # Constant coefficient for the right-hand side
n_samples = n_c  # Match the number of samples for consistency

# Initialize y array and input u[n]
y_sim = [0] * n_samples  # Output signal (initialize to zero)
u = [1 if n > 0 else 0 for n in range(n_samples)]  # Input signal

# Compute the difference equation
for n in range(2, n_samples):  # Start from n=2 since y[0] and y[1] are initial conditions
    rhs = coeff * (1 + 3 * u[n-1] + 3 * u[n-2] + u[n-3]) if n >= 3 else coeff * (1 + 3 * u[n-1] + 3 * u[n-2])
    y_sim[n] = 3 * y_sim[n-1] - 3 * y_sim[n-2] + (y_sim[n-3] if n >= 3 else 0) + rhs

# Convert y_sim to a numpy array for plotting
y_sim = np.array(y_sim)

def theory_value(x):
    return -(x*x)/2.0

y_theory = theory_value(x_itr) 
# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x_itr, y_itr, label="Theory2", color="red")
plt.plot(x_itr, y_theory, label = "Theory1", color="blue")
plt.plot(x_itr, y_sim, label="Sim", color="green", linestyle="--", marker="o", markersize = 2)
plt.xlabel("Time (s)")
plt.ylabel("Output y(n)")
plt.title("Comparison of Theoretical and Simulated Results")
plt.legend()
plt.grid(True)
plt.savefig('../figs/fig.png')
plt.show()

