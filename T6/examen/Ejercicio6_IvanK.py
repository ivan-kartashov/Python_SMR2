class Coche:
    def __init__(self, marca, modelo, km=0):
        self.marca = marca
        self.modelo = modelo
        self.km = km
    def recorrer(self, kms):
        self.km += kms
    def mostrar(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Kilómetros: {self.km}")

class CocheElectrico(Coche):
    def __init__(self, marca, modelo, km=0, bateria=100):
        super().__init__(marca, modelo, km)
        self.bateria = bateria
    def cargar(self):
        self.bateria = 100


coche = CocheElectrico("Tesla", "Model 3")
coche.recorrer(120)
coche.bateria -= 30
coche.cargar()

assert coche.km == 120
assert coche.marca == "Tesla"
assert coche.modelo == "Model 3"
assert coche.bateria == 100