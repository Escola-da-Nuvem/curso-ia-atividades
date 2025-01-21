# Este programa calcula o volume de uma caixa retangular

# Solicita as dimensões da caixa ao usuário
comprimento = float(input("Digite o comprimento da caixa em cm: "))
largura = float(input("Digite a largura da caixa em cm: "))
altura = float(input("Digite a altura da caixa em cm: "))

# Calcula o volume da caixa
volume = comprimento * largura * altura

# Exibe o resultado
print(f"O volume da caixa é {volume} cm³")
