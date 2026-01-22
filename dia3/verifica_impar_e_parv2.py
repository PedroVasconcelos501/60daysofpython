entrada= input("Digite o numero: ")

try: #tente rodar
    numero= int(entrada)
    if numero % 2 == 0:
        print(f"O numero {numero} é par")
    else:
        print(f"O numero {numero} é impar")

except ValueError: #se der erro de valor
    print("Por favor, digite um numero valido")
    