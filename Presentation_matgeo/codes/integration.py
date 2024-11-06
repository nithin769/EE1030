import ctypes

# Load the shared library
lib = ctypes.CDLL('./integration.so')
lib.area.argtypes = [ctypes.c_double, ctypes.c_double]
lib.area.restype = ctypes.c_double
print("Area enclosed:",lib.area(0,2))
