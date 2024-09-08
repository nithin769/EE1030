#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define EPSILON 1e-9  // A small threshold to treat values as zero

int calculateRank(float **M, int m, int n) {
    int rank = 0;

    // Process the matrix row by row
    for (int row = 0; row < m; row++) {
        // Find the first non-zero element in the current row
        int non_zero_column = -1;
        for (int col = 0; col < n; col++) {
            if (fabs(M[row][col]) > EPSILON) {
                non_zero_column = col;
                break;
            }
        }

        // If the row is entirely zero, skip it
        if (non_zero_column == -1) {
            continue;
        }

        // Increment rank since this row contributes to the rank
        rank++;

        // Normalize the row by making the leading coefficient 1
        float leading_coefficient = M[row][non_zero_column];
        for (int col = non_zero_column; col < n; col++) {
            M[row][col] /= leading_coefficient;
        }

        // Eliminate the leading coefficient from the rows below
        for (int i = row + 1; i < m; i++) {
            float factor = M[i][non_zero_column];
            for (int col = non_zero_column; col < n; col++) {
                M[i][col] -= factor * M[row][col];
            }
        }
    }
}

