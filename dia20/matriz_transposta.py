def transpor_matriz(matriz):
    """
    Gerar uma matriz transporta de 3x3
    Substitui colunar horizontal por vertical
    
    arg: matriz: lista de listas (matriz 3x3)    
    return: matriz transposta
    raise: ValueError: se a matriz não for 3x3
    
    """
    
    #verificar se a matriz é 3x3
    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
        raise ValueError("A matriz deve ser 3x3")
    
    #gerar matriz transposta
    transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]
    
    return transposta
    
    
    #explicação da matriz transposta utilizando iteradores e listas
matriz = [
 [1, 2, 3], 
 [4, 5, 6], 
 [7, 8, 9]
 
 ]
    
transposta = [] 


for i in range(3):
     #iniciando nova linha      
    nova_linha = []
        
    for j in range(3):
        #adicionando elemento correspondente a matriz original na nova linha
        nova_linha.append(matriz[j][i])

          
    #print(nova_linha)
    transposta.append(nova_linha)
  
for linha in transpor_matriz(matriz):
    print(linha)