class Pizza:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__ingredientes = []

    def get_nombre(self):
        return self.__nombre

    def add_ingrediente(self, ingrediente):
        self.__ingredientes.append(ingrediente)

    def imprimir_ascii(self):
        """TODO: devolver dibujo ASCII de la pizza"""
        
        
        
        pizza_ascii = f"""
              -----
             /     \\
            |       |
             \     /
              -----
        """

        print(pizza_ascii)
        
