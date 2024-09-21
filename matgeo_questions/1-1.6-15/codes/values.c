#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "rankcalculation/libs/matfun.h"
#include "rankcalculation/libs/geofun.h"

int main() {
	double **A,**B,**C;
	A = createMat(2,1);
	B = createMat(2,1);
	C = createMat(2,1);
	A[0][0] = 5;
	A[1][0] = 1;
	B[0][0] = -2;
	B[1][0] = -3;
	C[0][0] = 8;
	C[1][0] = 19.0/7.0;
	FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "x y\n");
	fprintf(file, "%.6lf %.6lf\n", A[0][0],A[1][0]);
	fprintf(file, "%.6lf %.6lf\n", B[0][0],B[1][0]);
	fprintf(file, "%.6lf %.6lf\n", C[0][0],C[1][0]);
	fclose(file);
	printf("Results have been written to values.dat\n");

	freeMat(A,2);
	freeMat(B,2);
	freeMat(C,2);
	return 0;
}
