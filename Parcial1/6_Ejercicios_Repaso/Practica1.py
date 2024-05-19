while True:
    nombre=str(input("Ingrese el nombre del articulo: "));
    articulo=float(input("Ingrese el precio del articulo: "));
    iva=articulo*0.16;
    total_pagar=iva+articulo;
    print(f"Articulo: {nombre}\nTotal a pagar: ${total_pagar}");
    
    while True:
        respuesta=input("Desea capturar otro articulo? SI/NO: ") .upper();
        if respuesta=="SI" or respuesta=="NO":
            break
        else:
            print("La opcion no es valida");
        
    if respuesta=="NO":
        break
