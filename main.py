from clases.visitante import * 
from clases.filosofia import *
from clases.iva import *

if __name__ == "__main__":

    print("Ejercicio 1:")
    ok = Mostrar("Ok")
    ko = Mostrar("Ko")
    condicion = Si(2 + 2 == 4, ok, ko)
    bloque = Bloque()
    bloque.agregarInstruction(condicion)
    mientras = MientrasQue(True, bloque)

    print("Ejercicio 2:")
    code1 = "Hola don Pepito"
    code2 = "Hola don José"
    escritura = FilosofiaMVC(code1, code2)
    escritura.escribir_archivo()

    print("Ejercicio 3:")
    producto = FactoryFactura()
    producto.set_naturaleza("alimentación")
    print("El precio del producto alimentario es:",producto.iva(),"€")
    producto.set_naturaleza("servicio")
    print("El precio del producto de servicio es:",producto.iva(),"€")