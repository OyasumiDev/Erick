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

    def ver_autos(self):
        """Muestra todos los autos de la base de datos."""
        query = f"SELECT * FROM {E_AUTO.TABLE.value}"
        try:
            autos = self.db.run_query(query, ())
            for auto in autos:
                print(auto)
        except Exception as ex:
            print(f"Error al obtener autos: {ex}")

# Simulación de una conexión (ajústalo con tu conexión real)
class MyDB:
    def __init__(self, connection):
        self.connection = connection

    def run_query(self, query, params):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()  # Devuelve los resultados si es una consulta SELECT
        else:
            self.connection.commit()
        cursor.close()

# Función para conectar a la base de datos
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="playerchidote77@",
        database="DB_PIA"
    )

# Función principal
def main():
    # Conexión a la base de datos
    connection = connect_db()
    db = MyDB(connection)
    gestor = AutoManager(db)

    # Datos de autos
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
        # Agrega más autos aquí...
    ]

    # Insertar autos
    for estado, marca, cilindros in autos:
        resultado = gestor.add(estado, marca, cilindros)
        print(resultado["message"])

    # Ver autos
    print("\nListado de autos en la base de datos:")
    gestor.ver_autos()

    # Cerrar la conexión
    connection.close()

if __name__ == "__main__":
    main()
