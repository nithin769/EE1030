import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./verifyrank.so')

# Define the argument and return types of the C function
lib.calculateRank.argtypes = [ctypes.POINTER(ctypes.POINTER(ctypes.c_float)), ctypes.c_int, ctypes.c_int]
lib.calculateRank.restype = ctypes.c_int

# Example matrix
matrix = np.array([
    [-7, -4],
    [3, 1.714286]
], dtype=np.float32)

m, n = matrix.shape

# Convert the numpy array to ctypes format
MatrixType = ctypes.POINTER(ctypes.c_float) * m
c_matrix = MatrixType(*[row.ctypes.data_as(ctypes.POINTER(ctypes.c_float)) for row in matrix])

# Call the C function to calculate the rank
rank = lib.calculateRank(c_matrix, m, n)

print(f"The rank of the matrix is: {rank}")




