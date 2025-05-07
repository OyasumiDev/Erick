import mysql.connector
from models.auto_model import AutoModel

AutoModel.add("Toyota", "Corolla", 2020, "Rojo", 15000.0)

def ver_autos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="BASE_AUTOS"
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM autos")
    autos = cursor.fetchall()

    for auto in autos:
        print(auto)

    conexion.close()


