from config.visual.menu_visual import mostrar_menu
from database.database_mysql import DatabaseMysql
from database.import_db import import_db
from enums.e_autos import E_AUTO

def resetear_base_datos():
    db = DatabaseMysql()

    drop_query = f"DROP TABLE IF EXISTS {E_AUTO.TABLE.value}"
    db.execute_query(drop_query)

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
        print("🔄 Reiniciando base de datos...")
        resetear_base_datos()
        
        print("📥 Insertando autos por defecto...")
        import_db()
        
        print("🚗 Iniciando sistema visual...")
        mostrar_menu()
    except Exception as e:
        print(f"❌ Error general en el programa: {e}")

if __name__ == "__main__":
    main()
