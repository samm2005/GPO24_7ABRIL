class Cuadrado:
    def __init__ (self, lado):
        self.lado = lado
    
    def area (self):
        return self.lado * self.lado
    
    
ladodo = int(input("ingrese un lado: ") )
mi_cuadro= Cuadrado(ladodo)
print("el area del cuadrado es: ", mi_cuadro.area())
    