import tkinter as tk
from tkinter import ttk, messagebox


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

    for col in columnas:
        tree.heading(col, text=col)
        ancho = 100 if col not in ("ID", "Marca", "Precio") else (50 if col == "ID" else 150)
        tree.column(col, width=ancho, anchor="center")

    tree.pack(pady=20, fill="both", expand=True)

    # Botón de recarga
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    btn_actualizar = tk.Button(frame_botones, text="🔄 Recargar autos", command=lambda: cargar_autos(tree))
    btn_actualizar.pack()

    # Carga inicial de autos
    cargar_autos(tree)
