from ingredientes.ingrediente import Ingrediente

class Queso(Ingrediente):
    def __init__(self, nombre):
        super().__init__("Queso", "🧀")