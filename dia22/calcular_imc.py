def calcular_imc():
     """
     Função que calcula o IMC
     """

print("Bem vindo a calculadora de IMC")


try:
        peso= float(input("Digite seu peso em kg: "))
        altura= float(input("Digite sua altura em metros: "))
        
        if peso < 0 or altura <0:
            print("Peso e altura devem ser maiores que zero.")  
           
                    
        imc=round(peso / (altura ** 2), 2)
            
        if imc < 18.5:
            print("Você está abaixo do peso.")
        elif 18.5 <= imc <= 24:
            print("Você está com peso normal.")   
        else:
            print("Você está acima do peso.")
            
except ValueError:
        print("Entrada inválida. Por favor, insira um número válido para peso e altura.")
 
#significa que estamos rodando o código internamente
#apenas roda se eu rodar o script calcular_imc   
if __name__ == "__main__":
    calcular_imc()