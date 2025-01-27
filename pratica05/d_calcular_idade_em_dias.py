import datetime

def calcular_idade_em_dias(ano_nascimento):

    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Simplificação, não considera anos bissextos
    return idade_dias

# Input do usuário
ano_nasc = int(input("Digite o ano de nascimento: "))

# Calcula e exibe o resultado
idade_em_dias = calcular_idade_em_dias(ano_nasc)
print(f"Sua idade aproximada em dias é: {idade_em_dias} dias")
