import ctypes #importamos ctypes
import numpy as np   #importamos numpy

# Cargar la biblioteca compartida
#funcion_array = ctypes.CDLL('./funcion_array.so')
file = ("/home/jinzo/Desktop/Victorrivera2__NESCGLE/victor_fluidos/nueva1/files_python_c/SRC/Ejemplo4/suma_arreglos_enteros.so")  # Direction of the path
#file = ("/home/fluidos/fluidos_structures/funcion2_array.so")  # Direction of the path.
suma_arreglos_enteros=ctypes.CDLL(file) 

# Definimos  los argumentos que tenemos en la funcion y tambien el tipo de arreglo c_int
sum_array = suma_arreglos_enteros.sum_array
sum_array.argtypes = [np.ctypeslib.ndpointer(dtype=np.intc),np.ctypeslib.ndpointer(dtype=np.intc),
												np.ctypeslib.ndpointer(dtype=np.intc),ctypes.c_int]

# arreglos  de la  funcion  a y b   con dtype con numpy   de  tipo enteros
a = np.array([-1, 7, 3, 4,4,4,5,6,8,6], dtype=np.intc)
b = np.array([5, 6, 7, 8,4,4,5,6,3,4], dtype=np.intc)
resultado = np.zeros(10, dtype=np.intc)  #determina   la variable resultado con 10 caracteres

#  Llamamos  a la función  que tenemos   almacenada de la funcion en c para imprimir el resultado
sum_array(a, b, resultado, len(a))#len (a) aplicada  a la funcion  ayuda a regresar el numero de elemenyos de numeros reales.
