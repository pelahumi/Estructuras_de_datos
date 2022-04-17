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
        archivo.write(self.codigo2)
        

