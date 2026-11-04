movimentacoes = []


def mostrar_menu():
    print("\n=== CONTROLE FINANCEIRO ===")
    print("1 - Adicionar movimentação")
    print("2 - Listar movimentações")
    print("3 - Ver resumo")
    print("4 - Excluir movimentação")
    print("5 - Editar movimentação")
    print("0 - Sair")


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        while True:
            nome = input("Nome da movimentação: ").strip()

            if nome:
                break

            print("O nome não pode ficar vazio.")

        while True:
            try:
                valor = float(input("Digite o valor da movimentação: "))

                if valor <= 0:
                    print("O valor deve ser maior que zero.")
                    continue

                break
            except ValueError:
                print("Valor inválido. Digite um número válido.")

        categoria = input("Digite a categoria da movimentação: ").lower()
        tipo = input("Despesa ou Receita? ").lower()

        while tipo not in ["despesa", "receita"]:
            print("Tipo inválido. Digite 'Despesa' ou 'Receita'.")
            tipo = input("Despesa ou Receita? ").lower()

        movimentacoes.append([nome, valor, categoria, tipo])

    elif opcao == "2":
        if not movimentacoes:
            print("Nenhuma movimentação cadastrada.")
        else:
            for indice, movimentacao in enumerate(movimentacoes, start=1):
                nome, valor, categoria, tipo = movimentacao
                print(
                    f"{indice} - Nome: {nome}, Valor: R$ {valor}, "
                    f"Categoria: {categoria}, Tipo: {tipo}"
                )

    elif opcao == "3":
        total_despesas = 0
        total_receitas = 0
        gastos_por_categoria = {}

        for _, valor, categoria, tipo in movimentacoes:
            if tipo == "despesa":
                total_despesas += valor
                gastos_por_categoria[categoria] = gastos_por_categoria.get(categoria, 0) + valor
            elif tipo == "receita":
                total_receitas += valor

        saldo = total_receitas - total_despesas

        print(f"Total de despesas: R$ {total_despesas}")
        print(f"Total de receitas: R$ {total_receitas}")
        print(f"Saldo: R$ {saldo}")

        print("\nGastos por categoria:")

        if not gastos_por_categoria:
            print("Nenhuma despesa cadastrada.")
        else:
            for categoria, valor in gastos_por_categoria.items():
                valor_porcentual = (valor / total_despesas) * 100 if total_despesas > 0 else 0
                print(
                    f"Categoria: {categoria}, Total gasto: R$ {valor}, "
                    f"Porcentagem de despesas: {valor_porcentual:.2f}%"
                )

    elif opcao == "4":
        if not movimentacoes:
            print("Nenhuma movimentação cadastrada.")
        else:
            for indice, movimentacao in enumerate(movimentacoes, start=1):
                nome, valor, categoria, tipo = movimentacao
                print(
                    f"{indice} - Nome: {nome}, Valor: R$ {valor}, "
                    f"Categoria: {categoria}, Tipo: {tipo}"
                )

            while True:
                try:
                    indice_excluir = int(input("Digite o índice da movimentação que deseja excluir: "))

                    if 1 <= indice_excluir <= len(movimentacoes):
                        del movimentacoes[indice_excluir - 1]
                        print("Movimentação excluída com sucesso.")
                        break
                    else:
                        print("Índice inválido. Tente novamente.")
                except ValueError:
                    print("Valor inválido. Digite um número válido.")

    
    elif opcao == "5":
        if not movimentacoes:
            print("Nenhuma movimentação cadastrada.")
        else:
            for indice, movimentacao in enumerate(movimentacoes, start=1):
                nome, valor, categoria, tipo = movimentacao

                print(
                    f"{indice} - Nome: {nome}, Valor: R$ {valor:.2f}, "
                    f"Categoria: {categoria}, Tipo: {tipo}"
                )

            while True:
                try:
                    indice_editar = int(
                        input("Digite o número da movimentação que deseja editar: ")
                    )

                    if 1 <= indice_editar <= len(movimentacoes):
                        break

                    print("Índice inválido. Tente novamente.")

                except ValueError:
                    print("Digite um número válido.")

            movimentacao = movimentacoes[indice_editar - 1]

            while True:
                print("\nO que deseja editar?")
                print("1 - Nome")
                print("2 - Valor")
                print("3 - Categoria")
                print("4 - Tipo")

                campo = input("Escolha o campo: ")

                if campo == "1":
                    movimentacao[0] = input("Digite o novo nome: ")

                elif campo == "2":
                    while True:
                        try:
                            novo_valor = float(
                                input("Digite o novo valor: ")
                            )

                            if novo_valor <= 0:
                                print("O valor deve ser maior que zero.")
                                continue

                            movimentacao[1] = novo_valor
                            break

                        except ValueError:
                            print("Digite um número válido.")

                elif campo == "3":
                    movimentacao[2] = input(
                        "Digite a nova categoria: "
                    ).lower()

                elif campo == "4":
                    novo_tipo = input(
                        "Despesa ou Receita? "
                    ).lower()

                    while novo_tipo not in ["despesa", "receita"]:
                        print("Tipo inválido. Digite 'Despesa' ou 'Receita'.")
                        novo_tipo = input(
                            "Despesa ou Receita? "
                        ).lower()

                    movimentacao[3] = novo_tipo

                else:
                    print("Opção inválida. Tente novamente.")
                    continue

                print("Movimentação editada com sucesso.")
                break

    else:
        print("Opção inválida. Tente novamente.")