from conexionBD import *
try:
    micursor=conexion.cursor()
    sql="SELECT * FROM clientes"
    micursor.execute(sql)
    resultados=micursor.fetchall()
    for fila in resultados:
        print (f"Id: {fila[0]}\nNombre: {fila[1]}\nDireccion: {fila[2]}\nTelefono: {fila[3]}\n")
except  Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print ("Ocurrio un error porfavor vuelva a intentar mas tarde")
else:
    print("Registros consultados exitosamente")