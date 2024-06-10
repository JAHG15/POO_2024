"""
list(Array)
son colecciones o conjunto de datos/valores bajo
un mismo nombre, para acceder a los valores se
hace con un indice numerico.
Nota:Sus valores si son modificables.
La lista es una coleccion ordenada y modificable. Permite miembros
duplicados.
"""
#Ejemplo 1 crear una lista con valores numericos enteros e imprimir la lista
"""
numeros=[23,34];
# print(numeros);
#Recorrer la lista con un for
for i in numeros:
    print(i);
#Recorrer la lista con un while
i=0;
while i<len(numeros):
    print(numeros[i]);
    i+=1
"""
#Ejemplo 1 crear una lista de palabras, posteriormente ingresar una palabra
#para buscar la coincidencia en la lista e indicar si aparece la palabra y en que posicion
#en caso contrario indicar una sola vez si no la encontro

# palabras=["hola","2024","10,13","True"];
# palabra_buscar=input("Ingresa la palabra buscar: ");
#Si palabra buscar esta en la lista palabras, hace el ciclo for, sino imprime "No se encontro la palabra"
# if palabra_buscar in palabras:
#     for i in palabras:
#         if palabra_buscar==i:
#             print(f"La palabra {palabra_buscar} se encontro en la posicion {palabras.index(i)}")
# else:
#     print(f"No se encontro la palabra")

# palabras=["hola","2024","10,13","True"];
# palabra_buscar=input("Ingresa la palabra buscar: ");
#Ejemplo 2
# i=0
# if palabra_buscar in palabras:
#     while i<len(palabras):
#         if palabra_buscar==palabras[i]:
#             print(f"La palabra {palabra_buscar} se encontro en la posicion {i}")
#         i+=1
# else:
#     print(f"No se encontro la palabra")

#Ejemplo 3 crear una lista multilinea (Matriz) para crear una agenda telefonica

# agenda=[
#     ["Carlos",6181234567],
#     ["Fernando",6182334567],
#     ["Matias",6691112233],
#     ["Juan Polainas",6182332345]
# ];

# print(agenda);
# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}");








    


