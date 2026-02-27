def calcular_media_nota(notas):
    """
    Calculando média de tas apartir de uma lista de notas
    Arg: 
    lista de notas
    
    :return:
    float: média das notas
    """
    
    media = sum(notas) / len(notas)

    # Round arredonda a média para 2 casas decimais
    return round (media, 2)

print(calcular_media_nota([10, 7.0, 9.0]))  # Deve retornar