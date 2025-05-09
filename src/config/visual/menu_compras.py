import tkinter as tk
from tkinter import ttk, messagebox
from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO

def ventana_compras():
    ventana = tk.Toplevel()
    ventana.title("Menú de Compras")
    ventana.geometry("700x500")
    ventana.config(bg="#F5F5F5")

    # Centrar ventana
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    # Tabla de autos
    tree = ttk.Treeview(ventana, columns=("ID", "Estado", "Marca", "Cilindros", "Precio"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Estado", text="Estado")
    tree.heading("Marca", text="Marca")
    tree.heading("Cilindros", text="Cilindros")
    tree.heading("Precio", text="Precio")

    tree.column("ID", width=50)
    tree.column("Estado", width=100)
    tree.column("Marca", width=150)
    tree.column("Cilindros", width=100)
    tree.column("Precio", width=100)

    tree.pack(pady=20)

    # Función para cargar autos disponibles
    def cargar_autos():
        db = DatabaseMysql()
        query = f"SELECT * FROM {E_AUTO.TABLE.value}"
        resultado = db.execute_query(query)
        if resultado["status"] == "success":
            for fila in resultado["data"]:
                tree.insert("", "end", values=(fila[0], fila[1], fila[2], fila[3], fila[4]))
        else:
            messagebox.showerror("Error", "No se pudo cargar la lista de autos")

    # Compra por ID
    entrada_id = ttk.Entry(ventana)
    entrada_id.pack(pady=10)
    entrada_id.insert(0, "ID del auto a comprar")

    def comprar_auto():
        id_auto = entrada_id.get()
        if not id_auto.isdigit():
            messagebox.showwarning("Entrada inválida", "Por favor ingresa un ID válido.")
            return

        db = DatabaseMysql()
        delete_query = f"DELETE FROM {E_AUTO.TABLE.value} WHERE {E_AUTO.ID.value} = %s"
        result = db.execute_query(delete_query, (id_auto,))
        if result["status"] == "success" and result["rowcount"] > 0:
            messagebox.showinfo("Compra exitosa", f"Auto con ID {id_auto} comprado.")
            tree.delete(*tree.get_children())
            cargar_autos()
        else:
            messagebox.showerror("Error", f"No se encontró un auto con ID {id_auto}.")

    ttk.Button(ventana, text="Comprar Auto", command=comprar_auto).pack(pady=5)

    cargar_autos()
