import textwrap
from time import sleep  # Para finalizar o programa

print(20 * "\033[34m=-")
print("{:^35}".format("CLASSIC BANK"))
print(20 * "=-")
print("{:^40}".format("\033[1mWelcome to Classic Bank!"))  # Cordialidade para ficar bonito


def menu():
    menu = """\n                       
    \033[0m================ MENU ================
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [NC]\tNova conta
    [LC]\tListar contas
    [NU]\tNovo usuário
    [Q]\tSair
    \033[1m=> Selecione uma opção: """  # Menu de opções disponíveis
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n\033[33m=== Depósito realizado com sucesso! ===")
    else:
        print("\n\033[31mOperação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n\033[31mOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\n\033[31mOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\n\033[31mOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n\033[33m=== Saque realizado com sucesso! ===")

    else:
        print("\n\033[31mOperação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n\033[33m================ EXTRATO ================")
    print("\033[31mNão foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\033[33m==========================================")


def criar_usuario(usuarios):
    cpf = input("\033[0mInforme o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[31mJá existe um usuário cadastrado com esse CPF.")
        return

    nome = input("\033[0mInforme o nome completo: ")
    data_nascimento = input("\033[0mInforme a data de nascimento (dd-mm-aaaa): ")
    endereco = input("\033[0mInforme o endereço (logadouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome,"data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco,})

    print("\033[33m=== Usuário cadastrado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\033[0mInforme o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\033[33m=== Conta cadastrada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n\033[31mUsuário não encontrado, fluxo de cadastro de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            \033[0mAgência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuário']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = " "
    numero_saques = 0
    usuarios = []
    contas = []

    while True:                              # .upper() para a resposta dada ficar em maiúsculo
        opcao = str(menu()).strip().upper()  # .strip() para remover espaços inúteis.

        if opcao == "D":
            valor = float(input("\033[0mInforme o valor do depósito: R$ "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("\033[0mInforme o valor do saque: R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "Q":
            print("\033[31mFinalizando operação bancária...")
            sleep(1.85)
            break

        else:
            print("\033[31mOperação inválida, por favor selecione novamente a opção desejada.")


main()
