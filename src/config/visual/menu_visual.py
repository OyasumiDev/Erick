import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from config.visual.menu_compras import ventana_compras  
from config.visual.menu_ventas import SistemaVentaAutos  # Aún no implementado, lo dejamos como espacio

def mostrar_menu():
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal")
    ventana_menu.geometry("1280x720")
    ventana_menu.configure(bg="#D3D3D3")

    # --- Cargar imagen de perfil ---
    try:
        imagen_original = Image.open("config/visual/assets/root_user.png")  # Ruta de tu imagen
        imagen_redimensionada = imagen_original.resize((80, 80))  # Tamaño pequeño-mediano
        imagen_usuario = ImageTk.PhotoImage(imagen_redimensionada)
    except Exception as e:
        print(f"❌ Error cargando imagen: {e}")
        imagen_usuario = None

    # --- Frame del encabezado ---
    header_frame = tk.Frame(ventana_menu, bg="#D3D3D3")
    header_frame.place(x=10, y=10)

    if imagen_usuario:
        img_label = tk.Label(header_frame, image=imagen_usuario, bg="#D3D3D3")
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

    # Botones funcionales
    ttk.Button(frame_menu, text="🛒  Menú de Compras", style="My.TButton", width=30, command=ventana_compras).grid(row=1, column=0, pady=10)
    ttk.Button(frame_menu, text="📊  Menú de Ventas", style="My.TButton", width=30, command=SistemaVentaAutos).grid(row=2, column=0, pady=10)
    ttk.Button(frame_menu, text="❌  Salir", style="My.TButton", width=30, command=ventana_menu.destroy).grid(row=3, column=0, pady=(30, 0))

    ventana_menu.mainloop()
