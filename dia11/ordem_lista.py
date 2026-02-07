#lista ordenada a parrtir do metodo sorted()

#1. lista numerica

lista_num = [2, 9, 1, 5, 6]

#sorted() é uma função imbutida do python que ordena uma lista
#retorna uma nova lista ordenada, sem modificar a lista original
numeros_ordenados = sorted(lista_num)
numeros_ordenados2= sorted(lista_num, reverse=True)

print(numeros_ordenados)
print(numeros_ordenados2)