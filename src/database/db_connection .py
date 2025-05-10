from database_mysql import DatabaseMysql  
from enums.e_autos import E_AUTO
import os

estado_insertado_file = "insert_state.txt"

def check_if_data_inserted():
    """Verifica si los datos ya han sido insertados."""
    return os.path.exists(estado_insertado_file)

def mark_data_as_inserted():
    """Marca los datos como insertados."""
    with open(estado_insertado_file, 'w') as file:
        file.write('true')

def insert_data():
    """Inserta datos en la base de datos si no han sido insertados previamente."""
    if check_if_data_inserted():
        print("✅ Los datos ya han sido insertados previamente.")
        return

    print("Insertando los datos al reiniciar el sistema...")

    autos_data = [
        (1, 'NUEVO', 'NISSAN', 6, 2023, 425000.00),
        (2, 'USADOS', 'NISSAN', 4, 2015, 195000.00),
        (3, 'NUEVO', 'CHEVROLET', 6, 2024, 478000.00),
        (4, 'USADOS', 'VOLKSWAGEN', 4, 2013, 145000.00),
        (5, 'USADOS', 'HONDA', 8, 2016, 230000.00),
    ]

    db = DatabaseMysql()
    try:
        for auto in autos_data:
            query = f"""
            INSERT INTO `{E_AUTO.TABLE.value}` (ID, ESTADO_AUTO, MARCA_AUTO, NUM_CILINDROS, ANIO, PRECIO)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            db.run_query(query, auto)
        print("✅ Datos insertados exitosamente en la tabla autos.")
        mark_data_as_inserted()
    except Exception as e:
        print(f"❌ Error al insertar datos: {e}")
