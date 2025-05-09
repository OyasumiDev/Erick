import tkinter as tk
from tkinter import ttk, messagebox
from models.auto_model import AutoModel

auto_model = AutoModel()

def cargar_autos(tree: ttk.Treeview):
    resultado = auto_model.get_all()
    tree.delete(*tree.get_children())

    if resultado["status"] == "success":
        for auto in resultado["data"]:
            tree.insert("", "end", values=(
                auto[0],  # id
                auto[1],  # estado_auto
                auto[2],  # marca_auto
                auto[3],  # num_cilindros
                auto[4],  # anio
                f"${auto[5]:,.2f}"  # precio
            ))
    else:
        messagebox.showerror("Error", f"No se pudieron cargar los autos.\n{resultado['message']}")

def ventana_compras():
    ventana = tk.Toplevel()
    ventana.title("📋 Lista de Autos Disponibles")
    ventana.geometry("800x500")

    label = tk.Label(ventana, text="Autos en venta", font=("Helvetica", 18, "bold"))
    label.pack(pady=10)

    columnas = ("ID", "Estado", "Marca", "Cilindros", "Año", "Precio")
    tree = ttk.Treeview(ventana, columns=columnas, show="headings")

    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    tree.pack(expand=True, fill="both", padx=20, pady=10)

    btn_actualizar = tk.Button(ventana, text="🔄 Recargar", command=lambda: cargar_autos(tree))
    btn_actualizar.pack(pady=5)

    cargar_autos(tree)

# Si quieres probarlo directamente
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    ventana_compras()
    root.mainloop()
