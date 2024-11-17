import numpy as np

# Function to take matrix input from the user
def get_matrix_input():
    rows = int(input("Enter the number of rows (and columns) of the matrix: "))
    matrix = []
    print(f"Enter the elements of the {rows}x{rows} matrix row by row:")
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i+1} elements separated by spaces: ").split()))
        matrix.append(row)
    return np.array(matrix)

# Get matrix input from the user
A = get_matrix_input()

# Check if the matrix is square
if A.shape[0] != A.shape[1]:
    print("Matrix must be square!")
else:
    # Calculate eigenvalues
    eigenvalues = np.linalg.eigvals(A)
    print("Eigenvalues:", eigenvalues)

