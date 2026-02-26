lista = [1, 2, 3]
tupla = (1, 2, 3)

lista += [4,]
print(lista)

tupla = list(tupla)
tupla += [4,]
tupla = tuple(tupla)
print(tupla)

diccionario = {"pepe":25, "xulei":67, "ale":"mujer"}

print(diccionario.values[1])

# class Super():
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self.edad = edad

#     def cambiar_nombre(self, nombre_nuevo):
#         self._nombre = nombre_nuevo

#     def mostrar_nombre(self):
#         return self._nombre

# class Hijo(Super):
#     def __init__(self, nombre, edad, calle):
#         super().__init__(nombre, edad)
#         self.__calle = calle

# class Puta(Super):
#     def __init__(self, nombre, edad):
#         super().__init__(nombre, edad)

# jose = Super("jose", 54)
# jose.cambiar_nombre("pepe")
# assert jose.mostrar_nombre() == "pepe"
