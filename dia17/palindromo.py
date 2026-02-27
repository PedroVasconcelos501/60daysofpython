def e_palindromo(texto):
    """    
    Verificar se um numero texto ou palavra é um palíndromo
    param: texto: palavra, texto, numero
    :return: uma mensagem dizendo se é ou não um palíndromo
    """
    texto = str(texto).replace(" ", "").lower()
    
    if texto == texto[::-1]:
        return f"{texto} é um palíndromo."
    return f"{texto} não é um palíndromo."

print(e_palindromo("arara"))