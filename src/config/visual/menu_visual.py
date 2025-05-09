import tkinter as tk
from tkinter import ttk
from menu_compras import ventana_compras  
from menu_ventas import ventana_ventas  

def mostrar_menu():
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal")
    ventana_menu.geometry("1280x720")
    ventana_menu.config(bg="#D3D3D3")

    # Centrar la ventana
    screen_width = ventana_menu.winfo_screenwidth()
    screen_height = ventana_menu.winfo_screenheight()
    window_width = 1280
    window_height = 720
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    ventana_menu.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Frame principal
    frame_menu = ttk.Frame(ventana_menu, padding="30", relief="solid", borderwidth=2)
    frame_menu.place(relx=0.5, rely=0.5, anchor="center")

    # Título
    title_label = ttk.Label(frame_menu, text="Menú Principal", font=("Arial", 24, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Botón para abrir el menú de compras
    ttk.Button(frame_menu, text="Menú de Compras", width=20, command=ventana_compras).grid(row=1, column=0, padx=10, pady=10)
    
    # Botón para abrir el menú de ventas
    ttk.Button(frame_menu, text="Menú de Ventas", width=20, command=ventana_ventas).grid(row=2, column=0, padx=10, pady=10)
    
    # Botón para salir
    ttk.Button(frame_menu, text="Salir", width=20, command=ventana_menu.destroy).grid(row=3, column=0, columnspan=2, pady=10)

    ventana_menu.mainloop()
