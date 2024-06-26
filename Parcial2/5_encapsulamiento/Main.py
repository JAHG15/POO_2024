from coches import *


print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)

# coche1.GetInfo()


# print("Objeto 2")
# coche2=Coches("Azul","Nissan","2020",180,150,6)

# coche2.GetInfo()

#Implementar el encapsulamiento o visibilidad
print (coche1.atributo_publico)
#print (coche1.__atributo_privado)#Esto no es posible
print (coche1.MetodoPublico())
# coche1.__MetodoPrivado()#Esto no es posible
coche1.getMetodoPublico() 