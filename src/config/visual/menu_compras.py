import tkinter as tk
from tkinter import ttk
from models.auto_model import AutoModel

def cargar_autos(tree):
    tree.delete(*tree.get_children())  # Limpia la tabla

    modelo = AutoModel()
    resultado = modelo.get_compras()

    if resultado["status"] != "success":
        print(f"❌ Error al obtener autos: {resultado['message']}")
        return

    for auto in resultado["data"]:
        try:
            print(f"📦 Auto leído: {auto}")

            if not isinstance(auto, (list, tuple)) or len(auto) < 6:
                print(f"⚠️ Auto inválido (esperado 6 elementos): {auto}")
                continue

            tree.insert("", "end", values=(
                auto[0],  # ID
                auto[1],  # Estado
                auto[2],  # Marca
                auto[3],  # Cilindros
                auto[4],  # Año
                f"${float(auto[5]):,.2f}"  # Precio formateado
            ))
        except Exception as e:
            print(f"❌ Error al cargar auto: {e}")

def ventana_compras():
    ventana = tk.Toplevel()
    ventana.title("🛒 Módulo de Compras")
    ventana.geometry("1000x500")

    tree = ttk.Treeview(ventana, columns=("ID", "Estado", "Marca", "Cilindros", "Año", "Precio"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Estado", text="Estado")
    tree.heading("Marca", text="Marca")
    tree.heading("Cilindros", text="Cilindros")
    tree.heading("Año", text="Año")
    tree.heading("Precio", text="Precio")

    tree.column("ID", width=50)
    tree.column("Estado", width=100)
    tree.column("Marca", width=150)
    tree.column("Cilindros", width=80)
    tree.column("Año", width=80)
    tree.column("Precio", width=100)

    tree.pack(pady=20, fill="both", expand=True)

    btn_actualizar = tk.Button(ventana, text="🔄 Recargar", command=lambda: cargar_autos(tree))
    btn_actualizar.pack(pady=10)

    cargar_autos(tree)
