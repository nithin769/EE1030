#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "libs/matfun.h"
#include "libs/geofun.h"

int main() {
	double **A,**B;
	A = createMat(2,1);
	B = createMat(2,1);
	A[0][0] = 2;
	A[1][0] = -1;
	B[0][0] = -2;
	B[1][0] = 1;
	FILE *file;
	file = fopen("values.dat", "w");

	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	fprintf(file, "x y\n");
	fprintf(file, "%lf %lf\n", A[0][0],A[1][0]);
	fprintf(file, "%lf %lf\n", B[0][0],B[1][0]);
	fclose(file);
	printf("Results have been written to values.dat\n");
	freeMat(A,2);
	freeMat(B,2);
	return 0;
}
