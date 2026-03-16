import random

def gerar_numeros_aleatoros():
    """
    gera numeros aleatórios imprimindo 10 numeros de 1 a 100
    """
    print("Bem vindo ao gerador de números aleatórios!")
    
    numeros_aleatorios = []
    
    #gerar numeros aleatorios
    for _ in range(10):
        numero = random.randint(1, 100)
        numeros_aleatorios.append(numero)
    
    print("\nNúmeros aleatórios gerados:")
    for i, numero in enumerate(numeros_aleatorios, start=1):
        print(f"Numero {i}: {numero}")
        
if __name__ == "__main__":
    gerar_numeros_aleatoros()