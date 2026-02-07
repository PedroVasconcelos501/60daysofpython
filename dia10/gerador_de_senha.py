import random 
import string

#random fornece uma função para gerar números aleatórios
#string fornece uma coleção de caracteres, como letras, dígitos e pontuação

def gerador_de_senha(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    
    while len(senha) < comprimento:
        senha += random.choice(caracteres)
        
    print(f"Senha gerada: {senha}")
    
gerador_de_senha(30)
