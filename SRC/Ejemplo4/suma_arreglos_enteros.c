//program to do array add to vectors
#include <stdio.h> // libreria  que ayuda a funciones en c
#include <stdlib.h>// libreria para convertir un enero a cadena de caracteres

int sum_array (int a[10],int b[10]){ //  deermina el tipo de funcion  in_suma de las varibales de los arreglos a y b
	int resultado[10];

for (int i = 0; i < 10; i++) {  // realiza las iteraciones  de la suma de los dos arreglos, en unn ciclo for
	resultado[i] = a[i] + b[i];
}

for (int i = 0; i < 10; i++) {  // realiza un ciclo for  que empieza en cero pero es menor que 10 que imprime el resultado
	printf("%d ", resultado[i]);
	
}
return resultado[10]; // regresa el resulado de las iteraciones
}




