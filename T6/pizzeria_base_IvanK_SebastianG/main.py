from pizzeria import Pizzeria
from pedido import Pedido
from pizza import Pizza
from ingredientes.queso import Queso
from ingredientes.carne import Carne
from ingredientes.vegetal import Vegetal

def main():
    pizzeria = Pizzeria()
    pedido = Pedido()

    while True:
        pizzeria.mostrar_nombre()
        pizzeria.mostrar_menu()
        opcion = input("Opción: ")
        ingcounter = 0
        if opcion == "1":
            pizza = Pizza(input("Escribir el nombre de la pizza personalizada: "))
            # TODO: añadir ingredientes
            # muestra al usuario opciones para que elija qué ingredientes quiere añadir a su pizza, 
            # hasta que elija la opción de terminar pizza
            # Por ejemplo, así añadiría Queso y después terminaría la pizza.
            
            while True:
                print(
                    f"""
                Ingredientes:
                1. Queso
                2. Carne
                3. Vegetal
                0. Terminar pizza
                Elige ingrediente:{ingcounter}
            """
                )
                ing = input()
                if ing == "1":
                    pizza.add_ingrediente(Queso("Queso"))
                    ingcounter += 1
                elif ing == "2":
                    pizza.add_ingrediente(Carne("Carne"))
                    ingcounter += 1
                elif ing == "3":
                    pizza.add_ingrediente(Vegetal("Vegetal"))
                    ingcounter += 1
                elif ing == "0":
                    pedido.add_pizza(pizza)
                    print("Pizza guardada correctamente")
                    break

        elif opcion == "2":
            pedido.mostrar_pedido()
        elif opcion == "3":
            break

if __name__ == "__main__":
    main()
