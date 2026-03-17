def escrever_arquivo(nome_arquivo, conteudo):
    """
    Escreve o conteúdo em um arquivo txt.

    Args:
        nome_arquivo (str): O nome do arquivo a ser criado.
        conteudo (str): O texto a ser escrito no arquivo.
    """


    with open(nome_arquivo, 'w') as arquivo:#w = write
        arquivo.write(conteudo)
        
    print(f"o conteudo foi salvo no arquivo {nome_arquivo}")
    
def ler_arquivo(nome_arquivo):
    """
    Lê o conteúdo de um arquivo txt.

    Args:
        nome_arquivo (str): O nome do arquivo a ser lido.
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:#r = read
            conteudo = arquivo.read()
        print(f"Conteúdo do arquivo {nome_arquivo}:\n{conteudo}")
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
        
def main(nome_arquivo, conteudo):
    """
    função principal que demonstra  escrita e leitura do arquivo

    Args:
        nome_arquivo (str): O nome do arquivo a ser criado.
        conteudo (str): O texto a ser escrito no arquivo.
    """
    
    print("Bem vindo ao programa de escrita e leitura de arquivos!")

    #escreve o arquivo
    escrever_arquivo(nome_arquivo, conteudo)
    
    #ler o arquivo
    print("fazendo a leitura do arquivo...")
    ler_arquivo(nome_arquivo)
    
if __name__ == "__main__":
    nome_arquivo = "exemplo.txt"
    conteudo = "Olá, este é um exemplo de escrita e leitura de arquivos em Python."
    main(nome_arquivo, conteudo)