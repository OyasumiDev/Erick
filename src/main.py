from config.visual.menu_visual import mostrar_menu
from database.database_mysql import DatabaseMysql
from database.import_db import import_db
from enums.e_autos import E_AUTO



def resetear_base_datos():
    # Crear una instancia de la clase DatabaseMysql para conectarse a la base de datos
    db = DatabaseMysql()

    # Eliminar la tabla si ya existe
    drop_query = f"DROP TABLE IF EXISTS {E_AUTO.TABLE.value}"
    db.execute_query(drop_query)

    # Crear la tabla desde cero
    create_query = f"""
    CREATE TABLE {E_AUTO.TABLE.value} (
        {E_AUTO.ID.value} INT AUTO_INCREMENT PRIMARY KEY,
        {E_AUTO.ESTADO_AUTO.value} VARCHAR(20),
        {E_AUTO.MARCA_AUTO.value} VARCHAR(50),
        {E_AUTO.NUM_CILINDROS.value} INT,
        {E_AUTO.ANIO.value} INT,
        {E_AUTO.PRECIO.value} FLOAT
    )
    """
    db.execute_query(create_query)
    print("✅ Base de datos reseteada y tabla creada correctamente.")

def main():
    try:
        # Reiniciar la base de datos y tabla
        print("🔄 Reiniciando base de datos...")
        resetear_base_datos()
        
        # Insertar los datos por defecto en la base de datos
        print("📥 Insertando autos por defecto...")
        import_db()
        
        # Iniciar el sistema visual (menú)
        print("🚗 Iniciando sistema visual...")
        mostrar_menu()
    except Exception as e:
        # Capturar cualquier error inesperado
        print(f"❌ Error general en el programa: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
