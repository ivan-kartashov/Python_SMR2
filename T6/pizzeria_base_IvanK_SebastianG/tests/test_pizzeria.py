import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ingredientes.queso import Queso
from ingredientes.carne import Carne
from ingredientes.vegetal import Vegetal
from pizza import Pizza
from pedido import Pedido

class TestIngrediente(unittest.TestCase):

    def test_encapsulacion(self):
        queso = Queso("Mozzarella")
        # __nombre y __simbolo no deben ser accesibles directamente
        with self.assertRaises(AttributeError):
            _ = queso.__nombre
        with self.assertRaises(AttributeError):
            _ = queso.__simbolo

        # Solo mediante getters
        self.assertEqual(queso.get_nombre(), "Mozzarella")
        self.assertEqual(queso.get_simbolo(), "🧀")

    def test_herencia(self):
        carne = Carne("Pollo")
        vegetal = Vegetal("Pimiento")

        self.assertEqual(carne.get_nombre(), "Pollo")
        self.assertEqual(carne.get_simbolo(), "@")
        self.assertEqual(vegetal.get_nombre(), "Pimiento")
        self.assertEqual(vegetal.get_simbolo(), "+")


class TestPizza(unittest.TestCase):

    def test_add_ingrediente(self):
        pizza = Pizza("Pizza personalizada")
        queso = Queso("Mozzarella")
        pizza.add_ingrediente(queso)

        # No se puede acceder a __ingredientes
        with self.assertRaises(AttributeError):
            _ = pizza.__ingredientes

        # Comprobar que se agregó correctamente mediante imprimir_ascii
        ascii_repr = pizza.imprimir_ascii()
        self.assertIn("🧀", ascii_repr)
        self.assertIn("Pizza personalizada", pizza.get_nombre() or "Test Pizza")  # nombre correcto


    def test_imprimir_ascii_multiple_ingredientes(self):
        pizza = Pizza("Mix")
        pizza.add_ingrediente(Queso("Mozzarella"))
        pizza.add_ingrediente(Carne("Pollo"))
        pizza.add_ingrediente(Vegetal("Pimiento"))

        ascii_repr = pizza.imprimir_ascii()
        self.assertIn("🧀", ascii_repr)
        self.assertIn("@", ascii_repr)
        self.assertIn("+", ascii_repr)


class TestPedido(unittest.TestCase):

    def test_add_pizza(self):
        pedido = Pedido()
        pizza1 = Pizza("Pizza1")
        pizza2 = Pizza("Pizza2")
        pedido.add_pizza(pizza1)
        pedido.add_pizza(pizza2)

        # Para comprobarlo, redirigimos la salida de mostrar_pedido
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        pedido.mostrar_pedido()

        sys.stdout = sys.__stdout__  # restaurar

        output = captured_output.getvalue()
        lines = [line.strip() for line in output.splitlines() if line.strip()]

        # Buscamos solo los nombres de las pizzas
        self.assertIn("Pizza1", lines)
        self.assertIn("Pizza2", lines)



if __name__ == "__main__":
    unittest.main()
