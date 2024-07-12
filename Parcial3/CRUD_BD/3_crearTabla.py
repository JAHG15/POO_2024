from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="CREATE TABLE clientes(id int primary key auto_increment, nombre varchar (60), direccion varchar (120), telefono varchar (10))"
    micursor.execute(sql)
except  Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print ("Ocurrio un error porfavor vuelva a intentar mas tarde")
else:
    print("Se creo la tabla exitosamente")