lista=[]
if len(lista)<=0:
    while True:
        agregar=input("Ingrese el elemento a agregar: ").upper()
        lista.append(agregar)
        respuesta=input("Desea agregar otro elemento? SI/NO ").upper()

        if respuesta=="NO":
            break

    print(f"La lista es: {lista}")
else:
    print("La lista ya tiene contenido")
    