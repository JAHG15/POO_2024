numero1=int(input("Ingrese un numero: "));
numero2=int(input("Ingrese un numero: "));

for i in range (numero1,numero2):
    numero1+=1;
    divi=numero1%2;
    if divi==1:
        print(numero1)
