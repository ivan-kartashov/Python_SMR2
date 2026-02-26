class Camiseta:
    def __init__(self, talla, color, precio):
        self.talla = talla
        self.color = color
        self.precio = precio
    
    def descripcion(self):
        return f"Camiseta {self.color}, talla {self.talla}, {self.precio}€"
    
    def teñir(self, color_tinte):
        self.color = color_tinte

    def rebajar(self, porcentaje):
        self.precio = self.precio * (100 - porcentaje)

    


camiseta = Camiseta("S", "rosa", 10)
camiseta.teñir("blanco")
assert camiseta.color == "blanco"

camiseta.rebajar(20)
assert camiseta.precio == 8