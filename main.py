carros = carregar_carros()


import json
import os

ARQUIVO = "carros.json"


def carregar_carros():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return []


def salvar_carros():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(carros, arquivo, indent=4, ensure_ascii=False)


carros = carregar_carros()


def formatar_preco(preco):
    preco = f"{preco:,.2f}"
    preco = preco.replace(",", "X").replace(".", ",").replace("X", ".")
    return preco

def cadastrar_carro():
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")

    ano = input("Digite o ano do carro: ")

    while not ano.isdigit():
        print("Digite um ano válido.")
        ano = input("Digite o ano do carro: ")

    ano = int(ano)

    preco = input("Digite o preço do carro: ")

    while not preco.isdigit():
        print("Digite um preço válido.")
        preco = input("Digite o preço do carro: ")

    preco = float(preco)

    carro = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "preco": preco
    }

    carros.append(carro)
    salvar_carros()

    print("Carro cadastrado com sucesso!")

def listar_carros():
    if len(carros) == 0:
            print("Nenhum carro cadastrado.")
    else:
        for carro in carros:
            print("-------------------------")
            print("Marca:", carro["marca"])
            print("Modelo:", carro["modelo"])
            print("Ano:", carro["ano"])
            print("Preço: R$", formatar_preco(carro["preco"]))

def pesquisar_carro():
    modelo_pesquisa = input("Digite o modelo que deseja pesquisar: ").lower()

    encontrado = False

    for carro in carros:
        if carro["modelo"].lower() == modelo_pesquisa:
            print("Carro encontrado!")
            print("Marca:", carro["marca"])
            print("Modelo:", carro["modelo"])
            print("Ano:", carro["ano"])
            print("Preço: R$", formatar_preco(carro["preco"]))

            encontrado = True

    if encontrado == False:
        print("Carro não encontrado.")  

def excluir_carro():
    modelo_excluir = input("Digite o modelo que deseja excluir: ").lower()

    encontrado = False

    for carro in carros:
        if carro["modelo"].lower() == modelo_excluir:
            carros.remove(carro)
            salvar_carros()

            print("Carro excluído com sucesso!")

            encontrado = True
            break

    if encontrado == False:
        print("Carro não encontrado.")    


def relatorio_estoque():
    if len(carros) == 0:
        print("Nenhum carro cadastrado para gerar o relatório.")
    else:
        carro_mais_caro = max(carros, key=lambda carro: carro["preco"])
        carro_mais_barato = min(carros, key=lambda carro: carro["preco"])

        print("\n===== RELATÓRIO DO ESTOQUE =====")
        print("Total de carros:", len(carros))

        print("Carro mais caro:", carro_mais_caro["modelo"])
        print("Preço: R$", formatar_preco(carro_mais_caro["preco"]))

        print("Carro mais barato:", carro_mais_barato["modelo"])
        print("Preço: R$", formatar_preco(carro_mais_barato["preco"]))

              
while True:
    print("\n===== CADASTRO DE CARROS =====")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Pesquisar carro")
    print("4 - Excluir carro")
    print("5 - Relatório do estoque")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    # Cadastrar carro
    if opcao == "1":
        cadastrar_carro()

    # Listar carros
    elif opcao == "2":
        listar_carros()

    # Pesquisar carro
    elif opcao == "3":
        pesquisar_carro()

    # Excluir carro
    elif opcao == "4":
        excluir_carro()

    # Relatório do estoque
    elif opcao == "5":
        relatorio_estoque()
    
    # Sair
    elif opcao == "6":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida.")