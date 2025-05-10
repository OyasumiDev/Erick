import tkinter as tk
from tkinter import ttk
from config.visual.menu_compras import ventana_compras  
from config.visual.menu_ventas import SistemaVentaAutos  

def mostrar_menu():
    """Función para mostrar el menú principal."""
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal")

    # Dimensiones de la ventana principal
    window_width = 1280
    window_height = 720

    # Centrar la ventana en la pantalla
    screen_width = ventana_menu.winfo_screenwidth()
    screen_height = ventana_menu.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    ventana_menu.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    
    ventana_menu.config(bg="#D3D3D3")

    # Frame principal del menú
    frame_menu = ttk.Frame(ventana_menu, padding="40", style="My.TFrame")
    frame_menu.place(relx=0.5, rely=0.5, anchor="center")

    # Estilo visual para los elementos
    style = ttk.Style()
    style.configure("My.TFrame", background="#D3D3D3")
    style.configure("My.TButton", font=("Segoe UI", 14), padding=10)
    style.configure("My.TLabel", background="#D3D3D3", font=("Segoe UI", 24, "bold"))

    # Título del menú
    title_label = ttk.Label(frame_menu, text="Menú Principal", style="My.TLabel")
    title_label.grid(row=0, column=0, pady=(0, 30))

    # Botón para abrir el menú de compras
    ttk.Button(frame_menu, text="1. Menú de Compras", style="My.TButton", width=25, command=ventana_compras).grid(row=1, column=0, pady=10)
    
    # Botón para salir
    ttk.Button(frame_menu, text="Salir", style="My.TButton", width=25, command=ventana_menu.destroy).grid(row=2, column=0, pady=(30, 0))

    # Mostrar la ventana principal
    ventana_menu.mainloop()
