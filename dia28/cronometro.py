import time

def cronometro(tempo):
    """
    cronometro que conta até um tempo determinado
    
    """
    print("Cronometro iniciado...")
    
    for segundo in range(tempo + 1):
       print (f"Tempo: {segundo} segundos", end="\r")
       time.sleep(1)
       
    print("\nCronometro finalizado!")
       
       
if __name__ == "__main__":
    Tempo = 10
    cronometro(Tempo)
