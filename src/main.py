from database.database_mysql import DatabaseMysql
from config.visual.menu_visual import menu
from enums.e_autos import E_AUTO

def resetear_base_datos():
    db = DatabaseMysql()
    try:
        # Elimina la tabla si existe
        drop_query = f"DROP TABLE IF EXISTS {E_AUTO.TABLE.value}"
        db.run_query(drop_query)
        print("🧨 Tabla eliminada correctamente")

        # Recrea la tabla usando AutoModel (si la tienes definida así)
        from models.auto_model import AutoModel
        AutoModel()
        print("✅ Tabla recreada correctamente")
    except Exception as e:
        print(f"❌ Error reseteando la base de datos: {e}")

if __name__ == "__main__":
    resetear_base_datos()  # Esto resetea la base
    menu()  # Esto abre el menú visual
