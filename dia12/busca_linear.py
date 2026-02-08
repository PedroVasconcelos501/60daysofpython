def busca_linear(lista, numero_procurado):
    
    """
    Procurar um  numero em uma lista usando busca linear

    :param lista: lista de números
    :param numero_procurado: número a ser procurado
    """

    for i, numero in enumerate (lista): #função nativa do python enumerate
#enumerate passa por cada item da lista enquanto contabiliza a partir do numero 0
        if numero == numero_procurado:
            return i #retorna o indice do numero encontrado
    return -1 #retorna -1 caso o numero não seja encontrado

lista = [10,2,3,4,6,13,9]
numero_procurado = 2

buscando_o_numero = busca_linear(lista, numero_procurado)
print(buscando_o_numero)

if buscando_o_numero != -1:
    print(f"Número encontrado no índice {buscando_o_numero}")
    
else:
    print("Número não encontrado")
    
    