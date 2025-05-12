import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import getpass

from config.visual.menu_compras import ventana_compras  
from config.visual.menu_ventas import SistemaVentaAutos

def mostrar_menu():
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal")
    ventana_menu.geometry("1280x720")
    ventana_menu.resizable(False, False)

    # Obtener usuario actual del sistema
    usuario_actual = getpass.getuser()

    # --- Rutas ---
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_perfil_path = os.path.join(BASE_DIR, "assets", "root_user.jpeg")
    img_fondo_path = os.path.join(BASE_DIR, "assets", "fondo_menu.jpg")

    # --- Fondo ---
    try:
        fondo_img = Image.open(img_fondo_path).resize((1280, 720))
        fondo_tk = ImageTk.PhotoImage(fondo_img)
        fondo_label = tk.Label(ventana_menu, image=fondo_tk)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"❌ Error cargando fondo: {e}")

    # --- Imagen de usuario ---
    try:
        imagen_original = Image.open(img_perfil_path)
        imagen_redimensionada = imagen_original.resize((80, 80))
        imagen_usuario = ImageTk.PhotoImage(imagen_redimensionada)
    except Exception as e:
        print(f"❌ Error cargando imagen de usuario: {e}")
        imagen_usuario = None

    # --- Frame de usuario ---
    header_frame = tk.Frame(ventana_menu, bg="#000000", bd=0, highlightthickness=0)
    header_frame.place(x=10, y=10)

    if imagen_usuario:
        img_label = tk.Label(header_frame, image=imagen_usuario, bg="#000000")
        img_label.image = imagen_usuario
        img_label.pack(side="left", padx=5)

    user_label = tk.Label(
        header_frame,
        text=f"USUARIO: {usuario_actual.upper()}",
        font=("Segoe UI", 14, "bold"),
        bg="#000000",
        fg="white"
    )
    user_label.pack(side="left", padx=10)

    # --- Menú principal (con fondo simulado como transparente usando color oscuro) ---
    frame_menu = tk.Frame(ventana_menu, bg="#000000")
    frame_menu.place(relx=0.5, rely=0.5, anchor="center")

    title_label = tk.Label(
        frame_menu,
        text="Menú Principal",
        font=("Segoe UI", 24, "bold"),
        bg="#000000",
        fg="white"
    )
    title_label.grid(row=0, column=0, pady=(0, 30))

    # Botones visuales (sin transparencia)
    style = ttk.Style()
    style.configure("My.TButton", font=("Segoe UI", 14), padding=10)

    ttk.Button(frame_menu, text="🛒  Menú de Compras", style="My.TButton", width=30, command=ventana_compras).grid(row=1, column=0, pady=10)
    ttk.Button(frame_menu, text="📊  Menú de Ventas", style="My.TButton", width=30, command=SistemaVentaAutos).grid(row=2, column=0, pady=10)
    ttk.Button(frame_menu, text="❌  Salir", style="My.TButton", width=30, command=ventana_menu.destroy).grid(row=3, column=0, pady=(30, 0))

    ventana_menu.mainloop()
