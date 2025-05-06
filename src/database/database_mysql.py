from config.config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE, DB_PORT
import mysql.connector as mysql
from mysql.connector import Error
from enums.e_autos import E_AUTO 
from helpers.class_singletone import class_singleton
# Asegúrate de importar correctamente tu Enum

@class_singleton
class DatabaseMysql:
    def __init__(self):
        self.host = DB_HOST
        self.port = DB_PORT
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.database = DB_DATABASE

        self._verificar_y_crear_base_datos()
        self._connect()

    def _verificar_y_crear_base_datos(self) -> bool:
        """Verifica si existe la base de datos y la crea si no existe."""
        try:
            tmp = mysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            )
            tmp.autocommit = True
            cur = tmp.cursor()
            cur.execute(
                "SELECT SCHEMA_NAME FROM information_schema.schemata WHERE schema_name = %s",
                (self.database,)
            )
            if cur.fetchone() is None:
                cur.execute(
                    f"CREATE DATABASE `{self.database}` "
                    "DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
                )
                print("🛠️ Base de datos creada")
            cur.close()
            tmp.close()
        except Error as e:
            print(f"❌ Error al verificar/crear BD: {e}")
            return False
        return True

    def _connect(self) -> None:
        """Conecta a la base de datos."""
        try:
            self.connection = mysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("✅ Conexión exitosa a la base de datos")
        except Error as e:
            print(f"❌ Error al conectar: {e}")

    def disconnect(self) -> None:
        """Cierra la conexión a la base de datos."""
        if hasattr(self, "connection") and self.connection:
            self.connection.close()
            print("ℹ️ Conexión cerrada a la base de datos")

    def run_query(self, query: str, params: tuple = ()) -> None:
        """Ejecuta una consulta de modificación (INSERT, UPDATE, DELETE)."""
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print(f"❌ Error ejecutando query: {e}")
            raise

    def get_one(self, query: str, params: tuple = (), dictionary: bool = True):
        """Obtiene un solo registro."""
        try:
            with self.connection.cursor(dictionary=dictionary) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
        except Error as e:
            print(f"❌ Error en get_one: {e}")
            return None

    def get_all(self, query: str, params: tuple = (), dictionary: bool = True):
        """Obtiene una lista de registros."""
        try:
            with self.connection.cursor(dictionary=dictionary) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Error as e:
            print(f"❌ Error en get_all: {e}")
            return []

    def is_autos_empty(self) -> bool:
        """Verifica si la tabla de autos está vacía."""
        try:
            query = f"SELECT COUNT(*) AS total FROM `{E_AUTO.TABLE.value}`"
            result = self.get_one(query)
            return result.get("total", 0) == 0
        except Exception as e:
            print(f"❌ Error verificando tabla autos: {e}")
            return True
