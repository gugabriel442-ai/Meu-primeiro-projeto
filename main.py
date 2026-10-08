carros = []


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
    modelo_excluir = input("Digite o modelo que deseja excluir: ")

    encontrado = False

    for carro in carros:
        if carro["modelo"] == modelo_excluir:
            carros.remove(carro)

            print("Carro excluído com sucesso!")

            encontrado = True
            break

    if encontrado == False:
        print("Carro não encontrado.")                  


while True:
    print("\n===== CADASTRO DE CARROS =====")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Pesquisar carro")
    print("4 - Excluir carro")
    print("5 - Sair")

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
    
    # Sair
    elif opcao == "5":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida.")