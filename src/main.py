import mysql.connector
from models.auto_model import AutoModel

from enum import Enum

# Enum para los nombres de columnas
class E_AUTO(Enum):
    TABLE = 'autos'
    ID = 'ID'
    ESTADO_AUTO = 'ESTADO_AUTO'
    MARCA_AUTO = 'MARCA_AUTO'
    NUM_CILINDROS = 'NUM_CILINDROS'

# Clase que maneja los autos
class AutoManager:
    def __init__(self, db_connection):
        self.db = db_connection  # Debe tener un método run_query(query, params)

    def add(self, estado_auto: str, marca: str, cilindros: int) -> dict:
        """Agrega un nuevo auto a la base de datos."""
        query = f"""
            INSERT INTO {E_AUTO.TABLE.value} (
                {E_AUTO.ESTADO_AUTO.value},
                {E_AUTO.MARCA_AUTO.value},
                {E_AUTO.NUM_CILINDROS.value}
            ) VALUES (%s, %s, %s)
        """
        try:
            self.db.run_query(query, (estado_auto, marca, cilindros))
            return {"status": "success", "message": "Auto agregado correctamente"}
        except Exception as ex:
            return {"status": "error", "message": f"Error al agregar auto: {ex}"}


# Simulación de una conexión (ajústalo con tu conexión real)
class MyDB:
    def __init__(self, connection):
        self.connection = connection

    def run_query(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        cursor.close()


# Función principal
def main():
    import mysql.connector

    # Conexión a MySQL (ajusta estos valores a los tuyos)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="playerchidote77@",
        database="DB_PIA"
    )

    db = MyDB(connection)
    gestor = AutoManager(db)

    autos = [
        ('NUEVO', 'NISSAN', 6),
        ('USADOS', 'NISSAN', 4),
        ('NUEVO', 'CHEVROLET', 6),
        ('USADOS', 'VOLKSWAGEN', 4),
        ('USADOS', 'HONDA', 8),
        ('NUEVO', 'TOYOTA', 4),
        ('USADOS', 'FORD', 4),
        ('NUEVO', 'HYUNDAI', 6),
        ('USADOS', 'KIA', 6),
        ('USADOS', 'HONDA', 4),
        ('NUEVO', 'TOYOTA', 6),
        ('USADOS', 'CHEVROLET', 6),
        ('USADOS', 'BMW', 8),
        ('NUEVO', 'FORD', 4),
        ('NUEVO', 'TOYOTA', 4),
        ('USADOS', 'KIA', 6),
        ('USADOS', 'MERCEDES-BENZ', 6),
        ('USADOS', 'NISSAN', 4),
        ('NUEVO', 'TESLA', 4),
        ('USADOS', 'JEEP', 6),
        ('USADOS', 'TOYOTA', 6),
        ('NUEVO', 'NISSAN', 4),
        ('USADOS', 'FORD', 4),
        ('USADOS', 'HONDA', 6),
        ('NUEVO', 'BMW', 6),
        ('USADOS', 'MITSUBISHI', 6),
        ('USADOS', 'CHEVROLET', 4),
        ('NUEVO', 'TESLA', 6),
        ('USADOS', 'KIA', 6),
        ('USADOS', 'FORD', 4),
        ('NUEVO', 'MITSUBISHI', 6),
        ('USADOS', 'HONDA', 6),
        ('USADOS', 'KIA', 4),
        ('NUEVO', 'VOLKSWAGEN', 4),
        ('USADOS', 'TOYOTA', 6),
        ('NUEVO', 'BMW', 8),
        ('USADOS', 'HYUNDAI', 6),
        ('USADOS', 'MERCEDES-BENZ', 8),
        ('USADOS', 'NISSAN', 4),
        ('USADOS', 'CHEVROLET', 6),
        ('USADOS', 'FORD', 4),
        ('NUEVO', 'HONDA', 4),
        ('NUEVO', 'TOYOTA', 6),
        ('USADOS', 'JEEP', 6),
        ('USADOS', 'VOLKSWAGEN', 4),
        ('USADOS', 'MITSUBISHI', 6),
        ('NUEVO', 'BMW', 8),
        ('USADOS', 'MERCEDES-BENZ', 8),
        ('USADOS', 'HYUNDAI', 6),
        ('USADOS', 'HONDA', 6),
        ('NUEVO', 'FORD', 4),
        ('USADOS', 'CHEVROLET', 4),
        ('NUEVO', 'JEEP', 6),
        ('USADOS', 'KIA', 4),
        ('NUEVO', 'MERCEDES-BENZ', 8),
        ('USADOS', 'NISSAN', 6),
        ('USADOS', 'TOYOTA', 6),
        ('NUEVO', 'BMW', 8),
        ('USADOS', 'HYUNDAI', 6),
        ('USADOS', 'TOYOTA', 6),
        ('NUEVO', 'NISSAN', 6),
        ('USADOS', 'MITSUBISHI', 6),
        ('USADOS', 'FORD', 4),
        ('USADOS', 'HONDA', 4),
        ('USADOS', 'JEEP', 6),
        ('NUEVO', 'TOYOTA', 6),
        ('USADOS', 'NISSAN', 4),
        ('NUEVO', 'HYUNDAI', 4),
        ('USADOS', 'MERCEDES-BENZ', 8),
        ('USADOS', 'KIA', 4),
        ('USADOS', 'HONDA', 6),
        ('NUEVO', 'MITSUBISHI', 6),
        ('USADOS', 'FORD', 6),
        ('USADOS', 'BMW', 8),
        ('USADOS', 'JEEP', 6),
        ('NUEVO', 'VOLKSWAGEN', 4),
        ('USADOS', 'MERCEDES-BENZ', 8),
        ('USADOS', 'HYUNDAI', 6),
        ('USADOS', 'CHEVROLET', 6),
        ('NUEVO', 'NISSAN', 4),
        ('USADOS', 'TOYOTA', 6),
        ('NUEVO', 'MITSUBISHI', 4),
        ('USADOS', 'HONDA', 6),
        ('USADOS', 'VOLKSWAGEN', 4),
        ('NUEVO', 'CHEVROLET', 4),
        ('USADOS', 'FORD', 6),
        ('USADOS', 'KIA', 4),
        ('NUEVO', 'BMW', 8),
        ('USADOS', 'MERCEDES-BENZ', 8),
        ('USADOS', 'HONDA', 4),
        ('NUEVO', 'VOLKSWAGEN', 4),
        ('USADOS', 'TOYOTA', 6),
        ('NUEVO', 'FORD', 4),
        ('USADOS', 'BMW', 6),
        ('USADOS', 'MERCEDES-BENZ', 8),
        ('USADOS', 'CHEVROLET', 4),
        ('NUEVO', 'HONDA', 6),
        ('USADOS', 'KIA', 4),
        ('USADOS', 'MERCEDES-BENZ', 8),
        ('USADOS', 'JEEP', 6)
    ]

    for estado, marca, cilindros in autos:
        resultado = gestor.add(estado, marca, cilindros)
        print(resultado["message"])

    connection.close()


if __name__ == "__main__":
    main()







def ver_autos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="playerchidote77@",
        database="DB_PIA"
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM autos")
    autos = cursor.fetchall()

    for auto in autos:
        print(auto)

    conexion.close()


