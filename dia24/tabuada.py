def tabuada():
    """
    essa função recebe um numero e devolve a sua tabuada
    """
    try:
        #solicita o numero para o usuario
        
        numero = int(input("Digite um numero para ver a sua tabuada: "))\
        
        print(f"\nTabuada do {numero}:")
        #gera tabuada de 1 a 10
        
        for i in range (1,11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
            
    except ValueError:
        print("Por favor, digite um numero valido.")
        
if __name__ == "__main__":
    tabuada()
