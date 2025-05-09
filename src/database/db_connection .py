import mysql.connector
import os

estado_insertado_file = "insert_state.txt"

class DatabaseConnectionSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Cambia estos valores según tu configuración
                password="yourpassword",
                database="autos_db"
            )
            cls._instance.cursor = cls._instance.connection.cursor()
        return cls._instance
    
    def get_cursor(self):
        return self._instance.cursor
    
    def commit(self):
        self._instance.connection.commit()
    
    def close(self):
        self._instance.cursor.close()
        self._instance.connection.close()

def check_if_data_inserted():
    if os.path.exists(estado_insertado_file):
        with open(estado_insertado_file, 'r') as file:
            return file.read().strip() == 'true'
    else:
        return False

def mark_data_as_inserted():
    with open(estado_insertado_file, 'w') as file:
        file.write('true')

def insert_data():
    print("Insertando los datos al reiniciar el sistema...")

    autos_data = [
        (1, 'NUEVO', 'NISSAN', 6, 2023, 425000),
        (2, 'USADOS', 'NISSAN', 4, 2015, 195000),
        (3, 'NUEVO', 'CHEVROLET', 6, 2024, 478000),
        (4, 'USADOS', 'VOLKSWAGEN', 4, 2013, 145000),
        (5, 'USADOS', 'HONDA', 8, 2016, 230000),
        # Agrega más autos si es necesario
    ]

    db = DatabaseConnectionSingleton()
    cursor = db.get_cursor()
    
    for auto in autos_data:
        cursor.execute("""
        INSERT INTO autos (ID, ESTADO_AUTO, MARCA_AUTO, NUM_CILINDROS, ANIO, PRECIO)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, auto)
    
    db.commit()
    print("Datos insertados exitosamente en la tabla autos.")
    
    mark_data_as_inserted()

