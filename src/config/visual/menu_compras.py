import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database.database_mysql import DatabaseMysql
from enums.e_autos import E_AUTO

def ventana_compras():
    # Crear la ventana de compras
    ventana_compras = tk.Toplevel()  # Esto crea una nueva ventana hija
    ventana_compras.title("Menú de Compras")
    ventana_compras.geometry("1280x720")
    ventana_compras.config(bg="#D3D3D3")  # Fondo gris claro

    # Centrar la ventana en la pantalla
    screen_width = ventana_compras.winfo_screenwidth()
    screen_height = ventana_compras.winfo_screenheight()
    window_width = 1280
    window_height = 720
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    ventana_compras.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Frame de la ventana
    frame_compras = ttk.Frame(ventana_compras, padding="30", relief="solid", borderwidth=2)
    frame_compras.place(relx=0.5, rely=0.5, anchor="center")

    # Título
    title_label = ttk.Label(frame_compras, text="Menú de Compras", font=("Arial", 24, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Mostrar la base de datos de autos en una tabla
    mostrar_tabla_autos(frame_compras)

    # Botón para comprar un auto
    ttk.Button(frame_compras, text="Comprar Auto", width=20, command=lambda: comprar_auto(ventana_compras)).grid(row=2, column=0, padx=10, pady=10)
    
    # Botón para salir
    ttk.Button(frame_compras, text="Salir", width=20, command=ventana_compras.destroy).grid(row=3, column=0, columnspan=2, pady=10)

    ventana_compras.mainloop()

def mostrar_tabla_autos(frame):
    # Obtener los datos de la base de datos
    db = DatabaseMysql()
    select_query = f"SELECT {E_AUTO.ID.value}, {E_AUTO.ESTADO_AUTO.value}, {E_AUTO.MARCA_AUTO.value}, {E_AUTO.NUM_CILINDROS.value}, {E_AUTO.PRECIO.value} FROM {E_AUTO.TABLE.value}"
    autos = db.execute_query(select_query)

    # Crear un treeview para mostrar los autos en tabla
    tree = ttk.Treeview(frame, columns=("ID", "Estado", "Marca", "Cilindros", "Precio"), show="headings", height=10)
    tree.grid(row=1, column=0, columnspan=2, pady=20)

    # Definir encabezados
    tree.heading("ID", text="ID")
    tree.heading("Estado", text="Estado")
    tree.heading("Marca", text="Marca")
    tree.heading("Cilindros", text="Cilindros")
    tree.heading("Precio", text="Precio")

    # Insertar los datos de los autos en la tabla
    for auto in autos:
        tree.insert("", tk.END, values=auto)

def comprar_auto(ventana_compras):
    # Crear una ventana para seleccionar el auto a comprar
    ventana_seleccion = tk.Toplevel(ventana_compras)
    ventana_seleccion.title("Seleccionar Auto para Comprar")
    ventana_seleccion.geometry("400x200")
    ventana_seleccion.config(bg="#D3D3D3")

    # Centrar la ventana
    screen_width = ventana_seleccion.winfo_screenwidth()
    screen_height = ventana_seleccion.winfo_screenheight()
    window_width = 400
    window_height = 200
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    ventana_seleccion.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Etiqueta de instrucción
    label = ttk.Label(ventana_seleccion, text="Ingrese el ID del auto que desea comprar:", font=("Arial", 14))
    label.pack(pady=20)

    # Entrada para el ID del auto
    entry_id = ttk.Entry(ventana_seleccion, font=("Arial", 14))
    entry_id.pack(pady=10)

    # Función para comprar el auto
    def confirmar_compra():
        auto_id = entry_id.get()
        if not auto_id.isdigit():
            messagebox.showerror("Error", "Por favor, ingrese un ID válido.")
            return

        # Verificar si el auto existe
        db = DatabaseMysql()
        select_query = f"SELECT * FROM {E_AUTO.TABLE.value} WHERE {E_AUTO.ID.value} = {auto_id}"
        result = db.execute_query(select_query)

        if result:
            messagebox.showinfo("Compra exitosa", f"Auto con ID {auto_id} comprado correctamente.")
            ventana_seleccion.destroy()
        else:
            messagebox.showerror("Error", "No se encontró el auto con ese ID.")

    # Botón para confirmar la compra
    ttk.Button(ventana_seleccion, text="Comprar", command=confirmar_compra, width=20).pack(pady=10)

    # Botón para cerrar la ventana de selección
    ttk.Button(ventana_seleccion, text="Cerrar", command=ventana_seleccion.destroy, width=20).pack(pady=10)
