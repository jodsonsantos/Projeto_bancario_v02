saldo = 0.0  # Não usado
historico_extrato = []  # Não usado
saques_diarios = 0  # Não usado
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0
usuarios = []
contas = []
NUMERO_CONTA_SEQUENCIAL = 1

def menu():
    print("\n=== Sistema Bancário V2 ===")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Criar Usuário")
    print("5 - Criar Conta Corrente")
    print("6 - Listar Contas")
    print("7 - Sair")
    return input("Escolha uma opção (1-7): ")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print(f"\n== Depósito: R${valor:.2f} realizado com sucesso! ==")
    else:
        print("\n@@ O valor de depósito deve ser positivo! @@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    if valor <= 0:
        print("Erro: O valor de saque deve ser positivo!")
    elif numero_saques >= limite:
        print(f"Erro: Limite de {limite} saques diários atingido.")
    elif valor > limite_saque:
        print(f"Erro: O valor máximo por saque é R${limite_saque:.2f}!")
    elif valor > saldo:
        print("Erro: Saldo insuficiente!")
    else:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque: R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    return saldo, extrato, numero_saques

def historico_extrato(saldo, /, *, extrato):
    print("\n========== Extrato ==========")
    if extrato:
        for transacao in extrato:
            print(transacao)
    else:
        print("Nenhuma transação realizada.")
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("================================")

def criar_usuario(usuarios, /, *, nome, data_nascimento, cpf, endereco):
    cpf = ''.join(filter(str.isdigit, cpf))
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro: CPF já cadastrado.")
            return usuarios
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso.")
    return usuarios

def criar_conta(contas, usuarios, /, *, cpf):
    global NUMERO_CONTA_SEQUENCIAL
    cpf = ''.join(filter(str.isdigit, cpf))
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if not usuario:
        print("Erro: Usuário com este CPF não encontrado.")
        return contas
    conta = {
        "agencia": "0001",
        "numero_conta": f"{NUMERO_CONTA_SEQUENCIAL:04d}",
        "usuario": usuario,
        "saldo": 0.0,
        "extrato": [],
        "saques_diarios": 0
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {conta['agencia']}, Conta: {conta['numero_conta']}")
    NUMERO_CONTA_SEQUENCIAL += 1
    return contas

def listar_contas(contas, /):
    print("\n=== Contas Correntes ===")
    if contas:
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}, CPF: {conta['usuario']['cpf']}, Saldo: R${conta['saldo']:.2f}")
    else:
        print("Nenhuma conta corrente encontrada.")

while True:
    try:
        opcao = menu()
        if opcao == "1":
            if contas:
                print("Contas disponíveis:")
                listar_contas(contas)
                numero_conta = input("Digite o número da conta para depósito: ")
                conta = next((c for c in contas if c["numero_conta"] == numero_conta), None)
                if conta:
                    valor = float(input("Informe o valor do depósito R$: "))
                    conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])
                else:
                    print("Erro: Conta não encontrada.")
            else:
                print("Erro: Nenhuma conta cadastrada.")
        elif opcao == "2":
            if contas:
                print("Contas disponíveis:")
                listar_contas(contas)
                numero_conta = input("Digite o número da conta para saque: ")
                conta = next((c for c in contas if c["numero_conta"] == numero_conta), None)
                if conta:
                    valor = float(input("Informe o valor do saque R$: "))
                    conta["saldo"], conta["extrato"], conta["saques_diarios"] = sacar(
                        saldo=conta["saldo"],
                        valor=valor,
                        extrato=conta["extrato"],
                        limite=LIMITE_SAQUES,
                        numero_saques=conta["saques_diarios"],
                        limite_saque=LIMITE_VALOR_SAQUE
                    )
                else:
                    print("Erro: Conta não encontrada.")
            else:
                print("Erro: Nenhuma conta cadastrada.")
        elif opcao == "3":
            if contas:
                print("Contas disponíveis:")
                listar_contas(contas)
                numero_conta = input("Digite o número da conta para extrato: ")
                conta = next((c for c in contas if c["numero_conta"] == numero_conta), None)
                if conta:
                    historico_extrato(conta["saldo"], extrato=conta["extrato"])
                else:
                    print("Erro: Conta não encontrada.")
            else:
                print("Erro: Nenhuma conta cadastrada.")
        elif opcao == "4":
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            cpf = input("Digite o CPF (apenas números ou com formatação): ")
            endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/estado): ")
            usuarios = criar_usuario(usuarios, nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        elif opcao == "5":
            cpf = input("Digite o CPF do usuário para criar a conta: ")
            contas = criar_conta(contas, usuarios, cpf=cpf)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "7":
            print("Obrigado por usar o sistema")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira um número válido.")
        continue