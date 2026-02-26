primer_nombre = str(input("Introduzca vuestro nombre: "))

apellido = str(input("Introduzca vuestro apellido: "))

nombre = primer_nombre + " " + apellido

longitud = len(nombre)

assert nombre.upper() == 'ANA LÓPEZ' 
assert apellido == 'López'
assert longitud == 9