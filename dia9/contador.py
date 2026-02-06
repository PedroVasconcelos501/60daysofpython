#contador que conta até um valor personalizado fornecido pelo usuário
def contador_personalizado():
    try:
        limite = int(input("Digite o valor máximo para o contador: "))
        
        #função range para contar de 0 até o valor fornecido
        for i in range(limite + 1):
            print(i)
            if i == limite:
                print("Contagem finalizada.")
                break
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        
contador_personalizado()