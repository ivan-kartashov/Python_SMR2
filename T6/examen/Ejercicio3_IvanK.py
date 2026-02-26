notas = {"Matemáticas": 7, "Lengua": 6, "Inglés": 8, "Programación": 9,}

notas["Física"] = 5
print(notas)
nota_total = 0
num_asignaturas = 0
for asignatura, nota in notas.items():
    nota_total += nota
    num_asignaturas += 1

media = nota_total / num_asignaturas

assert 'Física' in notas
assert media == 7.0