"""
Ejemplo 4.- Crear un programa que permita gestionar(Administrar) peliculas, colocas un menu
de opciones para agregar,remover,consultar peliculas.
Notas:
1- Utilizar funciones y mandar llamar desde otro archivo
2- Utilizar listas para almacenar los nombres de peliculas
"""
peliculas=[]
#Funcion 1
def InsertarPeliculas():
        nombre=input("Ingrese el nombre de la pelicula: ") 
        peliculas.append(nombre)
        print("La pelicula fue agregada con exito!")

#Funcion 2
def EliminarPeliculas():
      nombre=input("Ingrese el nombre de la pelicula: ")
      if nombre in peliculas:
            respuesta=input("Esta seguro de borrar esta pelicula? SI/NO").upper()
            if respuesta=="SI":
                  posicion=peliculas.index(nombre)
                  peliculas.pop(posicion)
                  print("La pelicula fue eliminada con exito!")
            elif respuesta=="NO":
                  print(f"Para volver al menu principal")
      else:
            print("La pelicula no se encuentra en la lista!")   

#Funcion 3
def Consultar():
      print(f"Las peliculas disponibles son: {peliculas}")

#Funcion 4
def Actualizar():
      nombre=input("Ingrese el nombre de la pelicula: ")
      if nombre in peliculas:
            posicion=peliculas.index(nombre)
            nuevo_nombre=input("Ingrese el nuevo nombre de la pelicula: ")
            peliculas[posicion]=nuevo_nombre
            print("La pelicula fue cambiada con exito!")
      else:
            print("La pelicula no se encuentra en la lista!")       

#Funcion 5
def EspereTecla():
    print("Oprima cuaquier tecla para continuar");
    input();

#Funcion 6
def Vaciar():
     peliculas.clear()
     print(f"La lista fue vaciada correctamente: {peliculas}")
#Funcion 7
def Buscar():
      nombre=input("Ingrese el nombre de la pelicula: ")
      if nombre in peliculas:
            print("La pelicula se encuentra en la lista!")
      else:
            print("La pelicula no se encuentra en la lista!")   


"""
Funciones calculadora
"""
def solicitarNumeros():
    #global n1,n2
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))
    return n1,n2

def solicitarNumeros2():
    #global n1,n2
    n1=int(input("Numero # 1:"))
    return n1

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
        return f"{n1}/{n2}={n1/n2}"
    elif opcion=="5" or opcion=="^" or opcion=="POTENCIA":
         
         return f"{n1}^{n2}={n1**n2}"

def EspereTecla():
    print("Oprima cuaquier tecla para continuar");
    input();
