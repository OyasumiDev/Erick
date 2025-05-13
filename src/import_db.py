from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO
from autos_data import autos_data
import traceback

class DatabaseImport:
    def import_db(self):
        # Crear una instancia de la clase de base de datos
        db = DatabaseMysql()
        
        try:
            # Verificar si la tabla 'autos' ya contiene datos
            query = "SELECT COUNT(*) FROM autos"
            result = db.execute_query(query)

            # Verificar si el resultado es un diccionario y obtener la clave 'data'
            if isinstance(result, dict) and 'data' in result:
                count = result['data'][0][0]  # Accedemos a los resultados desde la clave 'data'
            else:
                raise ValueError(f"El resultado inesperado de la consulta fue: {result}")

            if count > 0:
                print("⚠️ La tabla ya contiene datos. No se insertará nada.")
                return

            # Iniciar la transacción
            db.execute_query("START TRANSACTION;")

            # Definir la consulta de inserción
            insert_query = """
                INSERT INTO autos (estado, marca, cilindros, anio, precio) 
                VALUES (%s, %s, %s, %s, %s)
            """

            # Ejecutar la inserción masiva usando los datos de autos
            db.execute_many(insert_query, autos_data)

            # Confirmar la transacción
            db.execute_query("COMMIT;")
            print("✅ Autos importados correctamente.")
        
        except Exception as e:
            # Revertir la transacción en caso de error
            db.execute_query("ROLLBACK;")
            # Imprimir el error con detalles más claros para diagnóstico
            print(f"❌ Error al importar los autos. Detalles del error: {str(e)}")

            # Si el error es un error relacionado con la base de datos
            if 'IntegrityError' in str(e):
                print("⚠️ Error de integridad: podría haber un problema con las restricciones de la base de datos.")
            elif 'OperationalError' in str(e):
                print("⚠️ Error operacional: podría haber un problema con la conexión a la base de datos.")
            else:
                print("⚠️ Error inesperado durante la importación.")

            # Imprimir la traza completa del error para depurar
            print("📜 Detalles del error:")
            print(traceback.format_exc())  # Esto imprimirá toda la traza del error
        
        finally:
            # Cerrar la conexión a la base de datos si fue abierta
            if db:
                db.close()  # Cerramos la conexión correctamente
