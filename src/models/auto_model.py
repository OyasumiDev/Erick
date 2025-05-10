import tkinter as tk
from tkinter import ttk, messagebox


class AutoModel:
    """Clase que maneja las operaciones con los autos, como obtener la lista de compras."""

    def __init__(self):
        # Aquí puedes inicializar los atributos que necesites
        pass

    def get_compras(self):
        """Simula la obtención de autos desde una base de datos o API."""
        try:
            # Aquí deberías conectar con tu base de datos y obtener los autos
            # El siguiente es un ejemplo simulado de cómo podría ser el formato de los datos:
            return {
                "status": "success",
                "data": [
                    {"id_auto": 1, "estado": "NUEVO", "marca": "Toyota", "cilindros": 4, "anio": 2021, "precio": 25000},
                    {"id_auto": 2, "estado": "USADO", "marca": "Honda", "cilindros": 6, "anio": 2019, "precio": 18000},
                    # Agrega más autos según sea necesario
                ]
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}


def cargar_autos(tree: ttk.Treeview):
    """Carga los autos disponibles en la tabla visual."""
    try:
        tree.delete(*tree.get_children())  # Limpia la tabla

        modelo = AutoModel()
        resultado = modelo.get_compras()

        if resultado["status"] != "success":
            messagebox.showerror("Error", f"No se pudieron cargar los autos: {resultado['message']}")
            return

        for auto in resultado["data"]:
            if not isinstance(auto, dict):
                print(f"⚠️ Auto inválido (esperado dict): {auto}")
                continue

            tree.insert("", "end", values=(
                auto.get("id_auto"),
                auto.get("estado"),
                auto.get("marca"),
                auto.get("cilindros"),
                auto.get("anio"),
                f"${float(auto.get('precio', 0)) :,.2f}"
            ))

    except Exception as e:
        messagebox.showerror("Error crítico", f"❌ Error al cargar autos: {e}")


def ventana_compras():
    """Crea la ventana de compras con tabla de autos y botón para recargar."""
    ventana = tk.Toplevel()
    ventana.title("🛒 Módulo de Compras")
    ventana.geometry("1000x500")

    # Tabla de autos
    columnas = ("ID", "Estado", "Marca", "Cilindros", "Año", "Precio")
    tree = ttk.Treeview(ventana, columns=columnas, show="headings")

    # Definir las cabeceras de la tabla
    for col in columnas:
        tree.heading(col, text=col)
        ancho = 100 if col not in ("ID", "Marca", "Precio") else (50 if col == "ID" else 150)
        tree.column(col, width=ancho, anchor="center")

    # Empaquetar la tabla
    tree.pack(pady=20, fill="both", expand=True)

    # Frame para los botones de la parte inferior
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    # Botón de recarga
    btn_actualizar = tk.Button(frame_botones, text="🔄 Recargar autos", command=lambda: cargar_autos(tree))
    btn_actualizar.pack()

    # Carga inicial de autos (esto se puede omitir si no es necesario)
    # cargar_autos(tree)  # Puedes descomentar esta línea si quieres cargar los autos cuando se abre la ventana
