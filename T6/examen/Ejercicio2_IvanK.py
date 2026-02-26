lista_inicial = [3, 7, 2, 9, 4,]
lista_inicial += [5,] #Intente hacerlo con append pero me dio un error, por eso lo hice así
print (lista_inicial)
lista = lista_inicial
lista.sort()
print(lista)

assert lista[-2] == 7