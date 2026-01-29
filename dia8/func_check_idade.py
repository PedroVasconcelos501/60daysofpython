def pode_dirigir(idade):
    if idade >= 18:
        return True
    else:
        return False
     

try:
    input_user = int(input("Por favor, insira sua idade: "))
    print(pode_dirigir(input_user)) 
except ValueError:
    print("Por favor, insira um número válido para a idade.")