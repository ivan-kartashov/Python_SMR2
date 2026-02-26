semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo")

primeros = []

semana = list(semana)

primer = str(semana[0])

ultimo = str(semana[-1])

primeros.append(primer)

primeros.append(ultimo)

primeros = tuple(primeros)

dias_con_a = []

for dia in semana:
    if "a" in dia:
        dias_con_a.append(dia)

assert primeros == ("Lunes", "Domingo")
assert dias_con_a == ["Martes", "Sábado"]
