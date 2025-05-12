# src/config/visual/menu_ventas.py

import tkinter as tk
from tkinter import messagebox
from models.auto_model import AutoModel

class SistemaVentaAutos:
    def __init__(self, master):
        self.master = master
        self.master.title("💸 Menú de Ventas")  # Título de la ventana
        self.master.geometry("700x500")  # Tamaño de la ventana

        self.auto_model = AutoModel()  # Instancia del modelo de autos

        # Frame principal para contener los elementos del menú
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Título en el menú
        self.titulo = tk.Label(self.frame, text="Autos Vendidos", font=("Arial", 16))
        self.titulo.pack(pady=10)

        # Lista donde se mostrarán los autos vendidos
        self.lista_autos = tk.Listbox(self.frame, font=("Arial", 12), width=80, height=15)
        self.lista_autos.pack(pady=10)

        # Botón para actualizar la lista de autos vendidos
        self.boton_actualizar = tk.Button(self.frame, text="🔄 Actualizar Lista", command=self.cargar_autos)
        self.boton_actualizar.pack(pady=5)

        # Cargar la lista de autos vendidos al iniciar
        self.cargar_autos()

    def cargar_autos(self):
        """Carga y muestra los autos vendidos desde la base de datos"""
        self.lista_autos.delete(0, tk.END)  # Limpiar la lista antes de actualizar
        autos = self.auto_model.get_autos_vendidos()  # Obtener autos vendidos desde el modelo

        if isinstance(autos, list) and autos:  # Verificar que haya autos vendidos
            self.autos_lista = autos  # Guardar la lista de autos vendidos
            for auto in autos:
                # Mostrar los detalles de cada auto en la lista
                texto = f"ID {auto['id']} | {auto['marca']} | {auto['estado']} | {auto['anio']} | {auto['cilindros']} cil | ${auto['precio']}"
                self.lista_autos.insert(tk.END, texto)  # Insertar auto en la lista
        else:
            # Si no hay autos vendidos, mostrar un mensaje
            messagebox.showinfo("Sin ventas", "No hay autos vendidos.")

    def comprar_auto(self):
        """Simula la compra de un auto (para el menú de compras)"""
        seleccion = self.lista_autos.curselection()  # Verificar si se seleccionó un auto
        if not seleccion:
            messagebox.showwarning("Seleccionar auto", "Selecciona un auto para comprar.")  # Advertencia si no se seleccionó
            return

        # Obtener el auto seleccionado
        index = seleccion[0]
        auto = self.autos_lista[index]
        auto_id = auto['id']

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
