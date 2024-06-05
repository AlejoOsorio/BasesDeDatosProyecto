import mariadb

import Database

conexion = Database.abrirConexion()

try:
    # Define la consulta SQL
    query = "SELECT * FROM prioridades"

    # Ejecuta la consulta
    conexion.execute(query)

    # Recupera los resultados
    for row in conexion.fetchall():
        # Procesa cada fila de resultados
        print(row)

except mariadb.Error as e:
    print(f"Error executing SQL query: {e}")

# Cierra la conexión
conexion.close()