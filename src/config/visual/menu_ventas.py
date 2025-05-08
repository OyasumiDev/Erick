import tkinter as tk
from tkinter import messagebox

def menu_ventas():
    def registrar_venta():
        messagebox.showinfo("Registrar", "Registrar nueva venta")

    def consultar_ventas():
        messagebox.showinfo("Consultar", "Consultar ventas realizadas")

    def regresar():
        ventana.destroy()
        from config.visual.menu_visual import menu
        menu()

    ventana = tk.Tk()
    ventana.title("Menú de Ventas")
    ventana.geometry("1200x800")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Menú de Ventas", font=("Arial", 32)).pack(pady=50)

    tk.Button(ventana, text="Registrar Venta", width=40, height=2, font=("Arial", 16), command=registrar_venta).pack(pady=15)
    tk.Button(ventana, text="Consultar Ventas", width=40, height=2, font=("Arial", 16), command=consultar_ventas).pack(pady=15)
    tk.Button(ventana, text="Regresar al Menú Principal", width=40, height=2, font=("Arial", 16), command=regresar).pack(pady=50)

    ventana.mainloop()
