#lista de frutas

#frutas = ["banana", "maçã", "uva", "pera", "manga"]
# for fruta in frutas:
    #print(fruta)
    
    
#utilizando o input para criar a lista de frutas
frutas = []

while True:
    fruta = input("Digite o nome da fruta: ")
    if fruta == "sair":
        break
    frutas.append(fruta)
    
    print(frutas)
    