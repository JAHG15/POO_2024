numero1=float(input("Ingrese un numero: "));
numero2=float(input("Ingrese un numero: "));

respuesta=input("Ingrese la operacion que desea realizar (suma,resta,multiplicacion,division): ").lower();
if respuesta=="suma":
    suma=numero1+numero2;
    print(f"El resultado es: {suma}");
elif respuesta=="resta":
    resta=numero1-numero2;
    print(f"El resultado es: {resta}");
elif respuesta=="multiplicacion":
    multiplicacion=numero1*numero2;
    print(f"El resultado es: {multiplicacion}");
elif respuesta=="division":
    division=numero1/numero2;
    print(f"El resultado es: {division}");