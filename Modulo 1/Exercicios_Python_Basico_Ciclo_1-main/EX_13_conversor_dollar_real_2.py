# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

pergunta = int(input("""Escolha uma opção
1 - Dollar para Real
2 - Real para Dollar
Digite a opção: """))

if pergunta == 1:
    cotacao = float(input("Digite a cotação do dollar: "))
    dolar = float(input("Digite o valor em dollar a ser convetido para real:  US$"))

    real = dolar * cotacao
 
    print(f"O valor em reais é: R${real:.2f}")

elif pergunta == 2:

    cotacao = float(input("Digite a cotação do dollar: "))
    real = float(input("Digite o valor em real a ser convetido para dollar: R$"))
    dolar = real / cotacao

    print(f"R$ {dolar:.2f}")

else:
    print("Opção inválida")