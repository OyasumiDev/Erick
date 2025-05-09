# src/config/visual/menu_compras.py
import tkinter as tk
from tkinter import ttk, messagebox
from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO

def menu_compras():
    db = DatabaseMysql()
    
    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Menú de Compras")
    ventana.state('zoomed')  # Pantalla completa

    # Título
    tk.Label(ventana, text="Compras de Autos", font=("Helvetica", 24, "bold")).pack(pady=20)

    # Frame para tabla
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(fill=tk.BOTH, expand=True, padx=20)

    # Treeview
    columnas = ("ID", "Estado", "Marca", "Cilindros", "Precio")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=15)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor=tk.CENTER, width=100)
    tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scroll
    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Cargar datos desde la base
    def cargar_autos():
        tabla.delete(*tabla.get_children())
        autos = db.get_all(f"SELECT * FROM {E_AUTO.TABLE.value}")
        for auto in autos:
            tabla.insert("", tk.END, values=(
                auto[E_AUTO.ID.value],
                auto[E_AUTO.ESTADO_AUTO.value],
                auto[E_AUTO.MARCA_AUTO.value],
                auto[E_AUTO.NUM_CILINDROS.value],
                f"${auto[E_AUTO.PRECIO.value]:,.2f}"
            ))

    cargar_autos()

    # Frame de compra
    frame_compra = tk.Frame(ventana)
    frame_compra.pack(pady=20)

    tk.Label(frame_compra, text="Ingrese ID del auto a comprar:", font=("Arial", 14)).grid(row=0, column=0, padx=10)
    entrada_id = tk.Entry(frame_compra, font=("Arial", 14))
    entrada_id.grid(row=0, column=1, padx=10)

    def comprar_auto():
        id_auto = entrada_id.get()
        if not id_auto.isdigit():
            messagebox.showerror("Error", "Debe ingresar un ID válido.")
            return

        auto = db.get_one(
            f"SELECT * FROM {E_AUTO.TABLE.value} WHERE {E_AUTO.ID.value} = %s", 
            (int(id_auto),)
        )
        if auto:
            db.run_query(f"DELETE FROM {E_AUTO.TABLE.value} WHERE {E_AUTO.ID.value} = %s", (int(id_auto),))
            messagebox.showinfo("Compra realizada", f"Auto con ID {id_auto} comprado exitosamente.")
            cargar_autos()
        else:
            messagebox.showerror("Error", "No se encontró un auto con ese ID.")

    tk.Button(frame_compra, text="Comprar", font=("Arial", 14), command=comprar_auto).grid(row=0, column=2, padx=10)

    # Botón para volver
    def volver_menu():
        ventana.destroy()
        from config.visual.menu_visual import menu
        menu()

    tk.Button(ventana, text="Volver al menú principal", font=("Arial", 12), command=volver_menu).pack(pady=10)

    ventana.mainloop()
