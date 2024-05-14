import ctypes # import ctypes with extension cl.

file = ("/home/jinzo/Desktop/Victorrivera2__NESCGLE/victor_fluidos/nueva1/files_python_c/SRC/Ejemplo2/suma_float.so")  # Direction of the path.
funcion2_suma=ctypes.CDLL(file)   # importar funcion2_suma de file

 #funcion2_suma= ctypes.CDLL("/home/jinzo/Desktop/Victorrivera__NESCGLE/victor_fluidos/nueva1/funcion2_suma.so")  # Direction of the path.
#funcion2_suma=cl.CDLL(file)  #Add the file path in CDLL with cl.
#funcion2_suma.argtypes=[ctypes.c_float,ctypes.c_float]

#d=(c_double *1)(4.23)
#numpy_d=array(d)
#numpy_d.dtype
#dtype(’float64’)
#numpy_d/1.35
#array([ 3.13333333])
#funcion2_suma.printf.argtypes=[a_float, b_float]

a = 7.22001231364165885261456154715154587498461465415747487946535125415313514   #Assigment of variable a
b = 10.2522564161451457145714515415741578144751581487549746165116161651561541   #Assigment of  variable b.

n_suma = funcion2_suma.suma    #n_suma funcion2_suma. 
n_suma.argtypes = [ctypes.c_float,ctypes.c_float] #n_suma argtypes
 #n_suma.argtypes =[ ctypes.c_float, ctypes.c_float]
 #n_suma.restype = ctypes.c_float
n_suma.restype = ctypes.c_float #toma la funcion de n_suma restype

print(n_suma(a,b))  #imprime la suma de los dos numeros de la funcion.

#print(type(funcion2_suma))  # print of the type of function.


#print(funcion2_suma.suma(a,b))#print the variables a ,b of the function2_suma with depend of the program in lenguage.

