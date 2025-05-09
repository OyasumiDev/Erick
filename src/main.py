import mysql.connector
from config.visual.menu_visual import mostrar_menu
from config.visual.menu_ventas import ventana_ventas
from config.visual.menu_compras import ventana_compras
from database.database_mysql import DatabaseMysql
from database.import_db import import_db
from enums.e_autos import E_AUTO
import csv
import os

def resetear_base_datos():
    db = DatabaseMysql()

    # Eliminar tabla si existe
    drop_query = f"DROP TABLE IF EXISTS {E_AUTO.TABLE.value}"
    db.execute_query(drop_query)

    # Crear tabla autos
    create_query = f"""
    CREATE TABLE {E_AUTO.TABLE.value} (
        {E_AUTO.ID.value} INT AUTO_INCREMENT PRIMARY KEY,
        {E_AUTO.ESTADO_AUTO.value} VARCHAR(20),
        {E_AUTO.MARCA_AUTO.value} VARCHAR(50),
        {E_AUTO.NUM_CILINDROS.value} INT,
        {E_AUTO.PRECIO.value} FLOAT
    )
    """
    db.execute_query(create_query)
    print("✅ Base de datos reseteada y tabla creada correctamente.")

def cargar_datos_csv():
    db = DatabaseMysql()
    ruta_csv = "data/autos_default.csv"

    if not os.path.exists(ruta_csv):
        print("❌ El archivo autos_default.csv no se encuentra.")
        return

    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                estado = fila["estado"]
                marca = fila["marca"]
                cilindros = int(fila["cilindros"])
                precio = float(fila["precio"])

                insert_query = f"""
                INSERT INTO {E_AUTO.TABLE.value}
                ({E_AUTO.ESTADO_AUTO.value}, {E_AUTO.MARCA_AUTO.value}, {E_AUTO.NUM_CILINDROS.value}, {E_AUTO.PRECIO.value})
                VALUES (%s, %s, %s, %s)
                """
                params = (estado, marca, cilindros, precio)
                result = db.execute_query(insert_query, params)

                if result["status"] == "success":
                    print(f"✅ Auto {marca} {estado} insertado correctamente.")
                else:
                    print(f"❌ Error al insertar el auto {marca} {estado}: {result['message']}")
            except Exception as e:
                print(f"❌ Error procesando fila: {fila}. Detalle: {e}")

def main():
    try:
        resetear_base_datos()
        cargar_datos_csv()
        mostrar_menu()  # Llamar al menú después de cargar la base de datos
    except Exception as e:
        print(f"❌ Error general en el programa: {e}")

if __name__ == "__main__":
    main()
