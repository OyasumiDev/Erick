import tkinter as tk
from tkinter import ttk

def ventana_compras():
    """Ventana para el menú de compras."""
    ventana_compras = tk.Toplevel()  # Crear una nueva ventana
    ventana_compras.title("Menú de Compras")
    
    # Dimensiones de la ventana
    window_width = 800
    window_height = 600

    # Centrar la ventana en la pantalla
    screen_width = ventana_compras.winfo_screenwidth()
    screen_height = ventana_compras.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    ventana_compras.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    
    ventana_compras.config(bg="#D3D3D3")

    # Frame para la ventana de compras
    frame_compras = ttk.Frame(ventana_compras, padding="40", style="My.TFrame")
    frame_compras.place(relx=0.5, rely=0.5, anchor="center")

    # Estilo para los elementos
    style = ttk.Style()
    style.configure("My.TFrame", background="#D3D3D3")
    style.configure("My.TButton", font=("Segoe UI", 14), padding=10)
    style.configure("My.TLabel", background="#D3D3D3", font=("Segoe UI", 24, "bold"))

    # Título de la ventana de compras
    title_label = ttk.Label(frame_compras, text="Menú de Compras", style="My.TLabel")
    title_label.grid(row=0, column=0, pady=(0, 30))

    # Botón de acción en la ventana de compras (por ejemplo, mostrar productos)
    ttk.Button(frame_compras, text="Ver Autos Disponibles", style="My.TButton", width=25, command=lambda: print("Mostrar autos")).grid(row=1, column=0, pady=10)

    # Botón para cerrar la ventana de compras
    ttk.Button(frame_compras, text="Cerrar", style="My.TButton", width=25, command=ventana_compras.destroy).grid(row=2, column=0, pady=(30, 0))

    ventana_compras.mainloop()
