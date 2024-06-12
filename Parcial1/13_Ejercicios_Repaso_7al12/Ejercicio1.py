numeros=[1,2,3,4,5,6,7,8]

def RecorrerLista():
    for i in numeros:
        print(i)
    print("La lista fue recorrida correctamente")

def Ordenarla():
    numeros.sort()
    print (numeros)

def Longitud():
    longitud=len(numeros)
    print(f"La longitud de la lista es: {longitud}")

def BuscarElementos():
    elemento=int(input("Ingrese el numero a buscar: "))
    posicion=numeros.index(elemento)
    print(f"El elemento fue encontrado en la posicion: {posicion}")

print("\n\t..::: Ejercicio 1 :::... \n 1.- Recorrer la lista \n 2.- Ordenarla \n 3.-Ver la longitud \n 4.- Buscar un elemento")
respuesta=input("Ingrese una opcion: ")
if respuesta=="1":
    RecorrerLista()
elif respuesta=="2":
    Ordenarla()
elif respuesta=="3":
    Longitud()
elif respuesta=="4":
    BuscarElementos()
    




