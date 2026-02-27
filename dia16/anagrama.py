def anagrama(palavra1, palavra2):
    """
    Verificar se duas palavras são um anagrama ou não
    :param palavra1: Primeira palavra
    :param palavra2: Segunda palavra
    return: True se as palavras forem um anagrama, False caso contrário
    """
    
    # Remover espaços e converter para minúsculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    if sorted(palavra1) == sorted(palavra2):
        return f"{palavra1} e {palavra2} são um anagrama"
    else:
        return f"{palavra1} e {palavra2} não são um anagrama"
     
print(anagrama("roma", "amor"))