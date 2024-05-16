"""
Existe una estructura de condicion llamda "if"
la cual evalua una condicion para econtrar el valor "True" y si se cumple
la condicion se ejecuta la linea o lineas codigo

Tienes 4 variantes del if
1.- if simple
2.-if compuesto
3.- if anidado
4.-elif
"""
"""
#If simple
color=input("Ingresa un color: ");
if color=="rojo":
    print("Soy el color rojo");

#if compuesto
color=input("Ingresa un color: ");
if color=="rojo":
    print("Soy el color rojo");
else:
    print("No soy el color rojo soy otra cosa");

#if anidado
color=input("Ingresa un color: ");
if color=="rojo":
    print("Soy el color rojo");
    if color!="rojo":
        print("No soy el color rojo");
else:
    print("No soy el color rojo soy otra cosa");

#if y elif
if color=="rojo":
    print("Soy el color rojo");
elif color=="amarillo":
    print("Soy el color amarillo");
elif color=="azul":
     print("Soy el color azul");
elif color=="morado":
     print("Soy el color morado");
else:
     print("No soy ningun color de los anteriores");
"""

#Crear un programa que solicite el numero de la semana 
#e imprima en pantalla el numero de la semana

dia_semana=int(input("Ingrese el dia de la semana: "));
if dia_semana==1:
    print("Lunes");
elif dia_semana==2:
    print("Martes");
elif dia_semana==3:
    print("Miercoles");
elif dia_semana==4:
    print("Jueves");
elif dia_semana==5:
    print("Viernes");
elif dia_semana==6:
    print("Sabado");
elif dia_semana==7:
    print("Domingo");
else:
    print("No corresponde a ningun dia de la semana");
