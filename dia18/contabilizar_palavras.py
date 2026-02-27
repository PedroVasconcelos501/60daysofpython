def contar_palavras(texto):
    """
    Conta o número de palavras em uma string
    :param texto: string de entrada
    :return: número de palavras

    """
    #split() vai separar o texto em palavras usando o espaço do texto
    palavras = texto.split()
    
    return len(palavras)

print(contar_palavras("Olá, como vai você?"))  # Deve retornar 4
    