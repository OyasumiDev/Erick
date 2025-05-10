import tkinter as tk
from tkinter import ttk, messagebox
from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO

class AutoModel:
    """Clase que maneja las operaciones relacionadas con autos."""

    def __init__(self):
        self.db = DatabaseMysql()

    def obtener_autos_nuevos(self):
        """Obtiene la lista de autos con estado 'NUEVO' desde la base de datos."""
        try:
            query = f"""
                SELECT id_auto, estado, marca, cilindros, anio, precio
                FROM {E_AUTO.TABLE.value}
                WHERE estado = %s
            """
            params = ("NUEVO",)
            result = self.db.get_all(query, params)

            if result["status"] == "success":
                return result
            else:
                raise Exception(result["message"])

        except Exception as e:
            return {"status": "error", "message": str(e)}

def cargar_autos_en_tabla(treeview: ttk.Treeview):
    """Carga los autos nuevos en el widget Treeview."""
    try:
        treeview.delete(*treeview.get_children())

        modelo = AutoModel()
        resultado = modelo.obtener_autos_nuevos()

        if resultado["status"] != "success":
            messagebox.showerror("Error", f"No se pudieron cargar los autos: {resultado['message']}")
            return

        for auto in resultado["data"]:
            if not isinstance(auto, dict):
                print(f"[ADVERTENCIA] Formato inválido: {auto}")
                continue

            treeview.insert("", "end", values=(
                auto.get("id_auto"),
                auto.get("estado"),
                auto.get("marca"),
                auto.get("cilindros"),
                auto.get("anio"),
                f"${float(auto.get('precio', 0)):,.2f}"
            ))

    except Exception as e:
        messagebox.showerror("Error crítico", f"Error al cargar autos: {e}")

def mostrar_ventana_compras():
    """Crea y muestra la ventana del módulo de compras."""
    ventana = tk.Toplevel()
    ventana.title("Módulo de Compras")
    ventana.geometry("1000x500")

    columnas = ("ID", "Estado", "Marca", "Cilindros", "Año", "Precio")
    tree = ttk.Treeview(ventana, columns=columnas, show="headings")

    for col in columnas:
        ancho = 100
        if col == "ID":
            ancho = 50
        elif col in ("Marca", "Precio"):
            ancho = 150
        tree.heading(col, text=col)
        tree.column(col, width=ancho, anchor="center")

    tree.pack(pady=20, fill="both", expand=True)

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    btn_actualizar = tk.Button(frame_botones, text="Recargar autos", command=lambda: cargar_autos_en_tabla(tree))
    btn_actualizar.pack()

    # Carga inicial opcional
    cargar_autos_en_tabla(tree)
