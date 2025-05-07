import mysql.connector
from models.auto_model import AutoModel
from enum import Enum

# Asegúrate de tener bien configurado tu modelo para la conexión a la base de datos
class DatabaseMysql:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",  # Cambia esto según tu configuración
            user="root",       # Cambia esto según tu configuración
            password="password",  # Cambia esto según tu configuración
            database="nombre_base_datos"  # Cambia esto por el nombre de tu base de datos
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def run_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

class E_AUTO(Enum):
    TABLE = "autos"
    ESTADO_AUTO = "estado_auto"
    MARCA_AUTO = "marca_auto"
    NUM_CILINDROS = "num_cilindros"
    ID = "id"

class AutoModel:
    def __init__(self):
        self.db = DatabaseMysql()

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
            return {"status": "success", "message": f"Auto {marca} agregado correctamente"}
        except mysql.connector.Error as err:
            return {"status": "error", "message": f"Error al agregar auto {marca}: {err}"}

    def close_connection(self):
        self.db.close()

# Lista de autos a insertar
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
    ('NUEVO', 'FORD', 6),
    ('USADOS', 'TOYOTA', 4),
    ('USADOS', 'HONDA', 6),
    ('NUEVO', 'KIA', 6),
    ('USADOS', 'CHEVROLET', 6),
    ('NUEVO', 'BMW', 4),
    ('USADOS', 'VOLKSWAGEN', 6),
    ('USADOS', 'TOYOTA', 4),
    ('NUEVO', 'HONDA', 8),
    ('USADOS', 'MITSUBISHI', 6),
    ('NUEVO', 'FORD', 4),
    ('USADOS', 'TESLA', 6),
    ('NUEVO', 'NISSAN', 4),
    ('USADOS', 'HONDA', 6),
    ('USADOS', 'FORD', 4),
    ('USADOS', 'CHEVROLET', 8),
    ('NUEVO', 'HONDA', 6),
    ('USADOS', 'MERCEDES-BENZ', 4),
    ('NUEVO', 'KIA', 4),
    ('USADOS', 'BMW', 6),
    ('USADOS', 'TESLA', 8),
    ('NUEVO', 'NISSAN', 4),
    ('USADOS', 'HYUNDAI', 6),
    ('NUEVO', 'FORD', 6),
    ('USADOS', 'HONDA', 8),
    ('USADOS', 'TOYOTA', 4),
    ('NUEVO', 'KIA', 6),
    ('USADOS', 'MERCEDES-BENZ', 6),
    ('NUEVO', 'VOLKSWAGEN', 6),
    ('USADOS', 'CHEVROLET', 4),
    ('NUEVO', 'MITSUBISHI', 6),
    ('USADOS', 'NISSAN', 4),
    ('NUEVO', 'FORD', 8),
    ('USADOS', 'HONDA', 4),
    ('USADOS', 'KIA', 6),
    ('NUEVO', 'BMW', 6),
    ('USADOS', 'JEEP', 4),
    ('USADOS', 'MERCEDES-BENZ', 4),
    ('USADOS', 'TOYOTA', 8),
    ('USADOS', 'FORD', 6),
    ('NUEVO', 'HONDA', 4),
    ('USADOS', 'VOLKSWAGEN', 6),
    ('USADOS', 'MITSUBISHI', 4),
    ('USADOS', 'CHEVROLET', 8),
    ('USADOS', 'NISSAN', 4),
    ('NUEVO', 'BMW', 6),
    ('USADOS', 'FORD', 6),
    ('USADOS', 'HONDA', 4),
    ('USADOS', 'TOYOTA', 4),
    ('NUEVO', 'HYUNDAI', 6)
]

# Instanciamos AutoModel
auto_model = AutoModel()

# Insertamos los autos
for auto in autos:
    respuesta = auto_model.add(auto[0], auto[1], auto[2])
    print(respuesta['message'])  # Imprime el mensaje de éxito o error

# Cerramos la conexión después de las inserciones
auto_model.close_connection()