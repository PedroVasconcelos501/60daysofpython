import random

def jogar_adivinhacao():
    """
    um jogo onde o usuario tenta adivinhar um numero aleatório
    """
    
    print("Bem-vindo ao jogo de adivinhação!")
    
    #gerar um numero aleatorio entre 1 e 10
    
    numero_secreto = random.randint(1, 10)
    
    tentativa= 0
    
    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 10: "))
            tentativa += 1
                
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
                
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
                
            else:
                print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativa} tentativas.")
                break
            
        except ValueError:
            print("Tentativa inválida. Por favor, digite um número inteiro entre 1 e 10.")
            
if __name__ == "__main__":
    jogar_adivinhacao()
    