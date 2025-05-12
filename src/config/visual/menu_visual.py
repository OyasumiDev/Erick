import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from import_db import DatabaseImport
from config.visual.menu_compras import ventana_compras  
from config.visual.menu_ventas import SistemaVentaAutos
from database.reset_db import reset_db  # Importamos la función reset_db

def abrir_menu_ventas():
    ventana_ventas = tk.Toplevel()  # Crea una ventana hija
    SistemaVentaAutos(ventana_ventas)  # Pasa la ventana a la clase

def mostrar_menu():
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal")
    ventana_menu.geometry("1280x720")
    ventana_menu.resizable(False, False)

    # --- Rutas seguras ---
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_perfil_path = os.path.join(BASE_DIR, "assets", "root_user.jpeg")
    img_fondo_path = os.path.join(BASE_DIR, "assets", "fondo_menu.jpg")

    # --- Cargar fondo ---
    try:
        fondo_img = Image.open(img_fondo_path).resize((1280, 720))
        fondo_tk = ImageTk.PhotoImage(fondo_img)
        fondo_label = tk.Label(ventana_menu, image=fondo_tk)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"❌ Error cargando fondo: {e}")
        fondo_label = None

    # --- Cargar imagen de perfil ---
    try:
        imagen_original = Image.open(img_perfil_path)
        imagen_redimensionada = imagen_original.resize((80, 80))
        imagen_usuario = ImageTk.PhotoImage(imagen_redimensionada)
    except Exception as e:
        print(f"❌ Error cargando imagen de usuario: {e}")
        imagen_usuario = None

    # --- Frame del encabezado ---
    header_frame = tk.Frame(ventana_menu, bg="#D3D3D3")
    header_frame.place(x=10, y=10)

    if imagen_usuario:
        img_label = tk.Label(header_frame, image=imagen_usuario, bg="#D3D3D3")
        img_label.image = imagen_usuario  # Mantener una referencia a la imagen
        img_label.pack(side="left", padx=5)

    user_label = tk.Label(header_frame, text="USUARIO: ROOT", font=("Segoe UI", 14, "bold"), bg="#D3D3D3")
    user_label.pack(side="left", padx=10)

    # --- Frame central con botones ---
    frame_menu = ttk.Frame(ventana_menu, padding="40", style="My.TFrame")
    frame_menu.place(relx=0.5, rely=0.5, anchor="center")

    style = ttk.Style()
    style.configure("My.TFrame", background="#D3D3D3")
    style.configure("My.TButton", font=("Segoe UI", 14), padding=10)
    style.configure("My.TLabel", background="#D3D3D3", font=("Segoe UI", 24, "bold"))

    title_label = ttk.Label(frame_menu, text="Menú Principal", style="My.TLabel")
    title_label.grid(row=0, column=0, pady=(0, 30))

    ttk.Button(frame_menu, text="🛒  Menú de Compras", style="My.TButton", width=30, command=ventana_compras).grid(row=1, column=0, pady=10)
    ttk.Button(frame_menu, text="📊  Menú de Ventas", style="My.TButton", width=30, command=abrir_menu_ventas).grid(row=2, column=0, pady=10)
    
    # Botón para resetear la base de datos
    ttk.Button(frame_menu, text="🔄  Resetear Base de Datos", style="My.TButton", width=30, command=reset_db).grid(row=3, column=0, pady=10)

    ttk.Button(frame_menu, text="❌  Salir", style="My.TButton", width=30, command=ventana_menu.destroy).grid(row=4, column=0, pady=(30, 0))

    ventana_menu.mainloop()
