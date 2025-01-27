def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

    Retorna:
    float: O valor da gorjeta calculada
    """
    # Converte a porcentagem para decimal e multiplica pelo valor da conta
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    # Arredonda para duas casas decimais
    return round(gorjeta, 2)

# Exemplo de uso
total_conta = 100.00
porcentagem = 15
gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R${total_conta:.2f}, a gorjeta de {porcentagem}% é R${gorjeta:.2f}")
