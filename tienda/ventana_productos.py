import tkinter as tk
from tkinter import messagebox, ttk
import json
from models.producto import Productos

class Ventana_productos:
    def __init__(self):
        self.mis_productos = Productos()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Productos")
        self.ventana.geometry("700x500")
        self.frame_entrada = tk.Frame(self.ventana,padx=10,pady=10)
        self.frame_botones = tk.Frame(self.ventana,padx=10,pady=10)
        self.frame_salida = tk.Frame(self.ventana,padx=10,pady=10)
        self.crear_entrada()
        self.frame_entrada.pack()
        self.crear_botones()
        self.frame_botones.pack()
        self.crear_salida()
        self.frame_salida.pack()
        self.ventana.mainloop()
        
    def __del__(self):
        self.mis_productos = None
        
    def crear_entrada(self):
        tk.Label(self.frame_entrada, text="Id:", width=10).grid(row=0,column=0, padx=10, pady=5, sticky="w")
        self.entrada_id = tk.Entry(self.frame_entrada, width=30)
        self.entrada_id.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.frame_entrada, text="Nombre:", width=10).grid(row=1,column=0, pady=5, sticky="w")
        self.entrada_nombre = tk.Entry(self.frame_entrada, width=30)
        self.entrada_nombre.grid(row=1, column=1, pady=5)
        tk.Label(self.frame_entrada, text="Precio:", width=10).grid(row=2,column=0, pady=5, sticky="w")
        self.entrada_precio = tk.Entry(self.frame_entrada, width=30)
        self.entrada_precio.grid(row=2, column=1, pady=5)
        tk.Label(self.frame_entrada, text="Stock:", width=10).grid(row=3,column=0, pady=5, sticky="w")
        self.entrada_stock = tk.Entry(self.frame_entrada, width=30)
        self.entrada_stock.grid(row=3, column=1, pady=5)
    
    def crear_botones(self):
        estilo = ttk.Style()
        estilo.configure('TButton', font=('Helvetica', 10), padding=5)
        ttk.Button(self.frame_botones, text="Agregar", command=self.agregar_producto).grid(row=0,column=0,padx=5)
        ttk.Button(self.frame_botones, text="Buscar", command=self.buscar_producto).grid(row=0,column=1,padx=5)
        ttk.Button(self.frame_botones, text="Modificar", command=self.modificar_producto).grid(row=0,column=2,padx=5)
        ttk.Button(self.frame_botones, text="Borrar", command=self.borrar_producto).grid(row=0,column=3,padx=5)
        ttk.Button(self.frame_botones, text="Listar", command=self.listar_producto).grid(row=0,column=4,padx=5)
        ttk.Button(self.frame_botones, text="Limpiar", command=self.limpiar_producto).grid(row=0,column=5,padx=5)

    def crear_salida(self):
        self.salida_texto = tk.Text(self.frame_salida, wrap="word", state="disabled")
        self.salida_texto.pack(expand=True, fill="both")
    
    def mostrar_mensaje(self, mensaje):
        self.salida_texto.config(state="normal")
        self.salida_texto.delete("1.0", tk.END)
        self.salida_texto.insert(tk.END, mensaje)
        self.salida_texto.config(state="disabled")
    
    def obtener_datos(self):
        id = self.entrada_id.get()
        nombre = self.entrada_nombre.get()
        try:
            precio = float(self.entrada_precio.get())
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número!")
            return None
        try:
            stock = float(self.entrada_stock.get())
        except ValueError:
            messagebox.showerror("Error", "El stock debe ser un número!")
            return None
        return {"id": id, "nombre": nombre, "precio":precio, "stock": stock}
        
    def agregar_producto(self):
        productos = self.obtener_datos()
        if productos:
            resultado = self.mis_productos.buscar(productos["id"])
            if resultado["id"]=="No encontrado":
                self.mis_productos.agregar(productos)
                self.mostrar_mensaje("productos agregado con éxito!")
                self.limpiar_producto()
            else:
                self.mostrar_mensaje("Id de productos ya existe!")

    def buscar_producto(self):
        id = self.entrada_id.get()
        if id!="":
            resultado = self.mis_productos.buscar(id)
            if resultado["id"]=="No encontrado":
                self.mostrar_mensaje("Id de producto no existe!")
            else:
                self.limpiar_producto()
                self.entrada_id.insert(0,resultado["id"])                     
                self.entrada_nombre.insert(0,resultado["nombre"])     
                self.entrada_precio.insert(0,resultado["precio"])     
                self.entrada_stock.insert(0,resultado["stock"])     

    def modificar_producto(self):
        producto = self.obtener_datos()
        self.buscar_producto()
        self.mis_productos.modificar(producto)
        
    def borrar_producto(self):
        id = self.entrada_id.get()
        self.buscar_producto()
        self.mis_productos.borrar(id)

    def listar_producto(self):
        listado = self.mis_productos.listar()
        lista = ""
        for un_productos in listado:
            lista = lista + str(un_productos) + "\n"
        self.mostrar_mensaje(lista)
        
    def limpiar_producto(self):
        self.entrada_id.delete(0,tk.END)
        self.entrada_nombre.delete(0,tk.END)
        self.entrada_precio.delete(0,tk.END)
        self.entrada_stock.delete(0,tk.END)
        self.mostrar_mensaje("")
    
mi_ventana_productos = Ventana_productos()
