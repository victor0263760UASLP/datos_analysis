//programa que permite apartir de dos variables flotantes y un entero, encontrar la secuencia de caracteres.
#include <stdio.h>
#include <stdlib.h>

float*array_float_string(float X0, float Xn, int n){

float*x = (float*)malloc((n + 1)*sizeof(float));
float dx =(Xn -X0)/(n+1);
for (int i =0; i<=n; i++){


	x[i] = i*dx + X0;
}


return x;

}