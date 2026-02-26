class Planeta:
    
    def __init__(self, tipo, composicion, localizacion):
        self.tipo = tipo
        self.composicion = composicion
        self.localizacion = localizacion

    def habitabilidad(self):
        oxigeno = self.composicion.get("Oxigeno")
        nitrogeno = self.composicion.get("Nitrogeno")
        if oxigeno is None or nitrogeno is None:
            return "Planeta Inhabitable"
        
        rango_oxigeno = (21, 22)
        rango_nitrogeno = (77, 79)

        if rango_oxigeno[0] <= oxigeno <= rango_oxigeno[1] and rango_nitrogeno[0] <= nitrogeno <= rango_nitrogeno[1]:
            if self.tipo == "Rocoso":
                return "Planeta potencialmente habitable"
            else:
                return "Planeta inhabitable"
        else:
            return "Planeta inhabitable"
        



tierra = Planeta(
    "Rocoso",
    {"Oxigeno": 21, "Nitrogeno": 78},
    "Zona habitable"
)

print(tierra.habitabilidad())

jupiter = Planeta(
    "Gaseoso",
    {"Hidrogeno": 87, "Helio": 13},
    "Zona habitable"
)

print(jupiter.habitabilidad())