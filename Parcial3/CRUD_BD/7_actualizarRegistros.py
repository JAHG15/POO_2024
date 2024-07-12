from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="update clientes set direccion='col.del maestro' where id=2"
    micursor.execute(sql)
    #Es necesario ejecutar el commit, para que finalice el SQL con exito.
    conexion.commit()
except  Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print ("Ocurrio un error porfavor vuelva a intentar mas tarde")
else:
    print("Registro actualizado exitosamente")