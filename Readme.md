# Manual paso por paso de C a Py

 


## Fundamentos de nociónes de funciónes en c 

Una de las características más importantes es la manipulación de diversos archivos por la cual es muy útil en esta ocasión utilizar, programar en c y manipularlos con Python. 

Por esa razón podemos ordenar nuestro código de la siguiente forma en la que se describe a continuación la importancia de c y Python comenzamos con la pregunta. 

## Por qué utilizar lenguaje en c? 

Una de las principales ventajas al utilizar es por su alta velocidad de ejecución de los programas compilados en C es un punto decisivo para utilizar el lenguaje.  

 

## Por qué python? 

En cuanto a la flexibilidad de python es muy versátil y flexible gracias a su diseño lo cual es muy importante en el desarrollo de programas en Python. 

## Cómo comenzamos? 

 

Primero hacemos un código en lenguaje c que sume dos números, y este pueda generar la suma. 

Después hacemos un programa en Python que pueda extraer el programa e imprimirlo. 

 

Las librerías para instalar cada uno de los paquetes podemos verlos de la siguiente manera, para instalar Python y las librerías para generar los archivos    ya que en la terminal solo admite instalar los programas con la palabra seudo seguido de la contraseña que nos permitió ingresar al programa. 

Posteriormente se instalaran todos los paquetes correspondientes a la aplicación uno de los paquetes no se instala el programa de Python o c no funcionara. 

Los Paths correspondientes se pueden consultan ingresando a la plataforma de Git Hub donde dependiendo de los requerimientos de tu equipo podrás consultarlos 
e instalarlos con la palabra seudo dependiendo de los requerimientos necesarios en el programa de tu computadora, sin embargo en Visual Studio se encuentran muchas herramientas de compilación.

 
Ahora estamos listos para crear nuestros scripts  de c, generar el archivo .so  y  ayudandonos para administrarlo con Python con la biblioteca ctypes.



## Implementación  

 

Podemos implementar una función para un sistema de arreglos en donde sumamos dos arreglos e imprimimos la suma de los arreglos llamando una función para posteriormente con el programa Python llamarla con ctypes. 

Después podemos generar un archivo .so e utilizarlo en Python para importarlo e imprimir los arreglos en este caso podemos generar un conjunto de archivos. 

 

Después puedes crear un Makefile que me pueda imprimir el archivo .so de manera que se generé la función array suma y también añadir el archivo .h de la librería de nuestra función en c. 


## Creación de Archivo .so porque es muy importante? 

 
## Qué es un archivo.so? 

Se utiliza para proporcionar acceso a bibliotecas compartidas a un programa determinado cuando se inician. (3) 
En este caso podemos utilizar un archivo C  a  un archivo.so y  esto  nos permite administrarlo con Python.
 

El archivo .so se puede crear de la siguiente manera:

En la terminal linux(Ubuntu) o en Visual Sudio Code ingresamos a su dirección donde se encuentra almacenado nuestro archivo.c
Posteriormente agregamos la palabra siguiente para que se genere nuestro archivo.so , anexando como ejemplo el programa en c que se llama algo y  para el nombre de nuestro archivo .so podemos escribir el mismo nombre  del archivo .c  u otro que se elija.


Lo podemos definir de la siguiente manera gcc funciona para archivos .c  y shared funciona para compartir,toma el archivo tipo  c y lo comvierte a un archivo  .so que se pueda leer con Python.
```makefile
gcc -fPIC -shared -o funcion.c funcion1.so  
 

  ``` 
 

## Programas  fundamentales c y python : 



## Ejemplo 1
Primero vamos hacer algo muy importante deseamos sumar dos numeros, podemos hacer la suma de a y b y lo hacemos  en el lenguaje de programación c buscando las librerias que me permitan usarlas  todas las funciones del mismo , en donde hacemos una función que permita almacenar cada una de las variables involucradas en la suma  y claro un return para después utilizar el valor de la función.

Podemos tomar en cuenta  al hacer el archivo.c que se almacene en la misma carpeta en donde vamos a generar cada uno de nuestros archivos .
Como podemos ver a continuación tenemos el archivo.c. te invito a utilizarlo para que puedas implementarlo como se muestra a continuación.

## Sumar dos números enteros (numerosenteros.c)

Primero vamos a buscar crear un programa que sume dos números en nuestro programa añadiendo las librerías fundamentales en c. 


Una de las características más importantes en el uso de sumar variables tenemos en consideracion la suma de las variables  a + b como variables enteras, el archivo se llama numerosenteros.c


La función se establece de acuerdo a la siguiente forma, primero vamos a agregar las librerías correspondientes a c de la siguiente manera.
```c 
#include <stdlib.h>// include library c.
#include <stdio.h> //include functions of the library  c.

 ``` 
Posteriormente agregamos el código correspondiente de la función que funciona con enteros.
La función realiza la operacion de sumar dos variables, la cual podemos determinarla con la variable sum, podemos ver que hace un return  del valor de nuestra función.
```c 
int suma(  int  a,  int b,  int sum){
sum = a + b;
//Posteriormente podemos agregar de manera compacta la suma con la variable sum , además de agregar el return para que regrese nuestra función de la 
 //siguiente manera.

return sum ;  
//return(sum);

}
 ```
Ahora tenemos nuestro  codigo generado. podemos ingresar en la terminal  para encontrar nuestro archivo , ahora bien cuando sabemos que estamos en la dirección correcta, vamos a generar nuestro archivo.so  como ejemplo podemos ver la siguiente forma.
podemos visualizar esta linea de comandos en la parte inferior  cuando ejecutamos un programa en el entorno visual estudio nosotros vamos a utilizar la parte donde dice terminal.
## Generar el archivo .so a partir de un programa numeros_enteros.c

Ahora bien podemos tener almacenado el valor de sum que nos ayuda para utilizarlo posteriormente en python.
Podemos encontrar en la parte inferior de el entorno de visual estudio las siguientes etiquetas en donde vamos a ingresar en la opcion  de terminal para ingresar a la ubicación de nuestro archivo en c para posteriormente generar nuestro archivo gcc como podemos ver a continuación.


PROBLEMS                    OUTPUT                    DEBUG CONSOLE                     TERMINAL                       PORTS

Después de  guardar y ejecutar tu archivo  en c se debe generar.so en  la terminal que se encuentra de la siguiente forma:
```Python
User :~/Path_to_your_files$ gcc- fPIC -shared -o  numerosenteros.so numerosenteros.c
```
De esa manera podemos ver que nuestro archivo.so se generó y podemos pasar al siguiente paso, utilizar python para extraer los datos, lo cual podemos ver a continuación en el siguiente archivo.


## Archivo  sumaenteros.py

Para abrir nuestro archivo  de suma de dos numeros enteros  en c necesitamos  utilizar  sumaenteros.py 
deacuerdo al siguiente código vamos a utilizarlo para administrar los datos , anteriormente pudimos observar  que  generamos un archivo.s, entonces ahora podemos cargar la ubicación del archivo.so e utilizarlo en python e ingresar el valor de cada una de las variables para posteriormente obtener la suma apartir de tener un código en c  y administrarlo con python, como podemos ver a continuación cada uno de los pasos utilizados en lenguaje de python.
```Python
#codigo que ayuda  para sumar dos numeros enteros desde la funcion de  numeros enteros
import ctypes as cl

```

Podemos importar ctypes, cuya biblioteca es útil para importar código que no sea de su origen.
Además accedemos a la dirección de nuestro file donde se encuentra almacenado nuestro archivo.so como podemos ver a continuación.
```Python
#Asignamos  el file  o el path de nuestro archivo .so

#Como en el ejemplo:
file = ("/pc/Desktop/carpeta/Archivo.so")  # Direction of the path.

```
Asignamos un nombre aleatorio, en donde se pueda  definir  numerosenteros.

Como en la siguiente asignación definiendo el file y añadiendo 	cl.CDLL para  poder utilizar la funcion por medio de ctypes.

```Python
numerosenteros=cl.CDLL(file)

```
#En el script python definimos el valor de nuestras variables.

#Cómo en el siguiente ejemplo para la suma de dos numeros enteros asiganmos un valor  tipo entero de la siguiente manera  en este caso podemos asignar un nombre a  cada una de las variables, en este caso las seleccionamos como a y b.
```Python

a = 8 #Assigment of variable a
b = 10

```
Vamos a imprimir con la función type para numeros enteros;como podemos ver en el ejemplo.
```Python

print(type(numerosenteros))  # print of the type of function.

```
Posteriormente definimos el archivo que tenemos cargado donde se encuentra toda esa sintaxis  del archivo donde tomamos solo la función suma con las variables correspondientes  asignadas con a y b.
De la siguiente manera:
```Python
print(numerosenteros.suma(a,b))#print the variables
```
De esta forma sumamos dos variables y podemos tener el resultado  que veremos  impreso en pantalla.

## Ejemplo 2
Podemos considerar para  realizar este programa primero hacer un programa en lenguaje c que pueda sumar dos numeros solo que  en este caso podemos implementar sumar  2 numeros flotantes, podemos implementar este código de la siguiente manera como podemos ver a continuación , eligiendo dos variables para  realizar una función que me permita sumar las dos variables como podemos observar en le programa suma_float.c.

##  sumar dos numeros flotantes(suma_float.c)
 

Posteriormente para el siguiente programa se va a generar de acuerdo a números flotantes por lo cual también adjuntamos las librerías correspondientes para suma de números flotantes.

 ```c 
#include <stdlib.h>// include library c.
#include <stdio.h> //include functions of the library  c.

 ``` 
 ```c 
//Agregamos ahora la función que nos va a permitir la suma  de dos numeros flotantes  realizandola de la siguiente manera:

 float suma(  float  a,  float b,  float sum){
 
``` 
Posteriormente podemos añadir la suma de los dos números flotantes, en este caso utilizamos una variable que se almacena como la suma de 2 variables tipo flotantes a y b  la cual se llama sum que va ayudar para almacenar  con la palabra return la sum.

 ```c 
sum = a + b;
``` 
```c 
//Por ultimo  agregamos la  variable return que nos permite regresar el valor de nuestra función 

return sum ;  
//return(sum);

}

 ```
## Generar el archivo .so a partir de un programa suma_float.c

Ahora bien podemos tener almacenado el valor de sum que nos ayuda para utilizarlo posteriormente en python.
Podemos encontrar en la parte inferior de el entorno de visual studio las siguientes etiquetas en donde vamos a ingresar en la opcion  de terminal para ingresar a la ubicación de nuestro archivo en c para posteriormente generar nuestro archivo gcc como podemos ver a continuación.

PROBLEMS                    OUTPUT                    DEBUG CONSOLE                     TERMINAL                       PORTS


Después de  guardar y ejecutar tu archivo  en c se debe generar.so en  la terminal que se encuentra de la siguiente forma:
```Python
User :~/Path_to_your_files$ gcc- fPIC -shared -o  suma_float.so suma_float.c
```
Para abrir nuestro archivo  de suma de dos numeros enteros  en c necesitamos  utilizar  suma_float.py 
deacuerdo al siguiente código.

 ## Archivo  suma_float.py
Ahora bien este archivo nos va ayudar para administrar  el programa que anteriormente realizamos en lenguaje  C , donde  se realizó una función para  obtener la suma de dos números flotantes, es ahora de llegar a administrarlo con python de la siguiente manera cargando el archivo.so de la dirección donde lo tenemos almacenado, para posteriormente asignar la función y el nombre que podemos elegir para nuestros datos y así paso por paso llegar a obtener la suma de los dos numeros flotantes.

```Python
#Ahora vamos a necesitar un programa  que se llama suma_float.
#Primero importamos ctypes una biblioteca fundamental para extraer datos.
import ctypes # import ctypes 
``` 
Después asignamos un nombre que nos permita recordar el archivo.

```Python
file =("/pc/Desktop/carpeta/Archivo.so")  # Direction of the path.
funcion2_suma=ctypes.CDLL(file)   # importar funcion2_suma de file
#Asignamos el valor de cada una de las variables de numeros flotantes.
a = 7.2200123  #Assigment of variable a
b = 10.25225  #Assigment of  variable b.
``` 

Vamos asignar una variable que nos permita extraer el archivo y asignar la función que deseamos sumar, ya que nos permitirá almacenar el valor de la funciòn que en este caso es suma.

```Python
n_suma = funcion2_suma.suma    #n_suma funcion2_suma. 

#Para posteriormente  con argtypes determinar el tipo de variables que van a ingresar a nuestro programa en este caso tipo flotantes.

n_suma.argtypes = [ctypes.c_float,ctypes.c_float] #n_suma argtypes
``` 

Ahora definimos que tipo de variables van a salir de nuestro programa de la siguiente forma, podemos encontrar que son tipo float razón por lo cual añadimos como se puede observar con la función de ctypes.
```Python
n_suma.restype = ctypes.c_float #toma la funcion de n_suma restype

#Por último imprimimos la suma de las dos variables.

print(n_suma(a,b))  #imprime la suma de los dos numeros de la funcion.
 ``` 
## Ejemplo 3

## Sumar dos numeros doubles(suma_doubles.c)
Podemos considerar sumar dos numeros doubles , entonces relizamos una función  que nos permita obtener la suma, en este caso podemos implemntarlo en c, sumamos los dos valores  y después con un return almacenamos el valor generado que en este caso  se considera con la  variable sum.
Tomamos en cuenta que  el programa en c va hacer quién va a realizar los calculos y python solo va adminstrar esos datos , entonces en este caso podemos encontrar que en c solo vamos a realizar la función, que podemos comenzar de la siguiente forma. 

Ahora podemos hacer una función que nos ayude a obtener la suma de  2 números doubles; primero añadimos las bibliotecas. 
```c 
#include <stdlib.h>// include library c.
#include <stdio.h> //include functions of the library  c.
```  
Agregamos nuevamente las instrucciones de nuestra función que va a sumar números doublés. 
Agregamos ahora la función que nos va a permitir la suma  de dos numeros flotantes  realizandola de la siguiente manera:
```c 
 double suma(  double  a,  double b,  double sum){

sum = a + b;//Posteriormente podemos añadir la suma de los dos números doubles. 

```  
Por último  agregamos la  variable return que nos permite regresar el valor de nuestra función 

 ```c 
return sum ;  
//return(sum);

}

 ```
## Generar el archivo .so a partir de un programa suma_doubles.c

Ahora bien podemos tener almacenado el valor de sum que nos ayuda para utilizarlo posteriormente en python.
Podemos encontrar en la parte inferior del entorno de visual estudio las siguientes etiquetas en donde vamos a ingresar en la opción  de terminal para ingresar a la ubicación de nuestro archivo en c para posteriormente generar nuestro archivo gcc como podemos ver a continuación.

PROBLEMS                    OUTPUT                    DEBUG CONSOLE                     TERMINAL                       PORTS

Después de  guardar y ejecutar tu archivo  en c se debe generar.so en  la terminal que se encuentra de la siguiente forma:
```Python
User :~/Path_to_your_files$ gcc- fPIC -shared -o  suma_doubles.so suma_doubles.c
```

Para abrir nuestro archivo  de suma de dos numeros enteros  en c necesitamos  utilizar  suma_doubles.py 
deacuerdo al siguiente código.
 ## Archivo  suma_doubles.py

```Python
#En el caso de la suma de numeros  tipo double podemos definir de la siguiente manera  importando la biblioteca ctypes.
#import ctypes # import ctypes with extension cl.

``` 

También podemos ver en el ejemplo  un file o un path de nuestro archivo de la siguiente manera.
```Python
file = ("/pc/Desktop/carpeta/Archivo.so")  # Direction of the path. # Direction of the path.

``` 
Asignamos un nombre a nuestra variable como la funcion2_suma  en donde vamos a cargar con ctypes el file.
```Python
suma_doubles = ctypes.CDLL(file)   # importar funcion2_suma de file
```
Asignamos el valor de cada una de las variables tipo double que vamos a sumar.
```Python
a = 7.22001231364165885  #Assigment of variable a
b = 10.2522564161451457   #Assigment of  variable b.

``` 
Asignamos otro nombre de la siguiente manera incorporando nuestra  variable funcion2_suma y  nuestra función que se llama  suma es el nombre   de una de la función que podemos encontrar en el programa en c, si cambia el nombre de la función  o añadimos otra función en donde se puede considerar de la siguiente forma.
```Python
n_suma = funcion2_suma.suma    #n_suma funcion2_suma. 
``` 
#Posteriormente definimos n_suma con argtypes en donde tenemos  2 variables  que vamos a sumar tipo doubles.
```Python
n_suma.argtypes = [ctypes.c_double ,ctypes.c_double] #n_suma argtypes
``` 
Después asignamos  el tipo variables que van a salir de nuestro programa esto con restype asignando que son variables tipo double.

```Python
n_suma.restype = ctypes.c_double  #toma la funcion de n_suma restype
``` 
#Por último imprimimos la suma de nuestras dos variables tipo doubles.
```Python
print(n_suma(a,b))  #imprime la suma de los dos numeros de la funcion.

 ``` 
## Ejemplo 4

## sumar dos arreglos  
Ahora vamos a comenzar realizando un programa que nos permita desarrollar  la suma de dos arreglos en c, por loc cual la suma la va  a realizar c y se va administrar con python, todos los valores se van a  proporcionar en python, pero c realizara todos los calculos de la suma de los dos arreglos. como podemos ver  en el primer codigo en c  como vamos generando un programa para permitirnos la suma de los dos arreglos.

## suma_arreglos_enteros.c

Ahora podemos  desarrollar un programa que nos ayude con un programa que nos permita la suma de dos arreglos de dimension 10.

Primero  agregamos las librerias correspondientes de la siguiente manera:
```c 
//program to do array add to vectors
#include <stdio.h> // libreria  que ayuda a funciones en c

#include <stdlib.h>// libreria para convertir un enero a cadena de caracteres.

``` 

Después añadimos una función que nos permita  determinar  los tipos de variables, en nuestro caso son variables tipo entero que dependen de la función sum_array, donde las dos variables tienen una dimensión de 10.
```c 
int sum_array (int a[10],int b[10]){ //  determina el tipo de funcion  in_suma de las varibales de los arreglos a y b
``` 
También podemos añadir una variable que es la que vamos a realizar para obtener el valor.
 ```c 
int resultado[10];

``` 
Después realizamos con dos for  dos ciclos  para poder realizar la suma de nuestros dos  arreglos  de la siguiente manera.
De esa forma podemos ver a  cada una de nuestras variables en el ciclo for que está definido, e inicia en cero. 
En donde definimos  el valor de n = 10, donde podemos  hacer un ciclo for que comienze en cero y sea menor que 10.
```c 
for (int i = 0; i < 10; i++) {  // realiza las iteraciones  de la suma de los dos arreglos, en unn ciclo for
	resultado[i] = a[i] + b[i];
}

``` 
```c 
for (int i = 0; i < 10; i++) {  // realiza un ciclo for  que empieza en cero pero es menor que 10 que imprime el resultado
	printf("%d ", resultado[i]);
	
 ``` 
Por último es muy importante agregar el return de nuestro resultado para posteriormente utilizarlo de la siguiente manera.
```c 

}
return resultado[10]; // regresa el resulado de las iteraciones
}
```
## Generar el archivo .so a partir de un programa suma_arreglos_enteros.c

Ahora bién podemos tener almacenado el valor de resultado que nos ayuda para utilizarlo posteriormente en python.
Podemos encontrar en la parte inferior de el entorno de visual estudio las siguientes etiquetas en donde vamos a ingresar en la opcion  de terminal para ingresar a la ubicación de nuestro archivo en c para posteriormente generar nuestro archivo gcc como podemos ver a continuación.

PROBLEMS                    OUTPUT                    DEBUG CONSOLE                     TERMINAL                       PORTS

Despues de  guardar y ejecutar tu archivo  en c se debe generar.so en  la terminal que se encuentra de la siguiente forma:
```Python
User :~/Path_to_your_files$ gcc- fPIC -shared -o  suma_arreglos_enteros.so suma_arreglos_enteros.c
```
## Archivo  suma_arreglos_enteros.py
Podemos considerar un archivo en python que suma dos arreglos tipo enteros, donde anteriormente definimos en un programa en c, ahora llega el turno para utilizar como vamos administrar nuestro archivo, en este archivo.py vamos administrar los datos de nuestra función  realizada anteriormente, vamos agregar dos arreglos tipo enteros empezando de la siguiente manera, primero necesitamos el archivo.so que generamos para utilizarlo ya  nos va ayudar a poder utilizar el archivo.so para abrirlo en python.
Para abrir nuestro archivo  de suma de dos numeros enteros  en c necesitamos  utilizar suma_arreglos_enteros .py 
deacuerdo al siguiente codigo.
```Python

#Para este caso de un arreglo con 10 valores podemos definir las bibliotecas de la siguiente manera importando numpy podemos definir cada una de #nuestras librerias de la siguiente manera.
import ctypes #importamos ctypes
import numpy as np   #importamos numpy
 ``` 
Podemos cargar la biblioteca de muchas maneras distinas una de ellas en cargando el archivo .so  que se encuentra en la misma biblioteca.
```Python
# Cargar la biblioteca compartida

#Por esta ocasión definimos el Path de nuestro archivo, la localización del archivo .so
file = ("/pc/Desktop/carpeta/Archivo.so")  # Direction of the path.
``` 
Aqui hay otro ejemplo de la dirección  de nuestro Path almacenado en otra dirección.
```Python
#suma_arreglos_enteros = ctypes.CDLL('./Archivo.so')
#Podemos definir un nombre para  cargar nuestro archivo mediante la función ctypes.
suma_arreglos_enteros =ctypes.CDLL(file) 
```
Definimos  los argumentos que tenemos en la función y también el tipo de arreglo c_int
```Python
#En este caso podemos definir un nombre llamado sum_array que define el nombre donde se encuentra almacendo nuestro file .
sum_array = suma_arreglos_enteros.sum_array
#Podemos definir los valores de entrada  con la función  argtypes tipo enteros
sum_array.argtypes = [np.ctypeslib.ndpointer(dtype=np.intc),np.ctypeslib.ndpointer(dtype=np.intc),
												np.ctypeslib.ndpointer(dtype=np.intc),ctypes.c_int]
```
Definimos cada una de los valores de cada  variable definidas como variables tipo int.
```Python
# arreglos  de la  funcion  a y b   con dtype con numpy   de  tipo enteros
a = np.array([-1, 7, 3, 4,4,4,5,6,8,6], dtype=np.intc)
b = np.array([5, 6, 7, 8,4,4,5,6,3,4], dtype=np.intc)

```
Obteniendo el resultado  indicando que son tipo int e indicando que son 10 argumentos.
```Python
resultado = np.zeros(10, dtype=np.intc)  #determina   la variable resultado con 10 caracteres.
```
Donde almacenamos el nombre de nuestra función e indicando los argumentos de la siguiente manera , e indicando los valores tipo int, e indicando el numero de argumentos con len(a).
Llamamos  a la función  que tenemos   almacenada de la función en c para imprimir el resultado.

Para abrir nuestro archivo  de suma de dos numeros enteros  en c necesitamos  utilizar Generator_array .py 
deacuerdo al siguiente codigo.
```Python
sum_array(a, b, resultado, len(a))#len (a) aplicada  a la funcion  ayuda a regresar el numero de elementos de numeros reales.

 ``` 
 ## Ejemplo 5

 ## Generator_array .c
Podemos realizar un código  en lenguaje en c  que le pusimos de nombre Generator_array ya que este código nos va a generar un conjunto de datos que dependen de los rangos que podemos definir en el programa, generandonos un conjunto de datos que siguen un cambio en dx, que en este caso podemos establecer pasos o cambios en numeros flotantes y también  definimos cunatos valores vamos a obtener.
Podemos como primer paso  añadir las librerias fundamentales  que podemos ver a continuación:

```c
#include <stdio.h> // libreria  que ayuda a funciones en c.

#include <stdlib.h>// libreria para convertir un entero a cadena de caracteres.
```
Posteriormente determinamos  nuestra función de la siguiente manera indicando que es un vector de arreglos.

```c
float*array_float_string(float X0, float Xn, int n){
 
//Vamos a  regresar el valor  float  de x con la función malloc
float*x = (float*)malloc((n + 1)*sizeof(float));
 ```
Podemos definir un  cambio dx  flotante de la siguiente manera.
```c
float dx =(Xn -X0)/(n+1);
for (int i =0; i<=n; i++){
//Existiera un cambio en nuestra función de acuerdo a delta de x, realizando la iteración en un ciclo for.

	x[i] = i*dx + X0;
}

//Regresamos el valor de X que vamos almacenar para posteriormente almacenarlo.
return x;

}
 ```
## Generar el archivo .so a partir de un programa Generator_array.c

Ahora bien podemos tener almacenado el valor de x que nos ayuda para utilizarlo posteriormente en python.
Podemos encontrar en la parte inferior de el entorno de visual estudio las siguientes etiquetas en donde vamos a ingresar en la opcion  de terminal para ingresar a la ubicación de nuestro archivo en c para posteriormente generar nuestro archivo gcc como podemos ver a continuación.

PROBLEMS                    OUTPUT                    DEBUG CONSOLE                     TERMINAL                       PORTS

Después de  guardar y ejecutar tu archivo  en c se debe generar.so en  la terminal que se encuentra de la siguiente forma:
```Python
User :~/Path_to_your_files$ gcc- fPIC -shared -o  Generator_array.so Generator_array.c
```

Para cargar  en c ,el programa que se llama generator_array primero podemos importar las dos librerias fundamentales para extraer datos en Python de la siguiente manera.

## Generator_array.py

Podemos implementar un código en python que nos permita administrar  el archivo en c que realizamos anteriormente, podemos observar algo muy importante en cada uno de los archivos en python que no en todos utilizamos numpy como podemos ver que en algunos casos si , siempre primer cargando la ubicación donde se encuentra almacenado nuestro archivo.so y en cada una de ellas utilizamos ctypes ya  que nos permite realizar la dinamica de interacción de las funciónes de c y en python agregar los datos y administrarlos.

```Python
import ctypes  #importamos ctypes  
import numpy as np #importamos numpy que nos facilita la conversion de datos


```
Posteriormente cargamos el archivo o Path  donde podemos encontrar nuestro archivo .so como podemos ver en el ejemplo.
Cargar la biblioteca compartida.
```Python
file = ("/pc/Desktop/carpeta/Archivo.so")  # Direction of the path.
```
Después necesitamos  asignar un nombre para cargar nuestro archivo a ctypes de la siguiente manera , en ese caso asignamos con el nombre Generator_array.py sin embargo puede cambiar su nombre.
```Python
Generator_array = ctypes.CDLL(file)  #carga la el archivo file  a ctypes.

```
Las variables que vamos asignar para el funcionamiento de nuestro programa se desarrollan de la siguiente manera aunque las variables pueden determinarse al inicio o al final de nuestro programa.
Dentro de algunas recomendaciones podemos destacar el numero de iteraciones que  depende de la memoria del computador, en este caso se realizo la iteración y para que funcionará de manera optima llego hasta un maximo  de  100000000.
Algunos ejemplos de asignación de valores  a las variables se pueden mostrar a continuación:

```Python
x0 = 1.512871423416543
xn = 2.00111     #recuerda que  xn debe ser mayor que x0
n = 100000000  #numeros enteros en el ciclo for para funcionar de manera optima maximo 100000000
# añadimos el formato de nuestras variables dos flotantes y un entero

```
Podemos definir un conjunto de variables tipo flotantes de la siguiente manera;primero vamos asignar  la variable que carga nuestro archivo posteriormente vamos a indicar la función que vamos a tomar como en el ejemplo.
```Python
Generator_array.array_float_string.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_int]
```
Vamos a establecer el tipo de salida como variable  tipo float de  la siguiente manera, igual indicando con la función restype.
```Python
Generator_array.array_float_string.restype = ctypes.POINTER(ctypes.c_float)#salida de nuestro arreglo 
#de numeros flotantes
 ``` 
Vamos a definir una función con la palabra def  en donde podemos indicar  sus variables.
```Python
def array_float_string(x0, xn, n):
	#llamamos la funcion de nuestra programa escrito en c con sus varibles
```
```Python
#Ahora bien podemos definir el arreglo de Array_sring1 y de la  función definida anteriormente.	
arreglo = Generator_array.array_float_string(x0, xn, n)
```
Un paso muy importante es apoyarnos de la libreria de numpy  en donde definimos un nombre que defina las iteraciónes de nuestros  arreglos.
```Python
#utilizamos el arreglo de ctypes a numpy  que vaya iterando en el rango de (n+1)
	convertir_arreglo= np.array([arreglo[i] for i in range(n+1)])
```
De esta función vamos a realizar un return para posteriormente utilizarla.
```Python
	#hacemos un return de la funcion 
	return convertir_arreglo
```
Ahora vamos a definir la palabra que realizamos return como una función que contenga las variables.
```Python
#convertirmos e imprimimos la función.
convertir_arreglo = array_float_string(x0, xn, n)
```
Por Último imprimimos convertir_arreglo y podemos definir  una cadena de  soluciónes en un arreglo que va determinado por el rango que indicamos y el número de iteraciónes o de resultados depende del paso que podemos determinar en c.
```Python
print( convertir_arreglo)
 
 ``` 
## Makefile 

Para el caso del makefile tenemos que escribir el archivo de la siguiente forma para posteriormente,podemos indicar de manera formal que  nuestro archivo  se pueda generar de manera automatica de la siguiente manera.
Eligiendo el tipo de compilador  que en nuestro caso es gcc por que va a tomar archivos tipo c.
```makefile 
SHELL := /bin/bash
c_compiler = gcc
``` 
Añadiendo una leyenda en ese caso funcion2_suma que genera archivo.o .
En donde toma los 3 archivos  genera archivo .so y toma el archivo .c y el archivo.h
```makefile 
funcion2_suma : funcion_array.o
	gcc -fPIC -shared -o  funcion3_array.so  funcion_array.c funcion_array.h

``` 
Por último limpia los archivos creados .o con la función rm y podemos abrirlo con la función make.
```makefile 
clear:
	rm funcion_array.o
```
Para posteriormente ejectutar nuestro programa con la función cp  y en la terminal solo con la palabra Makefile toda la lista de comandos se puede ejecutar de manera automatica.
## Conclusión: 
El programa funcionara de manera óptima ,el gcc funcionara y podrás extraer los archivos de la dirección de tu programa  mencionando el tipo de documento realizando  un archivo compartido .so, de manera mas general,llegamos a  generar un archivo .c  que sume dos numeros de tipo float, int, double  y se puedan extraer con Python utilizando la biblioteca ctypes, además puedes hacer la suma de arreglos y llegar a generar un vector de arreglos definiendo un rango de iteraciónes y todo ello se pudo abrir con Python  utilizando el archivo .so.

Nota* para el caso de hipervínculos en markdown  no se pudo con un solo click  que cada hipervínculo se abriera en otra pestaña  debido a la naturaleza de archivos.md por esa razón se  implementó una opción  dando click izquierdo en cada hipervínculo mostrara la opción para abrirlo, muestra opción como  open link in new tab, open link in new window y open link in incógnito window recomendamos open link in new tab.

## Fuentes consultadas: 


1) https://visualstudio.microsoft.com/.

2) https://www.file-extension.info/es/format/so

3) https://www.ionos.mx/digitalguide/paginas-web/desarrollo-web/programacion-con-c/
   
4) https://www.python.org/downloads/.

5) https://developer.mozilla.org/es/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks
   
6) https://www.gnu.org/software/make/manual/make.html


