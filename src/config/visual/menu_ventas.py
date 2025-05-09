# config/visual/ventas.py

import tkinter as tk
from tkinter import ttk, messagebox
from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO

def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def obtener_autos():
    db = DatabaseMysql()
    query = f"SELECT * FROM {E_AUTO.TABLE.value}"
    resultado = db.execute_query(query)
    return resultado.get("data", [])

def cargar_tabla(tabla):
    for row in tabla.get_children():
        tabla.delete(row)
    autos = obtener_autos()
    for auto in autos:
        tabla.insert("", "end", values=(
            auto[E_AUTO.ID.value],
            auto[E_AUTO.ESTADO_AUTO.value],
            auto[E_AUTO.MARCA_AUTO.value],
            auto[E_AUTO.NUM_CILINDROS.value],
            f"${auto[E_AUTO.PRECIO.value]:,.2f}"
        ))

def comprar_auto(entrada_id, tabla):
    try:
        auto_id = int(entrada_id.get())
        db = DatabaseMysql()
        # Verificar si existe
        check_query = f"SELECT * FROM {E_AUTO.TABLE.value} WHERE {E_AUTO.ID.value} = %s"
        result = db.execute_query(check_query, (auto_id,))
        if not result["data"]:
            messagebox.showerror("Error", f"No existe un auto con ID {auto_id}.")
            return
        # Eliminar (simula compra)
        delete_query = f"DELETE FROM {E_AUTO.TABLE.value} WHERE {E_AUTO.ID.value} = %s"
        db.execute_query(delete_query, (auto_id,))
        messagebox.showinfo("Éxito", f"Auto con ID {auto_id} comprado.")
        cargar_tabla(tabla)
        entrada_id.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Debes ingresar un número válido.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def ventana_ventas():
    ventana = tk.Toplevel()
    ventana.title("Ventas")
    ventana.configure(bg="#dcdcdc")
    centrar_ventana(ventana, 1000, 600)

    # Tabla
    columnas = ("ID", "Estado", "Marca", "Cilindros", "Precio")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=15)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150, anchor="center")
    tabla.pack(pady=20)

    cargar_tabla(tabla)

    # Input para comprar
    frame = ttk.LabelFrame(ventana, text="Comprar Auto", padding=20)
    frame.pack(pady=10)

    ttk.Label(frame, text="ID del auto a comprar:").grid(row=0, column=0, padx=10)
    entrada_id = ttk.Entry(frame, width=10)
    entrada_id.grid(row=0, column=1, padx=10)

    btn_comprar = ttk.Button(frame, text="Comprar", command=lambda: comprar_auto(entrada_id, tabla))
    btn_comprar.grid(row=0, column=2, padx=10)

    # Botón cerrar
    ttk.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=10)
