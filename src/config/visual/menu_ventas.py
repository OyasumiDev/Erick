import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database.database_mysql import DatabaseMysql

class SistemaVentaAutos:
    
    def __init__(self):
        self.database = DatabaseMysql()  # Asegúrate de que tu clase de base de datos esté configurada
        self.menu_ventas()

    def menu_ventas(self):
        # Aquí directamente mostramos la ventana con la tabla de autos vendidos, sin abrir una ventana adicional
        self.ventana_ventas = tk.Tk()
        self.ventana_ventas.title("Autos Vendidos")
        self.ventana_ventas.geometry("1280x720")  # Tamaño pequeño de ventana
        
        self.ventana_ventas.config(bg="#f2f2f2")
        
        # Título de la tabla
        label_titulo_ventas = tk.Label(self.ventana_ventas, text="Autos Vendidos", font=("Arial", 20, "bold"), bg="#f2f2f2", fg="#333")
        label_titulo_ventas.pack(pady=20)

        # Crear un Treeview para mostrar los datos de los autos vendidos
        self.tree = ttk.Treeview(self.ventana_ventas, columns=("ID", "Estado", "Marca", "Cilindros", "Año", "Precio", "Fecha de Venta"), show="headings")
        
        # Estilo para la tabla
        self.tree.heading("ID", text="ID")
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Marca", text="Marca")
        self.tree.heading("Cilindros", text="Cilindros")
        self.tree.heading("Año", text="Año")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Fecha de Venta", text="Fecha de Venta")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Estado", width=100, anchor="center")
        self.tree.column("Marca", width=150, anchor="center")
        self.tree.column("Cilindros", width=100, anchor="center")
        self.tree.column("Año", width=100, anchor="center")
        self.tree.column("Precio", width=100, anchor="center")
        self.tree.column("Fecha de Venta", width=150, anchor="center")

        # Obtener los autos vendidos de la base de datos
        autos_vendidos = self.obtener_autos_vendidos()

        # Llenar el Treeview con los datos de los autos vendidos
        for auto in autos_vendidos:
            self.tree.insert("", tk.END, values=(auto["auto_id"], auto["estado"], auto["marca"], auto["cilindros"], auto["anio"], auto["precio"], auto["fecha_venta"]))

        # Mostrar el Treeview en la ventana
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Botón para cerrar la ventana, centrado en la parte inferior
        boton_cerrar = tk.Button(self.ventana_ventas, text="Cerrar", command=self.ventana_ventas.destroy, font=("Arial", 14), bg="#FF5733", fg="white", relief="raised", bd=3)
        boton_cerrar.pack(side="bottom", pady=20, padx=20, anchor="center")

        # Botón para actualizar datos
        boton_actualizar = tk.Button(self.ventana_ventas, text="Actualizar", command=self.actualizar_auto, font=("Arial", 14), bg="#33B5FF", fg="white", relief="raised", bd=3)
        boton_actualizar.pack(side="bottom", pady=20, padx=20, anchor="center")

        self.ventana_ventas.mainloop()

    def obtener_autos_vendidos(self):
        # Ajusté el método para devolver correctamente los resultados como lista de diccionarios
        query = "SELECT auto_id, estado, marca, cilindros, anio, precio, fecha_venta FROM ventas"
        resultado = self.database.get_all(query)
        if isinstance(resultado, list):  # Verificar que el resultado sea una lista
            return resultado
        else:
            messagebox.showerror("Error", "Error al obtener autos vendidos.")
            return []

    def actualizar_auto(self):
        # Obtener el ID del auto seleccionado
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showerror("Error", "Por favor, selecciona un auto para actualizar.")
            return
        
        auto_id = self.tree.item(seleccionado[0])['values'][0]  # Obtener el ID del auto seleccionado

        # Crear ventana emergente para editar los datos del auto
        self.ventana_actualizacion = tk.Toplevel(self.ventana_ventas)
        self.ventana_actualizacion.title("Actualizar Auto")
        self.ventana_actualizacion.geometry("400x300")
        
        # Etiquetas y campos de entrada para actualizar los datos del auto
        tk.Label(self.ventana_actualizacion, text="Estado").pack(pady=5)
        entry_estado = tk.Entry(self.ventana_actualizacion)
        entry_estado.pack(pady=5)
        
        tk.Label(self.ventana_actualizacion, text="Marca").pack(pady=5)
        entry_marca = tk.Entry(self.ventana_actualizacion)
        entry_marca.pack(pady=5)
        
        tk.Label(self.ventana_actualizacion, text="Cilindros").pack(pady=5)
        entry_cilindros = tk.Entry(self.ventana_actualizacion)
        entry_cilindros.pack(pady=5)
        
        tk.Label(self.ventana_actualizacion, text="Año").pack(pady=5)
        entry_anio = tk.Entry(self.ventana_actualizacion)
        entry_anio.pack(pady=5)
        
        tk.Label(self.ventana_actualizacion, text="Precio").pack(pady=5)
        entry_precio = tk.Entry(self.ventana_actualizacion)
        entry_precio.pack(pady=5)
        
        # Función para actualizar los datos en la base de datos
        def actualizar_en_base_de_datos():
            estado = entry_estado.get()
            marca = entry_marca.get()
            cilindros = entry_cilindros.get()
            anio = entry_anio.get()
            precio = entry_precio.get()

            if not (estado and marca and cilindros and anio and precio):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            # Ejecutar la actualización en la base de datos
            query = f"""
                UPDATE ventas
                SET estado = '{estado}', marca = '{marca}', cilindros = {cilindros}, anio = {anio}, precio = {precio}
                WHERE auto_id = {auto_id}
            """
            resultado = self.database.execute_query(query)
            if resultado:
                messagebox.showinfo("Éxito", "Auto actualizado correctamente.")
                self.ventana_actualizacion.destroy()
                self.menu_ventas()  # Volver a cargar la lista de autos actualizada
            else:
                messagebox.showerror("Error", "No se pudo actualizar el auto.")
        
        # Botón para confirmar la actualización
        boton_actualizar_db = tk.Button(self.ventana_actualizacion, text="Actualizar", command=actualizar_en_base_de_datos)
        boton_actualizar_db.pack(pady=20)

# Instancia y ejecución del sistema
if __name__ == "__main__":
    sistema = SistemaVentaAutos()
