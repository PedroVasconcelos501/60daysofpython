def conversor_moeda(valor, taxa_cambio, tipo_conversao):
    """
    Essa função converte dolar em reais e visse e versa
    Args:
        valor (float): O valor a ser convertido
        taxa_cambio: A taxa de cambio atual
        tipo_conversao: O tipo de conversão, "dolar_para_real" ou "real_para_dolar"
        
    Return:
        float: O valor convertido arrendondado para 2 casas decimais
        
    Raises:
        ValueError: Se o tipo de conversão for inválido
    """
    
    if tipo_conversao == "dolar_real":
        return round(valor * taxa_cambio, 2)
    elif tipo_conversao == "real_dolar":
        return round(valor / taxa_cambio, 2)
    else:
        return ValueError("Tipo de conversão inválido:")

print(conversor_moeda(12, 6.10, "real_dolar"))