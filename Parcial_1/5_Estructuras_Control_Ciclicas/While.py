# Ciclo while es una estructura iterativa que se ejecuta X veces siempre y cuando
#la condicion se cumpla y se seguira ejecutando tantas veces como sea
#True la condicion

# Sintaxis
# while condicion:
# bloque de instrucciones

#Ejemplo 1 crea un programa que imprima en pantalla 5 el @
contador=1;
while contador<=5:
    print("@");
    contador+=1;

#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5 y los sume y al final imprima la suma
acumulador=0;
while contador<=5:
    print(contador);
    acumulador+=contador;
    contador+=1;

print(f"La suma es: {acumulador}");

#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuario desee

numero=int(input("Ingresa un numero: "));
i=1;
multi=0;
while i <=10:
    multi=i*numero;
    print(f"{numero} X {i} = {multi} ");
    i+=1;
    