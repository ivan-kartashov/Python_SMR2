#! Minijuego realizado por Pablo Peréz, Ivan Kartashov y Sebastian Gúzman
#El juego realizado es un pequeño juego de estrategía, donde hay varios objetos, que se cambian de valor cada turno
#El objetivo del juego es alcanzar la máxima puntuación posible, y pagando con puntuación se pueden ampliar los turnos que tenemos
#Se pueden vender tus objetos para obtener puntuación y así tener más puntuación que otros
import random

#Stats iniciales, el inventario inicial y la deadline inicial, además de los precios estandár
turnsleft = 10
inventory = {"oro": 0,"plata": 0,"cobre": 0,"arboles": 0,"sillas": 0,"mesas": 0, }
score = 100
precio_oro = 80
precio_plata = 60
precio_cobre = 20
precio_arboles = 10
precio_sillas = 2
precio_mesas = 5
turnnumber = 0
#-----------------------------------------------------------------------------------------------
eventos = ["Colapsan las minas! Precio de los minerales +25%", "Huracanes en los bosques! Precio de los arboles +15%", "Carpinteros de huelga! Precio de mesas y sillas +50%", "Atasco en la carretera, precio de todo +10%", "Nuevas minas abiertas! Precio de los minerales -20%", "Abundancia de bosques! Precio de los arboles -10%", "Graduación en grado medio de carpinteria! Precio de mesas y sillas -50%", "Guerra declarada a la nación vecina! Precio de todo -10%", ]
#-----------------------------------------------------------------------------------------------
#Ahora empezamos el juego con un while, que seguira mientras los turnos restantes sean mayores que 0
while turnsleft > 0: #El juego sigue mientras hay mas que 0 turnos restantes
    turnnumber += 1 #Aumentamos cada vez que reiteramos el while el turno
    event = random.randint(1,10)
    if event == 6 or event == 7: #Aqui elegimos los eventos aleatorios y sus consecuencias en los precios
        randomevent = random.choice(eventos)
        print(randomevent)
        if "minerales +25%" in randomevent:
            precio_oro = int(precio_oro * 1.25) #int al principio permite redondear el valor para que siempre sea un número entero
            precio_plata = int(precio_plata * 1.25)
            precio_cobre = int(precio_cobre * 1.25)
        elif "arboles +15%" in randomevent:
            precio_arboles = int(precio_arboles * 1.15)
        elif "mesas y sillas +50%" in randomevent:
            precio_sillas = int(precio_sillas * 1.50)
            precio_mesas = int(precio_mesas * 1.50)
        elif "de todo +10%" in randomevent:
            precio_oro = int(precio_oro * 1.10)
            precio_plata = int(precio_plata * 1.10)
            precio_cobre = int(precio_cobre * 1.10)
            precio_arboles = int(precio_arboles * 1.10)
            precio_sillas = int(precio_sillas * 1.10)
            precio_mesas = int(precio_mesas * 1.10)
        elif "minerales -20%" in randomevent:
            precio_oro = int(precio_oro * 0.8)
            precio_plata = int(precio_plata * 0.8)
            precio_cobre = int(precio_cobre * 0.8)
        elif "arboles -10%" in randomevent:
            precio_arboles = int(precio_arboles * 0.8)
        elif "mesas y sillas -50%" in randomevent:
            precio_mesas = int(precio_mesas * 0.5)
            precio_sillas = int(precio_sillas * 0.5)
        elif "de todo -10%" in randomevent:
            precio_oro = int(precio_oro * 0.9)
            precio_plata = int(precio_plata * 0.9)
            precio_cobre = int(precio_cobre * 0.9)
            precio_arboles = int(precio_arboles * 0.9)
            precio_sillas = int(precio_sillas * 0.9)
            precio_mesas = int(precio_mesas * 0.9) 
    print(f"Precios: \n Oro: {precio_oro} Plata: {precio_plata} Cobre: {precio_cobre} Arboles: {precio_arboles} Sillas: {precio_sillas} Mesas: {precio_mesas}")
    while True: # Este While es importante, nos permite estar en el menú y realizar varias acciones por turno
        print("\nTurno", turnnumber) #Mostramos al usuario el turno en el cual se encuentra
        print("Turnos restantes:", turnsleft) #Mostramos al usuario los turnos que le quedan
        print("Puntuación:", score) #Mostramos al usuario cuanta puntuación tiene
        eleccion = int(input("1)Comprar  2)Vender  3)Ver inventario  4)Pasar turno  5)Comprar turnos \n")) #Menu donde le decimos al usuario que y como hacer
        if eleccion == 1:
            print("¿Que deseas comprar? Tengo oro, plata, cobre, arboles, sillas y mesas a la venta")
            compra = input("Elige ('nada' para volver al menú): ").lower()
            if compra != "nada":
                try: #Ahora que sabemos que va a comprar le pedimos la cantidad
                    cantidad_compra = int(input("Cantidad deseada: "))
                    if compra == "oro":
                        precio_compra = precio_oro * cantidad_compra
                    elif compra == "plata":
                        precio_compra = precio_plata * cantidad_compra
                    elif compra == "cobre":
                        precio_compra = precio_cobre * cantidad_compra
                    elif compra == "arboles":
                        precio_compra = precio_arboles * cantidad_compra
                    elif compra == "sillas":
                        precio_compra = precio_sillas * cantidad_compra
                    elif compra == "mesas":
                        precio_compra = precio_mesas * cantidad_compra
                    if precio_compra <= score:
                        score -= precio_compra
                        inventory[compra] += cantidad_compra
                        print(f"Habeís adquirido {cantidad_compra} de {compra}. Os quedan {score} puntos")
                    else:
                        print("No hay suficiente dinero")
                except TypeError: #ValueError #Les decimos si han introducido un valor que no vale
                    print("Cantidad inválida, la compra no fue realizada.")
        elif eleccion == 2:
            print("¿Que deseaís vender?")
            print("Este es vuestro inventario:", inventory) #Le mostramos el inventario al usuario para que sepa que puede vender y que no
            objeto_venta = input("Introducir el nombre aquí: ").lower()
            if objeto_venta != "nada":
                try:
                    cantidad_venta = int(input(f"Cantidad a vender, teneís {inventory[objeto_venta]} {objeto_venta}"))
                    if cantidad_venta <= inventory[objeto_venta]: #La cantidad de objetos que se quieren comprar deberán ser menores o iguales que los que tiene actualmente el usuario
                        if objeto_venta == "oro":
                            precio_venta = precio_oro * cantidad_venta
                        elif objeto_venta == "plata":
                            precio_venta = precio_plata * cantidad_venta
                        elif objeto_venta == "cobre":
                            precio_venta = precio_cobre * cantidad_venta
                        elif objeto_venta == "arboles":
                            precio_venta = precio_arboles * cantidad_venta
                        elif objeto_venta == "sillas":
                            precio_venta = precio_sillas * cantidad_venta
                        elif objeto_venta == "mesas":
                            precio_venta = precio_mesas * cantidad_venta
                        inventory[objeto_venta] -= cantidad_venta
                        score += precio_venta
                        print(f"Vendiste {cantidad_venta} {objeto_venta} y ganaste {precio_venta} puntos. Ahora tienes {score} puntos")
                    else: #Si no tiene suficientes objetos para vender se lo decimos
                        print(f"No tienes suficiente/s {objeto_venta}")
                except TypeError: #ValueError
                    print("Cantidad inválida, la venta no se ha podido realizar")
        elif eleccion == 3: #Al elegir la opción 3, le mostramos el inventario al usuario
            print(inventory)
        elif eleccion == 4: #Al elegir la opción de pasar turno, el turno se pasa
            turnsleft -= 1
            break
        elif eleccion == 5: #Al elegir la opción 5 de comprar más turnos, le preguntamos si lo quiere de verdad
            print("Puedes comprar 5 turnos por 200 puntos, quieres?")
            mas_turnos = input("¿Si o no?").lower()
            if mas_turnos == "si": #Si tiene suficientes puntos
                if score >= 200:
                    score -= 200
                    turnsleft += 5
                    print(f"Has comprado 5 turnos, ahora tienes {turnsleft} turnos restantes")
                else: #Si no tiene suficientes puntos
                    print("No tienes suficientes puntos amigo")
        if turnsleft <= 0: #Si no le quedan más turnos
            break

print(f"Habeís perdido \n5Score final: {score}") #Al final les mostramos que han perdido y que tienen x de puntuación