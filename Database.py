import mariadb
import sys


def abrirConexion():
    try:
        conexion = mariadb.connect(
            user="root",
            password="1006242",
            host="127.0.0.1",
            port=3306,
            database="proyectofinal"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    return conexion.cursor()


def cerrarConexion(conexion):
    if conexion:
        conexion.close()
