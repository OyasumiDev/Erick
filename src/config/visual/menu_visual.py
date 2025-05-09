import tkinter as tk
from tkinter import messagebox
import csv

def guardar_en_csv(datos, nombre_archivo):
    with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(datos)

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def abrir_compras():
    ventana = tk.Toplevel()
    ventana.title("Compras")
    centrar_ventana(ventana, 600, 400)
    ventana.configure(bg="#e6e6e6")
    tk.Label(ventana, text="📥 Módulo de Compras", font=("Arial", 16), bg="#e6e6e6").pack(pady=30)

def abrir_ventas():
    ventana = tk.Toplevel()
    ventana.title("Ventas")
    centrar_ventana(ventana, 600, 400)
    ventana.configure(bg="#e6e6e6")
    tk.Label(ventana, text="📤 Módulo de Ventas", font=("Arial", 16), bg="#e6e6e6").pack(pady=30)

def salir():
    if messagebox.askokcancel("Salir", "¿Deseas salir del sistema?"):
        ventana_principal.destroy()

def mostrar_menu():
    global ventana_principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Sistema de Autos")
    centrar_ventana(ventana_principal, 1280, 720)
    ventana_principal.configure(bg="#e6e6e6")

    tk.Label(ventana_principal, text="🚗 Menú Principal", font=("Arial", 28), bg="#e6e6e6").pack(pady=40)

    frame_botones = tk.Frame(ventana_principal, bg="#e6e6e6")
    frame_botones.pack(pady=50)

    botones = [
        ("📥 Compras", abrir_compras),
        ("📤 Ventas", abrir_ventas),
        ("❌ Salir", salir),
    ]

    for texto, comando in botones:
        tk.Button(frame_botones, text=texto, width=30, height=2, font=("Arial", 14),
                  command=comando).pack(pady=20)

    ventana_principal.mainloop()
