from collections import Counter

def contar_ocorrencias(lista):
    """
    Contar ocorrencias de cada elemento em uma lista
    Args:
        lista (list): A lista de elementos a ser analisada
    Return:
        Counter: Um objeto Counter contendo a contagem de cada elemento    
    """
    
    contagem = Counter(lista)
    
    for elemento, quantidade in contagem.items():
        print(f"{elemento}: {quantidade}")
    
    return "Contagem concluída!"

if __name__ == "__main__":
    lista_exemplo = ['maçã', 'banana', 'laranja', 'maçã', 'banana', 'maçã']
    resultado = contar_ocorrencias(lista_exemplo)
   