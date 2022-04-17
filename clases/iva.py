class Producto():
    def __init__(self, naturaleza):
        self.precio_neto = 100
        self.naturaleza = naturaleza

class FactoryFactura(Producto):
    def __init__(self):
        super.__init__()

    def crear(self):
        self.naturaleza = str(input("Introduce la naturaleza del producto: "))

    def iva(self):
        if self.naturaleza == "alimentación":
            precio_bruto = self.precio_neto + (self.precio_neto * 5.5 / 100)
            return precio_bruto
        elif self.naturaleza == "servicio":
            


