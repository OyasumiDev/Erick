import mysql.connector
from mysql.connector import Error
import os

estado_insertado_file = "insert_state.txt"

class DatabaseConnectionSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None
            cls._instance._cursor = None
        return cls._instance

    def _connect(self):
        """Establece una nueva conexión a la base de datos."""
        try:
            self._connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="yourpassword",
                database="autos_db"
            )
            self._cursor = self._connection.cursor()
        except Error as e:
            print(f"❌ Error al conectar a la base de datos: {e}")
            self._connection = None
            self._cursor = None

    def get_cursor(self):
        """Obtiene el cursor de la base de datos, estableciendo la conexión si es necesario."""
        if self._connection is None or self._connection.is_closed():
            self._connect()
        return self._cursor

    def commit(self):
        """Confirma la transacción actual."""
        if self._connection:
            self._connection.commit()

    def close(self):
        """Cierra el cursor y la conexión a la base de datos."""
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()

def check_if_data_inserted():
    """Verifica si los datos ya han sido insertados."""
    if os.path.exists(estado_insertado_file):
        with open(estado_insertado_file, 'r') as file:
            return file.read().strip() == 'true'
    return False

def mark_data_as_inserted():
    """Marca los datos como insertados."""
    with open(estado_insertado_file, 'w') as file:
        file.write('true')

def insert_data():
    """Inserta datos en la base de datos si no han sido insertados previamente."""
    if check_if_data_inserted():
        print("✅ Los datos ya han sido insertados previamente.")
        return

    print("Insertando los datos al reiniciar el sistema...")

    autos_data = [
        (1, 'NUEVO', 'NISSAN', 6, 2023, 425000),
        (2, 'USADOS', 'NISSAN', 4, 2015, 195000),
        (3, 'NUEVO', 'CHEVROLET', 6, 2024, 478000),
        (4, 'USADOS', 'VOLKSWAGEN', 4, 2013, 145000),
        (5, 'USADOS', 'HONDA', 8, 2016, 230000),
    ]

    db = DatabaseConnectionSingleton()
    cursor = db.get_cursor()

    try:
        for auto in autos_data:
            cursor.execute("""
            INSERT INTO autos (ID, ESTADO_AUTO, MARCA_AUTO, NUM_CILINDROS, ANIO, PRECIO)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, auto)
        db.commit()
        print("✅ Datos insertados exitosamente en la tabla autos.")
        mark_data_as_inserted()
    except Error as e:
        print(f"❌ Error al insertar datos: {e}")
    finally:
        db.close()
