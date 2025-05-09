import mysql.connector
from mysql.connector import Error
from config.config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE, DB_PORT
from enums.e_autos import E_AUTO
from helpers.class_singletone import class_singleton

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
        try:
            tmp = mysql.connector.connect(
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
                    f"CREATE DATABASE `{self.database}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
                )
                print("🛠️ Base de datos creada")
            cur.close()
            tmp.close()
        except Error as e:
            print(f"❌ Error al verificar/crear BD: {e}")
            return False
        return True

    def _connect(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("✅ Conexión exitosa a la base de datos")
        except Error as e:
            print(f"❌ Error al conectar: {e}")

    def close(self) -> None:
        """Cierra la conexión a la base de datos."""
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()
            print("🔒 Conexión cerrada correctamente.")

    def run_query(self, query: str, params: tuple = ()) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
            self.connection.commit()
        except Error as e:
            print(f"❌ Error ejecutando query: {e}")
            raise

    def get_one(self, query: str, params: tuple = (), dictionary: bool = True):
        try:
            with self.connection.cursor(dictionary=dictionary) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
        except Error as e:
            print(f"❌ Error en get_one: {e}")
            return None

    def get_all(self, query, params=None):
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, params or ())
                rows = cursor.fetchall()
            return {"status": "success", "data": rows}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def is_autos_empty(self) -> bool:
        try:
            query = f"SELECT COUNT(*) AS total FROM `{E_AUTO.TABLE.value}`"
            result = self.get_one(query)
            return result.get("total", 0) == 0
        except Exception as e:
            print(f"❌ Error verificando tabla autos: {e}")
            return True

    def execute_query(self, query, params=None):
        if not self.connection:
            self._connect()

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
            return {"status": "success", "message": "Consulta ejecutada correctamente"}
        except Error as e:
            return {"status": "error", "message": str(e)}
