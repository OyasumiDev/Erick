import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
from database.database_mysql import DatabaseMysql

class SistemaVentaAutos:
    
    def __init__(self):
        self.database = DatabaseMysql()  # Asegúrate de que tu clase de base de datos esté configurada
        self.ventana_principal()

    def ventana_principal(self):
        ventana = tk.Tk()
        ventana.title("Sistema de Venta de Autos")
        ventana.geometry("1440x900")
        
        # Menú principal
        label_titulo = tk.Label(ventana, text="Menú Principal de Ventas", font=("Arial", 24))
        label_titulo.pack(pady=20)
        
        # Botón para mostrar autos
        boton_ventas = tk.Button(ventana, text="Mostrar Autos para Venta", command=self.menu_ventas, font=("Arial", 14))
        boton_ventas.pack(pady=10)

        # Botón de salir
        boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, font=("Arial", 14))
        boton_salir.pack(pady=10)

        ventana.mainloop()

    def menu_ventas(self):
        menu_ventas = tk.Toplevel()
        menu_ventas.title("Menú de Ventas")
        menu_ventas.geometry("800x600")

        # Crear un Treeview para mostrar los datos de los autos
        tree = ttk.Treeview(menu_ventas, columns=("Estado", "Marca", "Cilindros", "Año", "Precio"), show="headings")
        
        # Definir las columnas del Treeview
        tree.heading("Estado", text="Estado")
        tree.heading("Marca", text="Marca")
        tree.heading("Cilindros", text="Cilindros")
        tree.heading("Año", text="Año")
        tree.heading("Precio", text="Precio")

        # Obtener los autos de la base de datos
        autos = self.obtener_autos()

        # Llenar el Treeview con los datos de los autos
        for auto in autos:
            tree.insert("", tk.END, values=(auto["estado"], auto["marca"], auto["cilindros"], auto["anio"], auto["precio"]))

        # Mostrar el Treeview en la ventana
        tree.pack(fill=tk.BOTH, expand=True)

        # Botón para cerrar la ventana
        boton_cerrar = tk.Button(menu_ventas, text="Cerrar", command=menu_ventas.destroy)
        boton_cerrar.pack(pady=10)

    def obtener_autos(self):
        query = "SELECT estado, marca, cilindros, anio, precio FROM autos"
        resultado = self.database.get_all(query)
        if resultado["status"] == "success":
            return resultado["data"]
        else:
            return []

# Instancia y ejecución del sistema
if __name__ == "__main__":
    sistema = SistemaVentaAutos()
