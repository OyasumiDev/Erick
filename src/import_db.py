from database.database_mysql import DatabaseMysql

class DatabaseImport:
    def import_db(self):
        # Usamos la nueva clase DatabaseMysql con el pool de conexiones
        db = DatabaseMysql()  # Obtén la instancia de la clase con el pool de conexiones
        
        try:
            # Verificamos si la tabla autos está vacía usando el pool de conexiones
            query = "SELECT COUNT(*) FROM autos"
            result = db.run_query(query)  # Ejecutamos la consulta de conteo
            count = result[0][0]  # Extraemos el valor del conteo de registros

            if count > 0:
                print("⚠️ La tabla ya contiene datos. No se insertará nada.")
                return

            # Iniciamos una transacción
            db.run_query("START TRANSACTION;")

            # Lista de autos a insertar (PON LA LISTA AQUÍ)
            autos = [
                    ('NUEVO', 'NISSAN', 6, 2024, 435000.00),
                    ('USADOS', 'NISSAN', 4, 2014, 150000.00),
                    ('NUEVO', 'CHEVROLET', 6, 2023, 410000.00),
                    ('USADOS', 'VOLKSWAGEN', 4, 2012, 120000.00),
                    ('USADOS', 'HONDA', 8, 2015, 175000.00),
                    ('NUEVO', 'TOYOTA', 4, 2024, 425000.00),
                    ('USADOS', 'FORD', 4, 2016, 165000.00),
                    ('NUEVO', 'HYUNDAI', 6, 2023, 400000.00),
                    ('USADOS', 'KIA', 6, 2014, 158000.00),
                    ('USADOS', 'HONDA', 4, 2013, 142000.00),
                    ('NUEVO', 'TOYOTA', 6, 2024, 460000.00),
                    ('USADOS', 'CHEVROLET', 6, 2015, 169000.00),
                    ('USADOS', 'BMW', 8, 2016, 240000.00),
                    ('NUEVO', 'FORD', 4, 2023, 395000.00),
                    ('NUEVO', 'TOYOTA', 4, 2024, 418000.00),
                    ('USADOS', 'KIA', 6, 2014, 160000.00),
                    ('USADOS', 'MERCEDES-BENZ', 6, 2013, 210000.00),
                    ('USADOS', 'NISSAN', 4, 2012, 135000.00),
                    ('NUEVO', 'TESLA', 4, 2024, 680000.00),
                    ('USADOS', 'JEEP', 6, 2015, 178000.00),
                    ('USADOS', 'TOYOTA', 6, 2014, 170000.00),
                    ('NUEVO', 'NISSAN', 4, 2023, 388000.00),
                    ('USADOS', 'FORD', 4, 2013, 145000.00),
                    ('USADOS', 'HONDA', 6, 2016, 185000.00),
                    ('NUEVO', 'BMW', 6, 2024, 640000.00),
                    ('USADOS', 'MITSUBISHI', 6, 2014, 155000.00),
                    ('USADOS', 'CHEVROLET', 4, 2013, 132000.00),
                    ('NUEVO', 'TESLA', 6, 2023, 715000.00),
                    ('USADOS', 'KIA', 6, 2015, 172000.00),
                    ('USADOS', 'FORD', 4, 2012, 130000.00),
                    ('NUEVO', 'MITSUBISHI', 6, 2024, 455000.00),
                    ('USADOS', 'HONDA', 6, 2014, 165000.00),
                    ('USADOS', 'KIA', 4, 2013, 140000.00),
                    ('NUEVO', 'VOLKSWAGEN', 4, 2024, 390000.00),
                    ('USADOS', 'TOYOTA', 6, 2015, 180000.00),
                    ('NUEVO', 'BMW', 8, 2023, 720000.00),
                    ('USADOS', 'HYUNDAI', 6, 2012, 128000.00),
                    ('USADOS', 'MERCEDES-BENZ', 8, 2013, 250000.00),
                    ('USADOS', 'NISSAN', 4, 2014, 145000.00),
                    ('USADOS', 'CHEVROLET', 6, 2015, 160000.00),
                    ('USADOS', 'FORD', 4, 2012, 135000.00),
                    ('NUEVO', 'HONDA', 4, 2024, 399000.00),
                    ('NUEVO', 'TOYOTA', 6, 2023, 470000.00),
                    ('USADOS', 'JEEP', 6, 2016, 190000.00),
                    ('USADOS', 'VOLKSWAGEN', 4, 2013, 138000.00),
                    ('USADOS', 'MITSUBISHI', 6, 2012, 129000.00),
                    ('NUEVO', 'BMW', 8, 2024, 730000.00),
                    ('USADOS', 'MERCEDES-BENZ', 8, 2015, 245000.00),
                    ('USADOS', 'HYUNDAI', 6, 2013, 140000.00),
                    ('USADOS', 'HONDA', 6, 2014, 158000.00),
                    ('NUEVO', 'FORD', 6, 2024, 460000.00),
                    ('USADOS', 'TOYOTA', 4, 2015, 148000.00),
                    ('USADOS', 'HONDA', 6, 2014, 165000.00),
                    ('NUEVO', 'KIA', 6, 2023, 405000.00),
                    ('USADOS', 'CHEVROLET', 6, 2015, 162000.00),
                    ('NUEVO', 'BMW', 4, 2024, 610000.00),
                    ('USADOS', 'VOLKSWAGEN', 6, 2013, 143000.00),
                    ('USADOS', 'TOYOTA', 4, 2012, 125000.00),
                    ('NUEVO', 'HONDA', 8, 2023, 480000.00),
                    ('USADOS', 'MITSUBISHI', 6, 2014, 150000.00),
                    ('NUEVO', 'FORD', 4, 2023, 390000.00),
                    ('USADOS', 'TESLA', 6, 2016, 230000.00),
                    ('NUEVO', 'NISSAN', 4, 2024, 415000.00),
                    ('USADOS', 'HONDA', 6, 2013, 145000.00),
                    ('USADOS', 'FORD', 4, 2015, 158000.00),
                    ('USADOS', 'CHEVROLET', 8, 2014, 198000.00),
                    ('NUEVO', 'HONDA', 6, 2023, 420000.00),
                    ('USADOS', 'MERCEDES-BENZ', 4, 2012, 142000.00),
                    ('NUEVO', 'KIA', 4, 2024, 405000.00),
                    ('USADOS', 'BMW', 6, 2014, 210000.00),
                    ('USADOS', 'TESLA', 8, 2016, 260000.00),
                    ('NUEVO', 'NISSAN', 4, 2023, 408000.00),
                    ('USADOS', 'HYUNDAI', 6, 2015, 160000.00),
                    ('NUEVO', 'FORD', 6, 2024, 455000.00),
                    ('USADOS', 'HONDA', 8, 2013, 190000.00),
                    ('USADOS', 'TOYOTA', 4, 2012, 130000.00),
                    ('NUEVO', 'KIA', 6, 2023, 420000.00),
                    ('USADOS', 'MERCEDES-BENZ', 6, 2014, 200000.00),
                    ('NUEVO', 'VOLKSWAGEN', 6, 2024, 440000.00),
                    ('USADOS', 'CHEVROLET', 4, 2015, 140000.00),
                    ('NUEVO', 'MITSUBISHI', 6, 2023, 432000.00),
                    ('USADOS', 'NISSAN', 4, 2013, 136000.00),
                    ('NUEVO', 'FORD', 8, 2024, 490000.00),
                    ('USADOS', 'HONDA', 4, 2012, 129000.00),
                    ('USADOS', 'KIA', 6, 2014, 162000.00),
                    ('NUEVO', 'BMW', 6, 2024, 645000.00),
                    ('USADOS', 'JEEP', 4, 2013, 135000.00),
                    ('USADOS', 'MERCEDES-BENZ', 4, 2015, 150000.00),
                    ('USADOS', 'TOYOTA', 8, 2014, 185000.00),
                    ('USADOS', 'FORD', 6, 2012, 137000.00),
                    ('NUEVO', 'HONDA', 4, 2023, 395000.00),
                    ('USADOS', 'VOLKSWAGEN', 6, 2015, 172000.00),
                    ('USADOS', 'MITSUBISHI', 4, 2014, 140000.00),
                    ('USADOS', 'CHEVROLET', 8, 2013, 195000.00),
                    ('USADOS', 'NISSAN', 4, 2012, 125000.00),
                    ('NUEVO', 'BMW', 6, 2023, 635000.00),
                    ('USADOS', 'FORD', 6, 2014, 170000.00),
                    ('USADOS', 'HONDA', 4, 2015, 150000.00),
                    ('USADOS', 'TOYOTA', 4, 2013, 138000.00),
                    ('NUEVO', 'HYUNDAI', 6, 2024, 410000.00)
                ]
            # Insertar los autos usando el método run_query
            for auto in autos:
                query = """
                INSERT INTO autos (estado, marca, cilindros, anio, precio)
                VALUES (%s, %s, %s, %s, %s)
                """
                db.run_query(query, auto)  # Insertamos cada auto

            # Confirmamos la transacción
            db.run_query("COMMIT;")
            print("✅ Autos importados correctamente.")
        
        except Exception as e:
            # Si ocurre un error, revertimos la transacción
            db.run_query("ROLLBACK;")
            print(f"❌ Error al importar los autos: {e}")
        
        finally:
            # Cerramos la conexión a la base de datos
            db.close()
