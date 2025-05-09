import mysql.connector
from mysql.connector import pooling, Error
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
        self.pool = None
        self._initialize_connection_pool()

    def _initialize_connection_pool(self):
        """Configura el pool de conexiones para mejorar el rendimiento."""
        try:
            dbconfig = {
                "host": self.host,
                "port": self.port,
                "user": self.user,
                "password": self.password,
                "database": self.database
            }
            self.pool = pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=5,
                **dbconfig
            )
            print("✅ Pool de conexiones inicializado exitosamente")
        except Error as e:
            print(f"❌ Error al inicializar el pool de conexiones: {e}")

    def _get_connection(self):
        """Obtiene una conexión del pool."""
        if self.pool:
            return self.pool.get_connection()
        else:
            print("❌ Pool de conexiones no inicializado")
            return None

    def close(self):
        """Cierra todas las conexiones del pool."""
        if self.pool:
            self.pool.close()
            print("🔒 Pool de conexiones cerrado correctamente.")

    def run_query(self, query: str, params: tuple = ()) -> None:
        """Ejecuta una consulta SQL utilizando el pool de conexiones."""
        conn = self._get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                conn.commit()
            except Error as e:
                print(f"❌ Error ejecutando query: {e}")
            finally:
                conn.close()

    def get_one(self, query: str, params: tuple = (), dictionary: bool = True):
        """Obtiene un único registro de la base de datos."""
        conn = self._get_connection()
        if conn:
            try:
                with conn.cursor(dictionary=dictionary) as cursor:
                    cursor.execute(query, params)
                    return cursor.fetchone()
            except Error as e:
                print(f"❌ Error en get_one: {e}")
            finally:
                conn.close()
        return None

    def get_all(self, query, params=None):
        """Obtiene múltiples registros de la base de datos."""
        conn = self._get_connection()
        if conn:
            try:
                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute(query, params or ())
                    rows = cursor.fetchall()
                return {"status": "success", "data": rows}
            except Exception as e:
                return {"status": "error", "message": str(e)}
            finally:
                conn.close()

    def is_autos_empty(self) -> bool:
        """Verifica si la tabla de autos está vacía."""
        try:
            query = f"SELECT COUNT(*) AS total FROM `{E_AUTO.TABLE.value}`"
            result = self.get_one(query)
            return result.get("total", 0) == 0
        except Exception as e:
            print(f"❌ Error verificando tabla autos: {e}")
            return True

    def execute_query(self, query, params=None):
        """Ejecuta una consulta SQL y maneja errores."""
        conn = self._get_connection()
        if conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(query, params)
                    conn.commit()
                return {"status": "success", "message": "Consulta ejecutada correctamente"}
            except Error as e:
                return {"status": "error", "message": str(e)}
            finally:
                conn.close()
