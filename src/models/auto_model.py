from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO
from config.visual.menu_visual import MenuVisual

class AutoModel:
    """Clase que maneja las operaciones relacionadas con autos."""

    def __init__(self):
        self.db = DatabaseMysql()

    def obtener_autos_nuevos(self):
        """Obtiene la lista de autos con estado 'NUEVO' desde la base de datos."""
        try:
            query = f"""
                SELECT id, estado, marca, num_cilindros, anio, precio
                FROM {E_AUTO.TABLE.value}
                WHERE estado = %s
            """
            params = ("NUEVO",)
            result = self.db.get_all(query, params)

            if result["status"] == "success":
                return result
            else:
                raise Exception(result["message"])

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def get_compras(self):
        """Obtiene todos los autos desde la base de datos."""
        query = f"SELECT * FROM {E_AUTO.TABLE.value}"
        try:
            result = self.db.get_all(query)
            if result["status"] == "success":
                return result["data"]  # Retorna solo los datos, no el status
            else:
                raise Exception(result["message"])
        except Exception as e:
            print(f"Error al obtener datos: {e}")
            return {"status": "error", "message": str(e)}


    def add(self, marca, anio, estado, cilindros, precio):
        """Agrega un nuevo auto a la base de datos."""
        try:
            query = f"""
                INSERT INTO {E_AUTO.TABLE.value} (marca, anio, estado, num_cilindros, precio)
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
