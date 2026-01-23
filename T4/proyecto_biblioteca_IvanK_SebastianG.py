#Biblioteca musica
#

#Función que agregara una cancion a la lista de todas las canciones y tambien realizara el contador de las canciones totales
def agregar_cancion(titulo, artista, fecha):
    cancion_nueva = (titulo, artista, fecha)
    biblioteca_musical.append(cancion_nueva)


#Funciones de organizar las canciones por sus titulos o autores alfabeticamente
def ordenar_por_titulo(cancion):
    return cancion[0]

def ordenar_por_autor(cancion):
    return cancion[1]

def mostrar_canciones(orden="titulo"):
    if orden == "titulo":
        canciones_ordenadas = sorted(biblioteca_musical, key=ordenar_por_titulo)
    elif orden == "autor":
        canciones_ordenadas = sorted(biblioteca_musical, key=ordenar_por_autor)
    else:
        return "Que dices"
    for titulo, artista, fecha in canciones_ordenadas:
        print(f"{titulo} - {artista} - {fecha}")


#Función que realizara la busqueda de una canción a partir de una palabra, caracter y etc
def buscar_cancion(palabra):
    resultados = []
    for titulo, artista, fecha in biblioteca_musical:
        if palabra.lower() in titulo.lower():
            resultados.append((titulo, artista, fecha))
    print(resultados) 
    
#Funcion que contara cuantas canciones tiene cada artista 
def estadisticas():
    artistas = {}
    for titulo, artista, fecha in biblioteca_musical:
        if artista in artistas:
            artistas[artista] += 1
        else:
            artistas[artista] = 1
    print(artistas)

#Función para borrar cancion por titulo
def eliminar_cancion(titulo_buscar):
    for cancion in biblioteca_musical:
        titulo, artista, fecha = cancion
        if titulo.lower() == titulo_buscar.lower():
            biblioteca_musical.remove(cancion)
            return 

#Funcion para modificar los datos de una canción existente
def actualizar_cancion(titulo_buscar, nuevo_titulo=None, nuevo_artista=None, nueva_fecha=None): #El valor predifenido de las variables titulo, artista y fecha van a ser none para que puedas introducir solo el valor para una de estas y etc
    for i in range(len(biblioteca_musical)):
        titulo, artista, fecha = biblioteca_musical[i]
        if titulo.lower() == titulo_buscar.lower():
            titulo_actualizado = nuevo_titulo if nuevo_titulo else titulo
            artista_actualizado = nuevo_artista if nuevo_artista else artista
            fecha_actualizada = nueva_fecha if nueva_fecha else fecha

            biblioteca_musical[i] = (titulo_actualizado, artista_actualizado, fecha_actualizada)
            print("Cancion cambiada")
            return

    print("No hay canción con titulo así")
#Funcion de ordenar por fecha para luego usarlo en sorted
def ordenar_por_fecha(cancion):
    return cancion[2]
#Función para mostrar canción por su fecha, viejas vs nuevas
def mostrar_por_fecha(tipo=None):
    if tipo == "viejas":
        canciones_ordenadas = sorted(biblioteca_musical, key=ordenar_por_fecha)
    elif tipo == "nuevas":
        canciones_ordenadas = sorted(biblioteca_musical, key=ordenar_por_fecha, reverse=True)
    else:
        print("nuevas o viejas solo")
        return

    for titulo, artista, fecha in canciones_ordenadas:
        print(f"{titulo} - {artista} - {fecha}")




biblioteca_musical = []
agregar_cancion('Bohemian Rhapsody','Queen',1975)
agregar_cancion('Imagine','John Lennon',1971)
agregar_cancion('Killer Queen','Queen',1974)
print(biblioteca_musical)
mostrar_canciones()
buscar_cancion("Kill")
estadisticas()
eliminar_cancion("Imagine")
print(biblioteca_musical)
mostrar_por_fecha("nuevas")