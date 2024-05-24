#sitolica entre 100 y 120
#diastolica 60 a 80
contador=0;
while True: 
    nombre=str(input("Ingrese su nombre: "));
    tipo_sangre=str(input("Ingrese su tipo de sangre: "));
    sistolica1=float(input("Ingrese la medicion sistolica 1:"));
    diastolica1=float(input("Ingrese la medicion diastolica 1:"));
    sistolica2=float(input("Ingrese la medicion sistolica 2:"));
    diastolica2=float(input("Ingrese la medicion diastolica 2:"));
    sistolica3=float(input("Ingrese la medicion sistolica 3:"));
    diastolica3=float(input("Ingrese la medicion diastolica 3:"));
    final=float(input("Ingrese la medicion final del dia: "));
    print(f"Nombre: {nombre}");
    print(f"Tipo de sangre: {tipo_sangre}");
    promedio_sistolica=(sistolica1+sistolica2+sistolica3)/3;
    print(f"El promedio de la presion sistolica es:  {promedio_sistolica}");
    promedio_diastolica=(diastolica1+diastolica2+diastolica3)/3;
    print(f"El promedio de la presion diastolica es:  {promedio_diastolica}");
    presion_final=(promedio_sistolica+promedio_diastolica+final)/3;
    print(f"La presion final es: {presion_final}");
    if promedio_sistolica <=120 and promedio_diastolica<=80:
        print("La presion es normal");  
    contador+=1;
    while True:
        respuesta=str((input("Desea capturar otro paciente? SI/NO: "))).upper();
        if respuesta=="SI" or respuesta=="NO":
            break
        else:
            print("No es una opcion valida");
       
    if respuesta=="NO":
        print(f"Numero de pacientes capturados: {contador}");
    break


    


