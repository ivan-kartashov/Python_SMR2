class Ingrediente:
    """
    Clase base que representa un ingrediente de una pizza.
    """

    def __init__(self, nombre, simbolo):
        self.__nombre = nombre
        self.__simbolo = simbolo

    def get_nombre(self):
        return self.__nombre

    def get_simbolo(self):
        return self.__simbolo
