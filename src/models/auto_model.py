from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO

class AutoModel:
    """Clase que maneja las operaciones relacionadas con autos."""

    def __init__(self):
        self.db = DatabaseMysql()

    def obtener_autos_nuevos(self):
        """Obtiene la lista de autos con estado 'NUEVO' desde la base de datos."""
        try:
            query = f"""
                SELECT id, estado, marca, cilindros, anio, precio
                FROM {E_AUTO.TABLE.value}
                WHERE estado = %s
            """
            params = ("NUEVO",)
            result = self.db.get_all(query, params)

            if result.get("status") == "success":
                return result
            else:
                return {"status": "error", "message": result.get("message", "Error desconocido")}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def get_autos_vendidos(self):
        query = "SELECT * FROM ventas;"  # Consulta a la tabla de ventas
        connection = self.db._get_connection()  # Cambiar a _get_connection
        if connection:
            cursor = connection.cursor()  # Obtener el cursor de la conexión
            try:
                cursor.execute(query)  # Ejecutar la consulta
                result = cursor.fetchall()  # Obtener todos los resultados de la consulta
                return result  # Devuelve los autos vendidos
            finally:
                cursor.close()  # Asegúrate de cerrar el cursor
                connection.close()  # Y también cierra la conexión después de usarla
        else:
            return {"status": "error", "message": "No se pudo obtener la conexión"}

    def get_compras(self):
        """Obtiene todos los autos desde la base de datos."""
        query = f"SELECT * FROM {E_AUTO.TABLE.value}"
        try:
            result = self.db.get_all(query)
            if result:  # Comprobamos si result no está vacío
                return result
            else:
                raise Exception("No se encontraron autos.")
        except Exception as e:
            print(f"Error al obtener datos: {e}")
            return {"status": "error", "message": str(e)}

    def add(self, marca, anio, estado, cilindros, precio):
        """Agrega un nuevo auto a la base de datos."""
        try:
            query = f"""
                INSERT INTO {E_AUTO.TABLE.value} (marca, anio, estado, cilindros, precio)
                VALUES (%s, %s, %s, %s, %s)
            """
            params = (marca, anio, estado, cilindros, precio)
            result = self.db.execute_query(query, params)  # ✅ Cambio aquí

            if result["status"] == "success":
                return {"status": "success", "message": f"Auto {marca} {anio} agregado correctamente"}
            else:
                raise Exception(result["message"])

        except Exception as e:
            return {"status": "error", "message": str(e)}
