from database.database_mysql import DatabaseMysql

class AutoModel:
    """Clase que maneja las operaciones relacionadas con autos."""

    def __init__(self):
        self.db = DatabaseMysql()

    def obtener_autos_nuevos(self):
        """Obtiene la lista de autos con estado 'NUEVO' desde la base de datos."""
        try:
            query = """
                SELECT id, estado, marca, cilindros, anio, precio
                FROM autos
                WHERE estado = %s
            """
            params = ("NUEVO",)
            result = self.db.get_all(query, params)

            if result["status"] == "success":
                return result["data"]
            else:
                return {"status": "error", "message": result.get("message", "Error desconocido")}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def get_autos_vendidos(self):
        """Obtiene todos los autos vendidos desde la base de datos."""
        query = "SELECT id, marca, estado, cilindros, anio, precio FROM ventas;"
        result = self.db.get_all(query)
        
        if result["status"] == "success" and result["data"]:
            # Los datos devueltos se formatean como una lista de tuplas
            return result["data"]
        else:
            return {"status": "error", "message": result.get("message", "Error desconocido")}

    def get_compras(self):
        """Obtiene todos los autos desde la base de datos."""
        query = "SELECT id, estado, marca, cilindros, anio, precio FROM autos"
        try:
            result = self.db.get_all(query)
            if result["status"] == "success" and result["data"]:
                return result["data"]
            else:
                raise Exception("No se encontraron autos.")
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def add(self, marca, anio, estado, cilindros, precio):
        """Agrega un nuevo auto a la base de datos."""
        try:
            if estado not in ["NUEVO", "USADO"]:
                raise Exception("Estado inválido")

            query = """
                INSERT INTO autos (marca, anio, estado, cilindros, precio)
                VALUES (%s, %s, %s, %s, %s)
            """
            params = (marca, anio, estado, cilindros, precio)
            result = self.db.execute_query(query, params)

            if result["status"] == "success":
                return {"status": "success", "message": f"Auto {marca} {anio} agregado correctamente"}
            else:
                raise Exception(result["message"])
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def vender_auto(self, auto_id):
        """Realiza la venta de un auto y lo elimina de la tabla de autos."""
        try:
            # Comienza una transacción
            conn = self.db._get_connection()
            if not conn:
                return {"status": "error", "message": "No se pudo obtener conexión"}

            cursor = conn.cursor()
            cursor.execute("START TRANSACTION")

            # Obtenemos el auto que se va a vender
            query = "SELECT id, marca, cilindros, anio, precio, estado FROM autos WHERE id = %s"
            params = (auto_id,)
            auto_result = self.db.get_one(query, params)

            if auto_result["status"] == "error" or not auto_result["data"]:
                return {"status": "error", "message": "Auto no encontrado"}

            auto = auto_result["data"]

            # Insertamos el auto en la tabla de ventas
            insert_query = """
                INSERT INTO ventas (id, marca, cilindros, anio, precio, estado)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            insert_params = (auto["id"], auto["marca"], auto["cilindros"], auto["anio"], auto["precio"], auto["estado"])
            insert_result = self.db.execute_query(insert_query, insert_params)

            if insert_result["status"] != "success":
                cursor.execute("ROLLBACK")
                cursor.close()
                conn.close()
                return {"status": "error", "message": "Error al insertar en ventas"}

            # Eliminamos el auto de la tabla de autos
            delete_query = "DELETE FROM autos WHERE id = %s"
            delete_result = self.db.execute_query(delete_query, (auto_id,))

            if delete_result["status"] != "success":
                cursor.execute("ROLLBACK")
                cursor.close()
                conn.close()
                return {"status": "error", "message": "Error al eliminar el auto de la tabla autos"}

            cursor.execute("COMMIT")
            cursor.close()
            conn.close()

            # Verificación adicional
            select_query = "SELECT * FROM ventas WHERE id = %s"
            select_params = (auto_id,)
            ventas_result = self.db.get_all(select_query, select_params)
            if ventas_result["status"] == "success" and ventas_result["data"]:
                print(f"Auto con ID {auto_id} insertado en ventas.")
            else:
                print(f"Error al insertar auto con ID {auto_id} en ventas.")

            return {"status": "success", "message": "Auto vendido correctamente"}
        except Exception as e:
            if conn:
                cursor.execute("ROLLBACK")
                cursor.close()
                conn.close()
            return {"status": "error", "message": str(e)}
