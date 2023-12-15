from conexion import *

class CClientes:
    
    def MostrarClientes():
        try:
            conexion = Cconexion.conexionBaseDeDatos()
            cursor = conexion.cursor()
            cursor.execute("select * from usuarios;")
            datos = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return datos

        except mysql.connector.Error as error:
            print("Error al mostrar datos, error: {}".format(error))
        

    def IngresarClientes(nombres,apellidos,sexo):

        try:
            conexion = Cconexion.conexionBaseDeDatos()
            cursor = conexion.cursor()
            sql = "insert into usuarios values(null,%s,%s,%s);"
            
            valores = (nombres,apellidos,sexo) 
            cursor.execute(sql,valores)
            conexion.commit()
            print(cursor.rowcount,"Datos ingresados correctamente")
            conexion.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de datos, error: {}".format(error))

    def EliminarClientes(idUsuario):

        try:
            conexion = Cconexion.conexionBaseDeDatos()
            cursor = conexion.cursor()
            sql = "delete from usuarios where usuarios.id = %s;"
            
            valores = (idUsuario,) 
            cursor.execute(sql,valores)
            conexion.commit()
            print(cursor.rowcount,"Registro Eliminado")
            conexion.close()

        except mysql.connector.Error as error:
            print("Error de eliminar datos, error: {}".format(error))

    def ModificarClientes(idUsuario,nombres,apellidos,sexo):

        try:
            conexion = Cconexion.conexionBaseDeDatos()
            cursor = conexion.cursor()
            sql = "update usuarios set usuarios.nombre = %s, usuarios.apellidos = %s, usuarios.sexo = %s where usuarios.id = %s;"
            
            valores = (nombres,apellidos,sexo,idUsuario) 
            cursor.execute(sql,valores)
            conexion.commit()
            print(cursor.rowcount,"Registro Actualizado")
            conexion.close()

        except mysql.connector.Error as error:
            print("Error de modificar datos, error: {}".format(error))
