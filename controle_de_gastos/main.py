import json

def salvar_movimentacoes():
    with open("movimentacoes.json", "w") as arquivo:
        json.dump(movimentacoes, arquivo, indent=4)

def carregar_movimentacoes():
    try:
        with open("movimentacoes.json", "r") as arquivo:
            dados = json.load(arquivo)

            if isinstance(dados, list):
                movimentacoes.extend(dados)

    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("Erro: o arquivo JSON está vazio ou possui conteúdo inválido.")


movimentacoes = []


def mostrar_menu():
    print("\n=== CONTROLE FINANCEIRO ===")
    print("1 - Adicionar movimentação")
    print("2 - Listar movimentações")
    print("3 - Ver resumo")
    print("4 - Excluir movimentação")
    print("5 - Editar movimentação")
    print("0 - Sair")

def obter_opcao():
    opcao = input("Escolha uma opção: ")
    return opcao


def adicionar_movimentacao():
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

    while True:
        categoria = input("Digite a categoria da movimentação: ").strip().lower()

        if categoria:
            break

        print("A categoria não pode ficar vazia.")

    tipo = input("Despesa ou Receita? ").strip().lower()

    while tipo not in ["despesa", "receita"]:
        print("Tipo inválido. Digite 'Despesa' ou 'Receita'.")
        tipo = input("Despesa ou Receita? ").strip().lower()

    movimentacoes.append([nome, valor, categoria, tipo])
    salvar_movimentacoes()


def listar_movimentacoes():
    if not movimentacoes:
        print("Nenhuma movimentação cadastrada.")
        return

    for indice, movimentacao in enumerate(movimentacoes, start=1):
        nome, valor, categoria, tipo = movimentacao
        print(
            f"{indice} - Nome: {nome}, Valor: R$ {valor}, "
            f"Categoria: {categoria}, Tipo: {tipo}"
        )


def ver_resumo():
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


def excluir_movimentacao():
    if not movimentacoes:
        print("Nenhuma movimentação cadastrada.")
        return

    listar_movimentacoes()

    while True:
        try:
            indice_excluir = int(input("Digite o índice da movimentação que deseja excluir: "))

            if 1 <= indice_excluir <= len(movimentacoes):
                del movimentacoes[indice_excluir - 1]
                salvar_movimentacoes()
                print("Movimentação excluída com sucesso.")
                break
            print("Índice inválido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Digite um número válido.")


def editar_movimentacao():
    if not movimentacoes:
        print("Nenhuma movimentação cadastrada.")
        return

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
            while True:
                novo_nome = input("Digite o novo nome: ").strip()

                if novo_nome:
                    movimentacao[0] = novo_nome
                    break

                print("O nome não pode ficar vazio.")
        elif campo == "2":
            while True:
                try:
                    novo_valor = float(input("Digite o novo valor: "))

                    if novo_valor <= 0:
                        print("O valor deve ser maior que zero.")
                        continue

                    movimentacao[1] = novo_valor
                    break
                except ValueError:
                    print("Valor inválido. Digite um número válido.")
        elif campo == "3":
            while True:
                nova_categoria = input("Digite a nova categoria: ").strip().lower()

                if nova_categoria:
                    movimentacao[2] = nova_categoria
                    break

                print("A categoria não pode ficar vazia.")
        elif campo == "4":
            novo_tipo = input("Despesa ou Receita? ").strip().lower()
            while novo_tipo not in ["despesa", "receita"]:
                print("Tipo inválido. Digite 'Despesa' ou 'Receita'.")
                novo_tipo = input("Despesa ou Receita? ").strip().lower()
            movimentacao[3] = novo_tipo
        else:
            print("Opção inválida. Tente novamente.")
            continue

        print("Movimentação editada com sucesso.")
        salvar_movimentacoes()
        break


carregar_movimentacoes()

while True:
    mostrar_menu()
    opcao = obter_opcao()

    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        adicionar_movimentacao()
    elif opcao == "2":
        listar_movimentacoes()
    elif opcao == "3":
        ver_resumo()
    elif opcao == "4":
        excluir_movimentacao()
    elif opcao == "5":
        editar_movimentacao()
    else:
        print("Opção inválida. Tente novamente.")