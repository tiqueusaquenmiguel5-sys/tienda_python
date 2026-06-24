"""
Se trata de escribir un programa con un CRUD para productos.
Cada producto debe tener los siguientes datos:
- codigo (string)
- nombre (string)
- precio (float)
- stock (int)
"""
import json

class Venta2:
    def __init__(self):
        try:
            with open("venta2.json","r", encoding="utf-8") as archivo_venta2:
                self.listado_v2 = json.load(archivo_venta2)
        except FileNotFoundError:
            self.listado_v2 = []
    
    def __del__(self, open=open):
        with open("venta2.json","w", encoding="utf-8") as archivo_venta2:
            json.dump(self.listado_v2, archivo_venta2, indent=4, ensure_ascii=False)
    
    def agregar(self, una_venta): # se recibe un json "un_producto"
            self.listado_v2.append(una_venta)
        
    def buscar(self, id):
        encontrado = {"id":"No encontrado"}
        for una_venta in self.listado_v2:
            if una_venta["id"]==id:
                encontrado = una_venta
                break
        return encontrado

    def modificar(self, nueva_venta):
        for i in range(len(self.listado_v2)):
            if self.listado_v2[i]["id"]==nueva_venta["id"]:
                self.listado_v2[i]["vendedor"]=nueva_venta["vendedor"]
                self.listado_v2[i]["total"]=nueva_venta["total"]
                self.listado_v2[i]["cantidad"]=nueva_venta["cantidad"]

    def borrar(self, id):
        for i in range(len(self.listado_v2)):
            if self.listado_v2[i]["id"]==id:
                self.listado_v2.pop(i)
                break

    def listar(self):
        return self.listado_v2