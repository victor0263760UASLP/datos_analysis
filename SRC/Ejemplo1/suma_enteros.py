

#codigo que ayuda  para sumar dos numeros enteros desde la funcion de  numeros enteros
import ctypes as cl



file = ("/home/jinzo/Desktop/Victorrivera__NESCGLE/victor_fluidos/nueva1/numerosenteros.so")  # Direction of the path.


numerosenteros=cl.CDLL(file)



a = 8 #Assigment of variable a
b = 10



print(type(numerosenteros))  # print of the type of function.


print(numerosenteros.suma(a,b))#print the variab