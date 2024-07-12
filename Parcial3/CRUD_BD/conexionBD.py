import mysql.connector
#Conexion con la BD de MYSQL
try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_python"
    ) 
except  Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print ("Ocurrio un error porfavor vuelva a intentar mas tarde")


#Verificar la conexion es correcta



