import os


def adicionar_contato(lista_nomes, nome):
    lista_nomes.append(nome)


def remover_contato(lista_nomes, nome):
    lista_nomes.remove(nome)


def listar_nomes(lista_nomes):
    for nome in lista_nomes:
        print(nome)


def limpar_tela():
    os.system("cls")




nomes = []
while True:
    limpar_tela()
    opcao = input("[1] - Adicionar contato\n" \
    "[2] - Remover contato\n" \
    "[3] - Listar contatos\n" \
    "[0] - Sair\n" \
    "Sua opção: ")


    if opcao == "1":
        nome = input("Digite um nome: ")
        adicionar_contato(nomes, nome)
   
    elif opcao == "2":
        remove = input("Qual contato deseja remover? ")
        remover_contato(nomes, nome)
   
    elif opcao == "3":
        listar_nomes(nomes)
        input("Aperte Enter para retornar ao menu.")
   
    elif opcao == "0":
        break

