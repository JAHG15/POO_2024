# Ciclo for es una estructura iterativa que se ejecuta X veces

# Sintaxis
# for variable in elemento_iterable (lsita,rango,etc):
# bloque de instrucciones

#Ejemplo 1 crea un programa que imprima en pantalla 5 el @
for contador in range (1,6):
    print("@");

#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5 y los sume y al final imprima la suma
acumulador=0;
for contador in range (1,6):
    print(contador);
    acumulador=acumulador+contador;

print(f"La suma es: {acumulador}");
#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuario desee

numero=int(input("Ingresa un numero: "));
multi=0;
for i in range (1,11):
    multi=i*numero;
    print(f"{numero} X {i} = {multi} ");