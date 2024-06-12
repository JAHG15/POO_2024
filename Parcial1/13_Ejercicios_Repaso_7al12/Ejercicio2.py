lista=[]
for i in range (121):
    elemento=input("Ingrese el elemento a agregar: ")
    lista.append(elemento)
print(f"Los elementos de la lista son: {lista}")
# print(lista)
while len(lista)<120:
    elemento=input("Ingrese el elemento a agregar: ")
    lista.append(elemento)

print(f"Los elementos de la lista son: {lista}")

