import time

def cronometro_de_10seg():
    """
    Realiza um cronômetro de 10 segundos
    
    """
    
    print("Cronômetro de 10 segundos iniciado!")
    
    tempo = 10
    
    while tempo > 0:
        print(f"Tempo restante: {tempo} segundos", end="\r",flush=True)
        time.sleep(1)  # Pausa o programa por 1 segundo
        tempo -= 1

    print("\nTempo esgotado!")

if __name__ == "__main__":
    cronometro_de_10seg()