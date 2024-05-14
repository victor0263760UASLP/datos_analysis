import ctypes  #importamos ctypes  
import numpy as np #importamos numpy que nos facilita la conversion de datos

# Cargar la biblioteca compartida
file =("/home/jinzo/Desktop/Victorrivera2__NESCGLE/victor_fluidos/nueva1/files_python_c/SRC/Ejemplo5/Generator_array.so")
#file =("/home/fluidos/Victorrivera2__NESCGLE/victor_fluidos/nueva1/Array_string1.so")
Generator_array= ctypes.CDLL(file)  #carga la el archivo file  a ctypes.
x0 = 1.512871423416543
xn = 2.00111     #recuerda que  xn debe ser mayor que x0
n = 100000000  #numeros enteros en el ciclo for para funcionar de manera optima maximo 100000000
# añadimos el formato de nuestras variables dos flotantes y un entero
Generator_array.array_float_string.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_int]
Generator_array.array_float_string.restype = ctypes.POINTER(ctypes.c_float)#salida de nuestro arreglo 
#de numeros flotantes

def array_float_string(x0, xn, n):
	#llamamos la funcion de nuestra programa escrito en c con sus variables
	arreglo = Generator_array.array_float_string(x0, xn, n)
	
	#utilizamos el arreglo de ctypes a numpy  que vaya ierando en el rango de (n+1)
	convertir_arreglo= np.array([arreglo[i] for i in range(n+1)])

	#hacemos un return de la funcion 
	return convertir_arreglo

#convertirmos e imprimimos la funcion
convertir_arreglo = array_float_string(x0, xn, n)
print( convertir_arreglo)


