class Producto():
    def __init__(self, naturaleza):
        self.precio_neto = 100
        self.naturaleza = naturaleza

class FactoryFactura(Producto):
    def __init__(self):
        super.__init__()

    def set_naturaleza(self, naturaleza_to_be_set):
        if isinstance(naturaleza_to_be_set, str):
            self.naturaleza = naturaleza_to_be_set
        else:
            raise TypeError("La naturaleza del producto tiene que ser un str")

    def iva(self):
        if self.naturaleza == "alimentación":
            precio_bruto = self.precio_neto + (self.precio_neto * 5.5 / 100)
            return precio_bruto
        elif self.naturaleza == "servicio":
            precio_bruto = self.precio_neto + (self.precio_neto * 20 / 100)
            return precio_bruto
        else: 
            raise TypeError("La naturaleza del producto no es correcta")

producto = FactoryFactura.set_naturaleza("")




