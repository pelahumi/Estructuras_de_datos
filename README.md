# Estructuras_de_datos
El link del repositorio es: [Github](https://github.com/pelahumi/Estructuras_de_datos)

---

## Índice:
1.[main](#1).  
2.[Ejercicio 1](#2).   
3.[Ejercicio 2](#3).   
4.[Ejercicio 3](#4).  

---

### Main<a name="1"></a>
```python3
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
```

### Ejercicio 1<a name="2"></a>
```python3
class Bloque(): 
    # Un bloque es un conjunto de instrucciones ejecutadas 
    # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruction(self, instruccion): 
        self.instrucciones.append(instruccion) 
 
class Si(): 
    # Representa una instrucción 'if'. 'condicion' es una cadena 
    # de caracteres que contiene la evaluación de la condición, 
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
    # si no se verifica. 
 
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion 
        self.entonces = entonces 
        self.si_no = si_no 
    
    def comprobar_condicion(self):
        if self.condicion == True:
            self.entonces = Mostrar("Ok")
            self.entonces.mostrar()

        else:
            self.si_no = Mostrar("Ko")
            self.si_no.mostrar()
 
class MientrasQue(): 
    # Representa una instrucción 'while'. 
    # 'condicion' es una cadena que contiene el valor evaluado 
    # para decidir si el bucle continúa o no, 
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque 

    def bucle(self):
        while self.condicion == True:
            self.bloque = Bloque()
            self.bloque.agregarInstruction[self.bloque]
        else:
            pass
 
class Mostrar(): 
    # Una instrucción para mostrar un mensaje 
    # en salida estándar. 
    def __init__(self, mensaje): 
        self.mensaje = mensaje 
    
    def mostrar(self):
        print(self.mensaje)
```

### Ejercicio 2<a name="3"></a>
```python3
class FilosofiaMVC():
    def __init__(self,codigo1, codigo2):
        self.codigo1 = codigo1
        self.codigo2 = codigo2
    
        #Comprobamos que las lineas de codigo sean str, y aprovechamos para pasarlas a mayusculas
        if isinstance(codigo1, str):
            self.codigo1 = codigo1.upper()
        else:
            raise TypeError("La linea de codigo 1 no es una str")

        if isinstance(codigo2, str):
            self.codigo2 = codigo2.upper()
        else:
            raise TypeError("La linea de codigo 2 no es una str")

    def escribir_archivo(self):
        archivo = open("filosofia.txt", "w")
        archivo.write(self.codigo1)
        archivo.write("\n")
        archivo.write(self.codigo2)
```

### Ejercicio 3<a name="4"></a>
```python3
class Producto():
    def __init__(self, naturaleza):
        self.precio_neto = 100
        self.naturaleza = naturaleza

class FactoryFactura(Producto):
    def __init__(self):
        self.precio_neto = 100
        self.naturaleza = ""

    def set_naturaleza(self, naturaleza_to_be_set):
        if isinstance(naturaleza_to_be_set, str):
            self.naturaleza = naturaleza_to_be_set
        else:
            raise ValueError("La naturaleza del producto tiene que ser un str")

    def iva(self):
        if self.naturaleza == "alimentación":
            precio_bruto = self.precio_neto + (self.precio_neto * 5.5 / 100)
            return precio_bruto
        elif self.naturaleza == "servicio":
            precio_bruto = self.precio_neto + (self.precio_neto * 20 / 100)
            return precio_bruto
        else: 
            print("La naturaleza del producto no es correcta")




