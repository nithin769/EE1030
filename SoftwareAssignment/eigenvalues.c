#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_ITERATIONS 1000
#define EPSILON 1e-10

// Function to normalize a vector
void normalize_vector(double *v, int n) {
    double norm = 0.0;
    for (int i = 0; i < n; i++) {
        norm += v[i] * v[i];
    }
    norm = sqrt(norm);

    if (norm > EPSILON) {
        for (int i = 0; i < n; i++) {
            v[i] /= norm;
        }
    }
}

// Function for Gram-Schmidt process
void gram_schmidt(double *A, double *Q, double *R, int n) {
    for (int k = 0; k < n; k++) {
        // Copy column k from A to Q
        for (int i = 0; i < n; i++) {
            Q[i * n + k] = A[i * n + k];
        }

        // Orthogonalize against previous columns
        for (int j = 0; j < k; j++) {
            R[j * n + k] = 0.0;
            for (int i = 0; i < n; i++) {
                R[j * n + k] += Q[i * n + j] * Q[i * n + k];
            }
            for (int i = 0; i < n; i++) {
                Q[i * n + k] -= R[j * n + k] * Q[i * n + j];
            }
        }

        // Normalize column k
        R[k * n + k] = 0.0;
        for (int i = 0; i < n; i++) {
            R[k * n + k] += Q[i * n + k] * Q[i * n + k];
        }
        R[k * n + k] = sqrt(R[k * n + k]);

        if (fabs(R[k * n + k]) > EPSILON) {
            for (int i = 0; i < n; i++) {
                Q[i * n + k] /= R[k * n + k];
            }
        }
    }
}

// Function to multiply two matrices (C = A * B)
void multiply_matrices(double *A, double *B, double *C, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i * n + j] = 0.0;
            for (int k = 0; k < n; k++) {
                C[i * n + j] += A[i * n + k] * B[k * n + j];
            }
        }
    }
}

// Function to compute all eigenvalues using the QR algorithm
void qr_algorithm(double *A, int n, double *eigenvalues) {
    double *Q = (double *)malloc(n * n * sizeof(double));
    double *R = (double *)malloc(n * n * sizeof(double));
    double *A_new = (double *)malloc(n * n * sizeof(double));

    // Copy input matrix A to A_new
    for (int i = 0; i < n * n; i++) {
        A_new[i] = A[i];
    }

    // QR iteration
    for (int iter = 0; iter < MAX_ITERATIONS; iter++) {
        gram_schmidt(A_new, Q, R, n); // Decompose A_new into Q and R
        multiply_matrices(R, Q, A_new, n); // A_new = R * Q

        // Check for convergence (off-diagonal elements close to zero)
        int converged = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && fabs(A_new[i * n + j]) > EPSILON) {
                    converged = 0;
                    break;
                }
            }
        }
        if (converged) {
            break;
        }
    }

    // Extract eigenvalues from the diagonal of A_new
    for (int i = 0; i < n; i++) {
        eigenvalues[i] = A_new[i * n + i];
    }

    free(Q);
    free(R);
    free(A_new);
}

int main() {
    int n;

    printf("Enter the size of the matrix: ");
    scanf("%d", &n);

    if (n > 20) {
        printf("Matrix size should be less than or equal to 20.\n");
        return 1;
    }

    double *A = (double *)malloc(n * n * sizeof(double));
    double *eigenvalues = (double *)malloc(n * sizeof(double));

    printf("Enter the elements of the matrix A (real numbers):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("A[%d][%d] = ", i, j);
            scanf("%lf", &A[i * n + j]);
        }
    }

    qr_algorithm(A, n, eigenvalues);

    printf("The eigenvalues are:\n");
    for (int i = 0; i < n; i++) {
        printf("%.16lf\n", eigenvalues[i]);
    }

    free(A);
    free(eigenvalues);

    return 0;
}
