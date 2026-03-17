def celsius_para_fahrenheit(celsius):
    """
    converte a temperatura de celsius para fahrenheit

    Args:
        celsius (float): temperatura em celsius
        
    Returns:
        float: temperatura em fahrenheit
    """
    
    return round ((celsius * 9/5) + 32, 2)

def fahrenheit_para_celsius(fahrenheit):
    """
    converte a temperatura de fahrenheit para celsius

    Args:
        fahrenheit (float): temperatura em fahrenheit
        
    Returns:
        float: temperatura em celsius
    """
    
    return round ((fahrenheit - 32) * 5/9, 2)

def main(temperatura, tipo_conversão):  
    """
    converte a temperatura de celsius para fahrenheit ou de fahrenheit para celsius

    Args:
        temperatura (float): temperatura a ser convertida
        tipo de conversão (str): tipo de conversão a ser realizada
        
    Returns:
        float: temperatura convertida
    """
    
    if tipo_conversão == "celsius":
        print(celsius_para_fahrenheit(temperatura))
    elif tipo_conversão == "fahrenheit":
        print(fahrenheit_para_celsius(temperatura))
    else:
        raise ValueError("Escala inválida. Use 'c' para celsius ou 'f' para fahrenheit.")
    
if __name__ == "__main__":
    main(20, "celsius")
    main(20, "fahrenheit")