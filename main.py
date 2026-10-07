carros = []

while True:
    print("===== CADASTRO DE CARROS =====")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Pesquisar carro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        ano = input("Digite o ano do carro: ")
        preco = input("Digite o preço do carro: ")

        carro = {
            "marca": marca,
            "modelo": modelo,
            "ano": ano,
            "preco": preco
        }

        carros.append(carro)
        print("Carro cadastrado com sucesso!")

    elif opcao == "2":
        for carro in carros:
            print(carro)

    elif opcao == "3":
        modelo_pesquisa = input("Digite o modelo que deseja pesquisar: ")

        for carro in carros:
            if carro["modelo"] == modelo_pesquisa:
                print("Carro encontrado!")
                print("Marca:", carro["marca"])
                print("Modelo:", carro["modelo"])
                print("Ano:", carro["ano"])
                print("Preço:", carro["preco"])

    elif opcao == "4":
        print("Programa encerrado!")
        break