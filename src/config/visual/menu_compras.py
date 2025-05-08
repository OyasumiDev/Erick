import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from enums.e_autos import E_AUTO
from database.database_mysql import DatabaseMysql
from config.visual.menu_visual import menu

class AutoModel:
    def __init__(self):
        self.db = DatabaseMysql()
    
    def get_all(self) -> dict:
        """Obtiene todos los autos registrados."""
        query = f"SELECT * FROM {E_AUTO.TABLE.value} ORDER BY {E_AUTO.ID.value} ASC"
        try:
            data = self.db.get_all(query)
            return {"status": "success", "data": data}
        except Exception as ex:
            return {"status": "error", "message": f"Error al obtener autos: {ex}"}

def menu_compras():
    def registrar_compra():
        messagebox.showinfo("Registrar", "Registrar nueva compra")

    def consultar_compras():
        # Aquí mostramos los autos registrados en la base de datos
        result = auto_model.get_all()
        if result["status"] == "success":
            mostrar_compras(result["data"])
        else:
            messagebox.showerror("Error", result["message"])

    def mostrar_compras(compras):
        # Crear una nueva ventana para mostrar las compras en formato tabla
        ventana_compras = tk.Toplevel()
        ventana_compras.title("Consultar Compras")
        ventana_compras.geometry("1200x800")
        
        # Crear la tabla
        tree = ttk.Treeview(ventana_compras, columns=("ID", "Estado", "Marca", "Cilindros"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Estado", text="Estado")
        tree.heading("Marca", text="Marca")
        tree.heading("Cilindros", text="Cilindros")
        
        # Insertar los datos de la base de datos en la tabla
        for compra in compras:
            tree.insert("", tk.END, values=(compra[E_AUTO.ID.value], compra[E_AUTO.ESTADO_AUTO.value], compra[E_AUTO.MARCA_AUTO.value], compra[E_AUTO.NUM_CILINDROS.value]))
        
        tree.pack(pady=20)

    def regresar():
        ventana.destroy()
        menu()

    ventana = tk.Tk()
    ventana.title("Menú de Compras")
    ventana.geometry("1200x800")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Menú de Compras", font=("Arial", 32)).pack(pady=50)

    tk.Button(ventana, text="Registrar Compra", width=40, height=2, font=("Arial", 16), command=registrar_compra).pack(pady=15)
    tk.Button(ventana, text="Consultar Compras", width=40, height=2, font=("Arial", 16), command=consultar_compras).pack(pady=15)
    tk.Button(ventana, text="Regresar al Menú Principal", width=40, height=2, font=("Arial", 16), command=regresar).pack(pady=50)

    ventana.mainloop()

# Crear la instancia del modelo AutoModel
auto_model = AutoModel()
