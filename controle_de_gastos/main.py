movimentacoes = []

while True:
    print("\n=== CONTROLE FINANCEIRO ===")
    print("1 - Adicionar movimentação")
    print("2 - Listar movimentações")
    print("3 - Ver resumo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        break

    elif opcao == "1":
        nome = input("Digite o nome da movimentação: ")

        while True:
            try:
                valor = float(input("Digite o valor da movimentação: "))
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

    else:
        print("Opção inválida. Tente novamente.")

# banana
