from clases.iva import *

if __name__ == "__main__":
    print("Ejercicio 3:")
    producto = FactoryFactura()
    producto.set_naturaleza("alimentaria")
    print(producto.iva())
