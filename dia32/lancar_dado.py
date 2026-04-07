import random

def lancar_dado():
    """
    Simular o lançamento de um dado de 6 faces.
    
    Returns:
        int: O resultado do lançamento do dado (entre 1 e 6).
    """
    return random.randint(1, 6)

if __name__ == "__main__":
    print("Lançando o dado...")
    resultado = lancar_dado()
    print(f"O resultado do lançamento do dado é: {resultado}.") 