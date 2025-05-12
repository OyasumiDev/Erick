import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las credenciales de la base de datos desde las variables de entorno
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

def obtener_autos_disponibles():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, estado, marca, cilindros, anio, precio FROM autos")
        autos = cursor.fetchall()
        conn.close()
        return autos
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo obtener autos: {e}")
        return []

def comprar_auto_por_id(tree, id_entry):
    auto_id = id_entry.get()
    if not auto_id.isdigit() or auto_id == "":
        messagebox.showwarning("ID inválido", "Ingrese un ID numérico válido.")
        return

    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM autos WHERE id = %s", (auto_id,))
        
        if cursor.rowcount == 0:
            messagebox.showinfo("No encontrado", f"No existe auto con ID {auto_id}.")
            # No se cierra la ventana de compras, solo el mensaje
        else:
            conn.commit()
            messagebox.showinfo("Compra exitosa", f"Auto con ID {auto_id} comprado.")
            # Actualiza la tabla
            actualizar_tabla(tree)
            
        conn.close()
    except Exception as e:
        # Esto no debería cerrar el menú de compras, solo muestra un error
        messagebox.showerror("Error", f"No se pudo completar la compra: {e}")
        # Esto asegura que la ventana de compras no se cierre


def actualizar_tabla(tree):
    for row in tree.get_children():
        tree.delete(row)
    for auto in obtener_autos_disponibles():
        tree.insert("", "end", values=auto)

def ventana_compras():
    ventana_compras = tk.Toplevel()
    ventana_compras.title("Menú de Compras")
    ventana_compras.geometry("1000x600")
    ventana_compras.config(bg="#D3D3D3")

    style = ttk.Style()
    style.configure("My.TFrame", background="#D3D3D3")
    style.configure("My.TButton", font=("Segoe UI", 12), padding=6, relief="flat")
    style.configure("My.TLabel", background="#D3D3D3", font=("Segoe UI", 16, "bold"))

    # Frame principal
    frame = ttk.Frame(ventana_compras, padding="20", style="My.TFrame")
    frame.pack(fill="both", expand=True)

    title_label = ttk.Label(frame, text="Autos Disponibles", style="My.TLabel")
    title_label.pack(pady=(0, 10))

    # Tabla con autos
    columns = ("ID", "Estado", "Marca", "Cilindros", "Año", "Precio")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")
    tree.pack(fill="both", padx=10, pady=10)
    actualizar_tabla(tree)

    # Entrada de ID
    id_frame = ttk.Frame(frame, style="My.TFrame")
    id_frame.pack(pady=10)
    ttk.Label(id_frame, text="ID del Auto a Comprar:", style="My.TLabel").pack(side="left", padx=5)
    id_entry = ttk.Entry(id_frame)
    id_entry.pack(side="left", padx=5)

    # Función para hacer la compra al presionar Enter
    def comprar_con_enter(event=None):
        comprar_auto_por_id(tree, id_entry)

    # Bind de la tecla Enter
    id_entry.bind("<Return>", comprar_con_enter)

    # Botón de comprar
    ttk.Button(frame, text="Comprar Auto", style="My.TButton",
               command=lambda: comprar_auto_por_id(tree, id_entry)).pack(pady=10)

    # Botón cerrar
    ttk.Button(frame, text="Cerrar", style="My.TButton", command=ventana_compras.destroy).pack(pady=10)

if __name__ == "__main__":
    ventana_compras()
