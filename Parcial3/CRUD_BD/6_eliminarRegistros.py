from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="delete from clientes where id=1"
    micursor.execute(sql)
    #Es necesario ejecutar el commit, para que finalice el SQL con exito.
    conexion.commit()
except  Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print ("Ocurrio un error porfavor vuelva a intentar mas tarde")
else:
    print("Registro eliminado exitosamente")