contador=0;
contador1=0;
for i in range (1,16):
    calificacion=float(input("Ingrese la calificacion: "));
    if calificacion>=80:
        contador+=1;
    else:
        if calificacion<80:
            contador1+=1;

print(f"Total de alumnos aprobados: {contador}");
print(f"Total de alumnos reprobados: {contador1}");



                