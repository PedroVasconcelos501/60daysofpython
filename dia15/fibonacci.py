fibonacci = [0, 1] # a sequencia de Fibonacci começa com 0 e 1

for i in range (8):
    proximo_numero = fibonacci[-1] + fibonacci[-2] # o próximo número é a soma dos dois últimos números
    fibonacci.append(proximo_numero) # adiciona o próximo número à lista
    
print(fibonacci)