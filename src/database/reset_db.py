from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO
from autos_data import autos_data


def reset_db():
    """Reinicia las tablas de autos y ventas, y luego inserta nuevos autos."""
    db = DatabaseMysql()

    try:
        # Iniciar transacción
        db.execute_query("START TRANSACTION;")
        print("🔄 Transacción iniciada...")

        # Resetear la tabla de autos (borrar todos los registros)
        query_autos = "TRUNCATE TABLE autos;"  # Cambié de DELETE a TRUNCATE
        result_autos = db.execute_query(query_autos)
        print(f"✅ Tabla de autos reiniciada. Filas afectadas: {result_autos}")

        # Resetear la tabla de ventas (borrar todos los registros)
        query_ventas = "TRUNCATE TABLE ventas;"  # Cambié de DELETE a TRUNCATE
        result_ventas = db.execute_query(query_ventas)
        print(f"✅ Tabla de ventas reiniciada. Filas afectadas: {result_ventas}")

        # Insertar los autos en la base de datos usando autos_data
        insert_query = """
            INSERT INTO autos (estado, marca, cilindros, anio, precio)
            VALUES (%s, %s, %s, %s, %s)
        """
        result_insert = db.execute_many(insert_query, autos_data)  # Cambié run_many por execute_many
        print(f"✅ Autos insertados correctamente. Filas insertadas: {result_insert}")

        # Confirmar la transacción
        db.execute_query("COMMIT;")
        print("✅ Cambios guardados exitosamente.")

    except Exception as e:
        # Revertir la transacción en caso de error
        db.execute_query("ROLLBACK;")
        print(f"❌ Error al resetear la base de datos: {e}")

    finally:
        # Cerrar la conexión a la base de datos si fue abierta
        db.close()
