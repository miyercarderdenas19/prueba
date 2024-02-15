import pyodbc

# Parámetros de conexión
server = 'SAP'
database = 'SG-STEAMCONTROL'
username = 'SGSTEAM'
password = 'Sg-St34m&C0ntr0l'

# Cadena de conexión
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Intenta establecer la conexión
try:
    
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    # Ejemplo de consulta SELECT
    cursor.execute("SELECT * Mantenimiento")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
     
     
    # Cerrar cursor y conexión
    cursor.close()
    conn.close()

except Exception as e:
    print(f'Error al conectar a la base de datos: {e}')
