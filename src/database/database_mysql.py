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
        try:
            if self.pool:
                return self.pool.get_connection()
            print("❌ Pool de conexiones no inicializado")
        except Error as e:
            print(f"❌ Error al obtener conexión: {e}")
        return None

    def execute_query(self, query, params=None):
        conn = self._get_connection()
        if not conn:
            return {"status": "error", "message": "No se pudo obtener conexión"}

        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                return {"status": "success", "data": result}
            else:
                conn.commit()
                return {"status": "success", "message": "Consulta ejecutada correctamente"}
        except Error as e:
            print(f"❌ Error en execute_query: {e}")
            return {"status": "error", "message": str(e)}
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    def execute_many(self, query, params_list):
        conn = self._get_connection()
        if not conn:
            return {"status": "error", "message": "No se pudo obtener la conexión"}

        try:
            cursor = conn.cursor()
            cursor.executemany(query, params_list)
            conn.commit()
            return {"status": "success", "message": "Inserción masiva realizada correctamente"}
        except Error as e:
            print(f"❌ Error en execute_many: {e}")
            return {"status": "error", "message": str(e)}
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    def get_one(self, query: str, params: tuple = (), dictionary: bool = True):
        conn = self._get_connection()
        if not conn:
            return {"status": "error", "message": "No se pudo obtener la conexión"}

        try:
            cursor = conn.cursor(buffered=True, dictionary=dictionary)
            cursor.execute(query, params)
            result = cursor.fetchone()
            if result:
                return {"status": "success", "data": result}
            return {"status": "error", "message": "No se encontraron datos"}
        except Error as e:
            print(f"❌ Error en get_one: {e}")
            return {"status": "error", "message": str(e)}
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    def get_all(self, query, params=None):
        conn = self._get_connection()
        if not conn:
            return {"status": "error", "message": "No se pudo obtener la conexión", "data": []}

        try:
            cursor = conn.cursor(buffered=True, dictionary=True)
            cursor.execute(query, params or ())
            rows = cursor.fetchall()
            return {"status": "success", "data": rows}
        except Error as e:
            print(f"❌ Error en get_all: {e}")
            return {"status": "error", "message": str(e), "data": []}
        finally:
            try:
                cursor.close()
                conn.close()
            except:
                pass

    def is_autos_empty(self) -> bool:
        try:
            query = f"SELECT COUNT(*) AS total FROM `{E_AUTO.TABLE.value}`"
            result = self.get_one(query)
            return result.get("data", {}).get("total", 0) == 0
        except Exception as e:
            print(f"❌ Error verificando tabla autos: {e}")
            return True

    def close(self):
        print("ℹ️ Cierre manual del pool no necesario en mysql.connector, pero método presente por estructura.")
