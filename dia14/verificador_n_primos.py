numero= int(input("Digite um número para verificar se ele é primo: "))

#assumimos com true se o numero é primo
e_primo = True

if numero <= 1:
    e_primo = False
    
for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0: #se for por i não é primo
        e_primo = False
        break #saimos do loop pois já sabemos que não é primo
    
if e_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")