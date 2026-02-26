class Pedido:
    def __init__(self):
        self.__pizzas = []

    def add_pizza(self, pizza):
        self.__pizzas.append(pizza)

    def mostrar_pedido(self):
        print("Cantidad de pizzas:", len(self.__pizzas))
        if not self.__pizzas:
            print("No hay pizzas en el pedido")
            return
        
        for pizza in self.__pizzas:
            print(pizza.get_nombre())
            pizza.imprimir_ascii()
