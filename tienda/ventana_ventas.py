import tkinter as tk
from tkinter import messagebox, ttk
import json
from models.venta2 import Venta2

class Ventana_ventas:
    def __init__(self):
        self.mis_ventas = Venta2()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Ventas")
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
        self.mis_ventas = None
        
    def crear_entrada(self):
        tk.Label(self.frame_entrada, text="Id:", width=10).grid(row=0,column=0, padx=10, pady=5, sticky="w")
        self.entrada_id = tk.Entry(self.frame_entrada, width=30)
        self.entrada_id.grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.frame_entrada, text="Vendedor:", width=10).grid(row=1,column=0, pady=5, sticky="w")
        self.entrada_vendedor = tk.Entry(self.frame_entrada, width=30)
        self.entrada_vendedor.grid(row=1, column=1, pady=5)
        tk.Label(self.frame_entrada, text="Total:", width=10).grid(row=2,column=0, pady=5, sticky="w")
        self.entrada_total = tk.Entry(self.frame_entrada, width=30)
        self.entrada_total.grid(row=2, column=1, pady=5)
        tk.Label(self.frame_entrada, text="Cantidad:", width=10).grid(row=3,column=0, pady=5, sticky="w")
        self.entrada_cantidad = tk.Entry(self.frame_entrada, width=30)
        self.entrada_cantidad.grid(row=3, column=1, pady=5)
    
    def crear_botones(self):
        estilo = ttk.Style()
        estilo.configure('TButton', font=('Helvetica', 10), padding=5)
        ttk.Button(self.frame_botones, text="Agregar", command=self.agregar_venta).grid(row=0,column=0,padx=5)
        ttk.Button(self.frame_botones, text="Buscar", command=self.buscar_venta).grid(row=0,column=1,padx=5)
        ttk.Button(self.frame_botones, text="Modificar", command=self.modificar_venta).grid(row=0,column=2,padx=5)
        ttk.Button(self.frame_botones, text="Borrar", command=self.borrar_venta).grid(row=0,column=3,padx=5)
        ttk.Button(self.frame_botones, text="Listar", command=self.listar_venta).grid(row=0,column=4,padx=5)
        ttk.Button(self.frame_botones, text="Limpiar", command=self.limpiar_venta).grid(row=0,column=5,padx=5)

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
        vendedor = self.entrada_vendedor.get()
        try:
            total = float(self.entrada_total.get())
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número!")
            return None
        try:
            cantidad = float(self.entrada_cantidad.get())
        except ValueError:
            messagebox.showerror("Error", "El stock debe ser un número!")
            return None
        return {"id": id, "vendedor": vendedor, "total":total, "cantidad": cantidad}
        
    def agregar_venta(self):
        ventas = self.obtener_datos()
        if ventas:
            resultado = self.mis_ventas.buscar(ventas["id"])
            if resultado["id"]=="No encontrado":
                self.mis_ventas.agregar(ventas)
                self.mostrar_mensaje("venta agregado con éxito!")
                self.limpiar_venta()
            else:
                self.mostrar_mensaje("Id de venta ya existe!")

    def buscar_venta(self):
        id = self.entrada_id.get()
        if id!="":
            resultado = self.mis_ventas.buscar(id)
            if resultado["id"]=="No encontrado":
                self.mostrar_mensaje("Id de venta no existe!")
            else:
                self.limpiar_venta()
                self.entrada_id.insert(0,resultado["id"])                     
                self.entrada_vendedor.insert(0,resultado["vendedor"])     
                self.entrada_total.insert(0,resultado["total"])     
                self.entrada_cantidad.insert(0,resultado["cantidad_productos"])     

    def modificar_venta(self):
        venta = self.obtener_datos()
        self.buscar_venta()
        self.mis_ventas.modificar(venta)
        
    def borrar_venta(self):
        id = self.entrada_id.get()
        self.buscar_venta()
        self.mis_ventas.borrar(id)

    def listar_venta(self):
        listado = self.mis_ventas.listar()
        lista = ""
        for una_venta in listado:
            lista = lista + str(una_venta) + "\n"
        self.mostrar_mensaje(lista)
        
    def limpiar_venta(self):
        self.entrada_id.delete(0,tk.END)
        self.entrada_vendedor.delete(0,tk.END)
        self.entrada_total.delete(0,tk.END)
        self.entrada_cantidad.delete(0,tk.END)
        self.mostrar_mensaje("")
    
mi_ventana_ventas = Ventana_ventas()