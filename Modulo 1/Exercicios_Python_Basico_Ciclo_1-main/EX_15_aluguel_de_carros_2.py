# Atualize o código de aluguel de carros feito anteriormente. 
# Crie um programa em Python que simule o cálculo do valor total a ser pago pelo aluguel de um carro. O programa deve:
# 1- Perguntar ao usuário qual foi o modelo do carro alugado.
# 2- Perguntar por quantos dias o carro foi alugado.
# 3- Perguntar quantos quilômetros foram percorridos com o carro.
# 4- Usar uma tabela de preços (pré-definida pelo próprio aluno) para determinar o valor diário de aluguel de acordo com o modelo do carro.
# 5- Calcular o custo total com base:
# 6- No número de dias alugados × valor por dia
# 7- No total de quilômetros rodados × R$0,15 por km
# 8- Exibir o valor total a ser pago, com duas casas decimais.

# Os alunos são livres para definir quais modelos de carro o programa aceitará e o valor por dia de cada um.

# Se o modelo inserido pelo usuário não estiver na lista, o programa deve aplicar um valor padrão por dia.

# OUTPUT ESPERADO: 

# ----------------------------------------------------- EXEMPLO 1

# Qual foi o modelo do carro alugado? uno
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100
# Você andou 100.0km por 10 dias, então o preço a pagar é R$415.00.

# ----------------------------------------------------- EXEMPLO 2

# Qual foi o modelo do carro alugado? bmw
# Por quantos dias o carro foi alugado: 10 
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$10015.00.

# ----------------------------------------------------- EXEMPLO 3(PREÇO PADRÃO)

# Qual foi o modelo do carro alugado? fox
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$615.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print("|", "_" * 35, "|")
print("| DRIVE STYLE - ALUGUEL AUTOMOTIVO    |")
print("| Carros disponíveis:                 |")
print("""| Chevrole Opala 1971 - 1
| Diaria = 350
| 
| Hyundai HB20s - 2
| Diaria = 90
| 
| VW Santana Quantum - 3
| Diaria = 150
| 
| VW Voyage G1 - 4
| Diaria = 180
| 
| VW Saveiro G3 - 5
| Diaria = 100
| """)

pergunta = input("| Qual desses você alugou? ")

if pergunta == "1":
    dia = int(input("| Por quantos dias o carro foi alugado: "))
    km = float(input("| Quantos km o carro rodou: "))

    preco = (dia * 350) + (km * 0.15)

    print(f"| Você andou {km}km por {dia} dias com o Opala 1971, então o preço a pagar é R${preco:.2f}")

elif pergunta == "2":
    dia = int(input("| Por quantos dias o carro foi alugado: "))
    km = float(input("| Quantos km o carro rodou: "))

    preco = (dia * 90) + (km * 0.15)

    print(f"| Você andou {km}km por {dia} dias com o HB20s, então o preço a pagar é R${preco:.2f}")

elif pergunta == "3":
    dia = int(input("| Por quantos dias o carro foi alugado: "))
    km = float(input("| Quantos km o carro rodou: "))

    preco = (dia * 150) + (km * 0.15)

    print(f"| Você andou {km}km por {dia} dias com o VW Santana Quantum, então o preço a pagar é R${preco:.2f}")

elif pergunta == "4":
    dia = int(input("| Por quantos dias o carro foi alugado: "))
    km = float(input("| Quantos km o carro rodou: "))

    preco = (dia * 180) + (km * 0.15)

    print(f"| Você andou {km}km por {dia} dias com o VW Voyage G1, então o preço a pagar é R${preco:.2f}")

elif pergunta == "5":
    dia = int(input("| Por quantos dias o carro foi alugado: "))
    km = float(input("| Quantos km o carro rodou: "))

    preco = (dia * 100) + (km * 0.15)

    print(f"| Você andou {km}km por {dia} dias com o VW Saveiro G3, então o preço a pagar é R${preco:.2f}")

else:
    print("| Opção inválida")