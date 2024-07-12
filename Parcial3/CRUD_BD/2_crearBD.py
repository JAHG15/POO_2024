import mysql.connector
#Conexion con la BD de MYSQL
try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    ) 
    #Crear un objeto nuevo de tipo cursor
    micursor=conexion.cursor()
    sql="CREATE DATABASE bd_python"
    micursor.execute(sql)
except  Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print ("Ocurrio un error porfavor vuelva a intentar mas tarde")
else:
    print(f"Se creo la base datos exitosamente")
    micursor.execute("SHOW DATABASES")
    for x in micursor:
        print(x)

