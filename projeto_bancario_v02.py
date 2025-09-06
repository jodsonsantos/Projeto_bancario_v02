saldo = 0.0
extrato = []
saques_diarios = 0
LIMITES_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0
usuarios = []
contas = []
NUMERO_CONTA_SEQUENCIAL = 1

def menu () :
    print("\n=== Sistema Bancario V2 ===")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Criar Usuario")
    print("5 - Listar Conta Corrente")
    print("6 - Listar Contas")
    print("7 - Sair")
    return input("Escolha uma opção: (1-7) ")

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append((f"deposito: R${valor:.2f}"))
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("erro: O valor de depósito inválido valor deve ser positivo.")
    return saldo,extrato

def sacar(*,saldo, valor, extrato,limite, numero_saques, limite_saque):

    if numero_saques >= limite:
        print(f"erro: O número máximo de {limite}  saques diários foi atingido.")
    elif valor > limite_saque:
        print(f"erro: O valor de saque inválido valor maximo por saque é de R$ {limite_saque:.2f}!")
    elif valor <= saldo:
        saldo -= valor
        numero_saques += 1
        extrato.append((f"sacar: R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("erro: O valor de saque insuficiente.")
    return saldo, extrato, numero_saques

def extrato(saldo, /, extrato):

    print("\n=== Extrato ===")
    if extrato:
        for transacao in extrato:
            print(transacao)
    else:
        print("Nenhuma transação realizada.")
print(f"\nSaldo atual: R${saldo:.2f}")

def criar_usuario(usuarios, /, nome, data_nascimento, cpf, endereco):
    cpf = ''.join(filter(str.isdigit, cpf))
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("erro: CPF já cadastrado.")
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
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break
    if not usuario:
        print("Erro: Usuário com este CPF não encontrado.")
        return contas

    conta = {
        "numero": "0001",
        "numero_conta" : f"{NUMERO_CONTA_SEQUENCIAL:04d}",
        "saldo": 0.0,
        "extrato": []
    }
    contas.append(conta)
    NUMERO_CONTA_SEQUENCIAL += 1
    print(f"Conta criada com sucesso! Número da conta: {conta['numero']}")
    return contas

def listar_contas(contas, /):
    print("\n=== Contas Correntes ===")
    if contas:
        for conta in contas:
            print(f"Agência: {conta['numero']}, Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}, CPF: {conta['usuario']['cpf']}, Saldo: R${conta['saldo']:.2f}")
    else:
        print("Nenhuma conta corrente encontrada.")

while True:

    opcao = menu()
    if opcao == "1":
        valor = float(input("Informe o valor do depósito R$: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "2":
        valor = float(input("Informe o valor do saque R$: "))
        saldo, extrato, saques_diarios = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITES_SAQUES, numero_saques=saques_diarios, limite_saque=LIMITE_VALOR_SAQUE)
    elif opcao == "3":
        extrato(saldo, extrato=extrato)
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
        
        