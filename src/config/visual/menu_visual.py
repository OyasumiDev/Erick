
import tkinter as tk
from tkinter import messagebox

def menu():
    def abrir_compras():
        # Importa menu_compras aquí, de forma local, para evitar la importación circular
        from config.visual.menu_compras import menu_compras
        ventana.destroy()
        menu_compras()

    def abrir_ventas():
        ventana.destroy()
        menu_ventas()

    def abrir_proveedores():
        messagebox.showinfo("Proveedores", "Aquí va el módulo de Proveedores")

    def salir():
        ventana.destroy()

    ventana = tk.Tk()
    ventana.title("Menú Principal")
    ventana.geometry("1200x800")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Menú Principal", font=("Arial", 32)).pack(pady=50)

    tk.Button(ventana, text="Compras", width=40, height=2, font=("Arial", 16), command=abrir_compras).pack(pady=15)
    tk.Button(ventana, text="Ventas", width=40, height=2, font=("Arial", 16), command=abrir_ventas).pack(pady=15)
    tk.Button(ventana, text="Proveedores", width=40, height=2, font=("Arial", 16), command=abrir_proveedores).pack(pady=15)
    tk.Button(ventana, text="Salir", width=40, height=2, font=("Arial", 16), command=salir).pack(pady=50)

    ventana.mainloop()
