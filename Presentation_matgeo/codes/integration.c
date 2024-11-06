#include <stdio.h>
#include <math.h>



double area(double lower_limit, double upper_limit)
{
	double sum=0 ;
	for ( double i = lower_limit; i<=upper_limit; i+=1e-7 )
	{
		sum += sqrt(4-i*i)*1e-7;
	}
	return sum ;
}
