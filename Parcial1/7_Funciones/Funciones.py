"""
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular
como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutilizar con el simple
hecho de invocarla es decir mandarla llamar

Sintaxis:

def nombredeMifuncion(parametris):
    bloque o conjunto de instrucciones

nombredeMifuncion(parametros)

Las funciones pueden ser de 4 tipos
1.- Funciones que no recibe parametros y no regresa valor
2.- Funcion que no recibe parametros y regresa valor
3.- Funcion que recibe parametros y no regresa valor
4.- Funcion que recibe parametros y regresa valor
"""

# #1.- Funcion que no recibe parametros y no regresa valor
# def sumaNumero1():
#     n1=int(input("Numero # 1: "))
#     n2=int(input("Numero # 2: "))
#     suma=n1+n2
#     print(f"{n1}+{n2}={suma}")

# sumaNumero1()

#2.- Funcion que no recibe parametros y regresa valor
# def sumaNumero2():
#     n1=int(input("Numero # 1: "))
#     n2=int(input("Numero # 2: "))
#     return f"{n1}+{n2}={n1+n2}"

# print(sumaNumero2())

#3.- Funcion que recibe parametros y no regresa valor
# def sumaNumero3(n1,n2):
#     print(f"{n1}+{n2}={n1+n2}")

# n1=int(input("Numero # 1: "))
# n2=int(input("Numero # 2: "))
# sumaNumero3(n1,n2)

#4.- Funcion que recibe parametros y regresa valor
# def sumaNumero4(n1,n2):
#     return f"{n1}+{n2}={n1+n2}"

# n1=int(input("Numero # 1: "))
# n2=int(input("Numero # 2: "))
# print(sumaNumero4(n1,n2))

"""
Crear un programa que solicite a traves de una funcion 
la siguiente informacion: 
Nombre, estatura,tipo de sangre, utilizar los 4 tipos de funciones.
"""
# def DatosPaciente1():
#     nombre=input("Ingrese el nombre del paciente: ");
#     edad=input("Ingrese la edad del paciente: ");
#     estatura=input("Ingrese la estaura: ");
#     tipo_sangre=input("Ingrese el tipo de sangre : ");
#     print(f"{nombre},{edad},{estatura},{tipo_sangre}");

# DatosPaciente1();
    
# def DatosPaciente2():
#     nombre=input("Ingrese el nombre del paciente: ");
#     edad=input("Ingrese la edad del paciente: ");
#     estatura=input("Ingrese la estaura: ");       
#     tipo_sangre=input("Ingrese el tipo de sangre : ");
#     return(f"{nombre},{edad},{estatura},{tipo_sangre}");
# print(DatosPaciente2());

# def DatosPaciente3(nombre,edad,estatura,tipo_sangre):
#     print(f"{nombre},{edad},{estatura},{tipo_sangre}");

# nombre=input("Ingrese el nombre del paciente: ");
# edad=input("Ingrese la edad del paciente: ");
# estatura=input("Ingrese la estaura: ");       
# tipo_sangre=input("Ingrese el tipo de sangre : ");

# DatosPaciente3(nombre,edad,estatura,tipo_sangre);

def DatosPaciente4(nombre,edad,estatura,tipo_sangre):
    return(f"{nombre},{edad},{estatura},{tipo_sangre}");

nombre=input("Ingrese el nombre del paciente: ");
edad=input("Ingrese la edad del paciente: ");
estatura=input("Ingrese la estaura: ");       
tipo_sangre=input("Ingrese el tipo de sangre : ");

print(DatosPaciente4(nombre,edad,estatura,tipo_sangre));
