# src/config/visual/menu_ventas.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from models.auto_model import AutoModel

class SistemaVentaAutos:
    def __init__(self, master):
        self.master = master
        self.master.title("💸 Menú de Ventas")  # Título de la ventana
        self.master.geometry("800x600")  # Tamaño de la ventana

        self.auto_model = AutoModel()  # Instancia del modelo de autos

        # Frame principal para contener los elementos del menú
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Título en el menú
        self.titulo = tk.Label(self.frame, text="Autos Vendidos", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Crear un Treeview (tabla) para mostrar los autos vendidos
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Marca", "Estado", "Año", "Cilindrada", "Precio"), show="headings", height=15)
        self.tree.pack(pady=10)

        # Configuración de los encabezados de la tabla
        self.tree.heading("ID", text="ID")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Año", text="Año")
        self.tree.heading("Cilindrada", text="Cilindrada (cil)")
        self.tree.heading("Precio", text="Precio ($)")

        # Ajustar el ancho de las columnas
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Marca", width=150, anchor="w")
        self.tree.column("Estado", width=100, anchor="w")
        self.tree.column("Año", width=80, anchor="center")
        self.tree.column("Cilindrada", width=100, anchor="center")
        self.tree.column("Precio", width=120, anchor="e")

        # Botón para actualizar la lista de autos vendidos
        self.boton_actualizar = tk.Button(self.frame, text="🔄 Actualizar Lista", command=self.cargar_autos)
        self.boton_actualizar.pack(pady=5)

        # Cargar la lista de autos vendidos al iniciar
        self.cargar_autos()

    def cargar_autos(self):
        """Carga y muestra los autos vendidos desde la base de datos"""
        # Limpiar la tabla antes de actualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        autos = self.auto_model.get_autos_vendidos()  # Obtener autos vendidos desde el modelo

        if isinstance(autos, list) and autos:  # Verificar que haya autos vendidos
            self.autos_lista = autos  # Guardar la lista de autos vendidos
            for auto in autos:
                # Insertar los datos de cada auto en la tabla
                self.tree.insert("", tk.END, values=(auto[0], auto[2], auto[1], auto[4], auto[3], f"${auto[5]:,.2f}"))
        else:
            # Si no hay autos vendidos, mostrar un mensaje
            messagebox.showinfo("Sin ventas", "No hay autos vendidos.")

    def comprar_auto(self):
        """Simula la compra de un auto (para el menú de compras)"""
        seleccion = self.tree.selection()  # Verificar si se seleccionó un auto
        if not seleccion:
            messagebox.showwarning("Seleccionar auto", "Selecciona un auto para comprar.")  # Advertencia si no se seleccionó
            return

        # Obtener el auto seleccionado
        item = seleccion[0]
        auto = self.tree.item(item)["values"]
        auto_id = auto[0]  # Accedemos al ID usando el valor de la tupla

        # Confirmación para comprar el auto
        confirmacion = messagebox.askyesno("Confirmar compra", f"¿Seguro que deseas comprar el auto ID {auto_id}?")
        if confirmacion:
            # Si se confirma, eliminar el auto de la tabla `autos` (para marcarlo como vendido)
            query = "DELETE FROM autos WHERE id = %s"
            try:
                self.auto_model.db.execute_query(query, (auto_id,))  # Ejecutar la consulta para eliminar el auto
                messagebox.showinfo("Compra realizada", f"Auto ID {auto_id} comprado con éxito.")  # Confirmación de compra exitosa
                self.cargar_autos()  # Actualizar la lista de autos vendidos
            except Exception as e:
                # Manejo de errores en caso de que la compra falle
                messagebox.showerror("Error", f"No se pudo realizar la compra: {e}")
