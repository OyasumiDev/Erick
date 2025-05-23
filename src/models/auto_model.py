from enums.e_autos import E_AUTO
from database.database_mysql import DatabaseMysql


class AutoModel:
    def __init__(self):
        self.db = DatabaseMysql()
        self._ensure_table()

    def _ensure_table(self) -> None:
        """Verifica si la tabla de autos existe, y la crea si no."""
        query = """
            SELECT COUNT(*) AS c
            FROM information_schema.tables
            WHERE table_schema = %s AND table_name = %s
        """
        result = self.db.get_one(query, (self.db.database, E_AUTO.TABLE.value))
        if result.get("c", 0) == 0:
            print(f"⚠️ La tabla {E_AUTO.TABLE.value} no existe. Creando...")
            create_query = f"""
                CREATE TABLE IF NOT EXISTS {E_AUTO.TABLE.value} (
                    {E_AUTO.ID.value} INT AUTO_INCREMENT PRIMARY KEY,
                    {E_AUTO.ESTADO_AUTO.value} ENUM('NUEVO', 'USADOS') NOT NULL,
                    {E_AUTO.MARCA_AUTO.value} VARCHAR(100) NOT NULL,
                    {E_AUTO.NUM_CILINDROS.value} TINYINT UNSIGNED NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
            self.db.run_query(create_query)
            print(f"✅ Tabla {E_AUTO.TABLE.value} creada correctamente.")
        else:
            print(f"✔️ La tabla {E_AUTO.TABLE.value} ya existe.")


    def add(self, estado_auto: str, marca: str, cilindros: int) -> dict:
        """Agrega un nuevo auto a la base de datos."""
        query = f"""
            INSERT INTO {E_AUTO.TABLE.value} (
                {E_AUTO.ESTADO_AUTO.value},
                {E_AUTO.MARCA_AUTO.value},
                {E_AUTO.NUM_CILINDROS.value}
            ) VALUES (%s, %s, %s)
        """
        try:
            self.db.run_query(query, (estado_auto, marca, cilindros))
            return {"status": "success", "message": "Auto agregado correctamente"}
        except Exception as ex:
            return {"status": "error", "message": f"Error al agregar auto: {ex}"}

    def get_all(self) -> dict:
        """Obtiene todos los autos registrados."""
        query = f"SELECT * FROM {E_AUTO.TABLE.value} ORDER BY {E_AUTO.ID.value} ASC"
        try:
            data = self.db.get_all(query)
            return {"status": "success", "data": data}
        except Exception as ex:
            return {"status": "error", "message": f"Error al obtener autos: {ex}"}

    def get_by_id(self, auto_id: int) -> dict:
        """Obtiene un auto por su ID."""
        query = f"SELECT * FROM {E_AUTO.TABLE.value} WHERE {E_AUTO.ID.value} = %s"
        try:
            data = self.db.get_one(query, (auto_id,))
            return {"status": "success", "data": data}
        except Exception as ex:
            return {"status": "error", "message": f"Error al obtener auto: {ex}"}
