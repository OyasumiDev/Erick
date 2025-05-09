from config.visual.menu_visual import mostrar_menu
from database.database_mysql import DatabaseMysql
from import_db import import_db
from enums.e_autos import E_AUTO
from models.auto_model import AutoModel
from helpers.class_singletone import class_singleton
from config.eliminar_cache import eliminar_pycache  


def resetear_base_datos():
    """Elimina la tabla de autos y la recrea desde cero usando los enums."""
    db = DatabaseMysql()

    try:
        print("🔄 Eliminando tabla anterior (si existe)...")
        drop_query = f"DROP TABLE IF EXISTS {E_AUTO.TABLE.value}"
        db.execute_query(drop_query)

        print("📦 Creando nueva tabla...")
        create_query = f"""
        CREATE TABLE {E_AUTO.TABLE.value} (
            {E_AUTO.ID.value} INT AUTO_INCREMENT PRIMARY KEY,
            {E_AUTO.ESTADO_AUTO.value} ENUM('NUEVO', 'USADOS') NOT NULL,
            {E_AUTO.MARCA_AUTO.value} VARCHAR(100) NOT NULL,
            {E_AUTO.NUM_CILINDROS.value} TINYINT UNSIGNED NOT NULL,
            {E_AUTO.ANIO.value} YEAR NOT NULL,
            {E_AUTO.PRECIO.value} DECIMAL(10, 2) NOT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """
        db.execute_query(create_query)
        print("✅ Tabla creada correctamente.")
    except Exception as e:
        print(f"❌ Error al resetear base de datos: {e}")
    finally:
        db.close()


def main():
    """Punto de entrada del sistema de autos."""
    try:
        # Primero, eliminar el __pycache__
        print("🧹 Limpiando __pycache__...")
        eliminar_pycache()

        print("🔁 Reiniciando base de datos...")
        resetear_base_datos()

        print("📥 Cargando autos por defecto...")
        import_db()

        print("🚗 Iniciando menú visual...")
        mostrar_menu()

    except Exception as e:
        print(f"❌ Error general en el programa: {e}")


if __name__ == "__main__":
    main()
