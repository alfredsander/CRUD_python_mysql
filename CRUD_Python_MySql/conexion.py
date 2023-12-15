import mysql.connector

class Cconexion:
    
    def conexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root',
                                               password='123456789',
                                               host='127.0.0.1',
                                               database='clientesdb',
                                               port='3306')
            print("conexion correcta")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos, error: {}".format(error))
            conexion.close()
    conexionBaseDeDatos()
