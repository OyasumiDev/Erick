import csv
import os
from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO

def exportar_autos_csv(nombre_archivo="autos_exportados.csv"):
    db = DatabaseMysql()

    select_query = f"SELECT {E_AUTO.ESTADO_AUTO.value}, {E_AUTO.MARCA_AUTO.value}, {E_AUTO.NUM_CILINDROS.value}, {E_AUTO.PRECIO.value} FROM {E_AUTO.TABLE.value}"
    result = db.execute_query(select_query)

    if result["status"] != "success":
        print(f"❌ Error al obtener datos de la base de datos: {result['message']}")
        return

    autos = result["data"]
    if not autos:
        print("⚠️ No hay autos para exportar.")
        return

    # Asegurarse de que la carpeta data existe
    carpeta_data = os.path.join(os.path.dirname(__file__), "..", "data")
    carpeta_data = os.path.abspath(carpeta_data)
    os.makedirs(carpeta_data, exist_ok=True)

    ruta_csv = os.path.join(carpeta_data, nombre_archivo)

    try:
        with open(ruta_csv, mode="w", newline='', encoding="utf-8") as archivo:
            campos = ["estado", "marca", "cilindros", "precio"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()

            for auto in autos:
                escritor.writerow({
                    "estado": auto[0],
                    "marca": auto[1],
                    "cilindros": auto[2],
                    "precio": auto[3]
                })

        print(f"✅ Autos exportados correctamente a {ruta_csv}")
    except Exception as e:
        print(f"❌ Error al escribir el archivo CSV: {e}")
