import tkinter as tk

def menu_ventas():
    ventana = tk.Tk()
    ventana.title("Menú Ventas")
    ventana.geometry("800x600")
    ventana.resizable(False, False)

    # Añadir botones y funcionalidades para el menú de ventas
    tk.Label(ventana, text="Menú de Ventas", font=("Arial", 24)).pack(pady=50)

    # Aquí puedes agregar más botones para la gestión de ventas
    ventana.mainloop()
