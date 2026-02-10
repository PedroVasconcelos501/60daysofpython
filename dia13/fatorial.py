#oq é fatorial? 
#fatorial é um calculo mateático que multiplicamos os valores apartir do numero passado
#3! = 3 * 2 * 1 = 6

def fatorial(n):
    """
    Calcula o fatorial de um número usando recursão
    
    
    :param n: O número inteiro não negativo
    :return: O fatorial de n
    """
    if n < 0:
        raise ValueError("O numero deve ser positivo")
    
    #essa condicional retorna 1 para o fatorial de 0 e 1
    if n == 0 or n == 1:
        return 1
    
    #recursividade
    #return n * fatorial(n - 1)

print(fatorial(5))  # Saída: 120

try:
    print(f"fatorial(-1): {fatorial(-1)}")  # Deve levantar um ValueError
except ValueError as e:
    print(e)  # Saída: O numero deve ser positivo