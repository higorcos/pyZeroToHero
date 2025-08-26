menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[u] Novo Usuário
[c] Nova Conta

=> """

saldo = 100
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contas = []
AGENCIA_PADRAO = "0001"

usuarios = []

def saque(*,saldo,valor,extrato,limite,numero_saques,limite_saque):


    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saque


    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return (saldo,extrato,)

def deposito(saldo,valor,extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return (saldo,extrato,)

def Fextrato(saldo,*,extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

    # CPF - apenas números
    while True:
        cpf = input("Digite o CPF (somente números): ")
        if not cpf.isdigit():
            print("CPF deve conter apenas números.")
        elif any(u['cpf'] == cpf for u in usuarios):
            print("Este CPF já está cadastrado.")
        else:
            break

    # Endereço com formatação
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite a sigla do estado (ex: SP): ")

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado.upper()}"

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!")
    print(usuario)


def encontrar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta():
    cpf = input("Informe o CPF do usuário: ")
    usuario = encontrar_usuario(cpf)

    if usuario:
        numero_conta = len(contas) + 1  # sequencial
        conta = {
            "agencia": AGENCIA_PADRAO,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
        contas.append(conta)
        print("\nConta criada com sucesso!")
        print(conta)
    else:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        result = deposito(saldo, valor, extrato)

        novo_saldo = result[0]
        if novo_saldo != saldo:
            saldo = novo_saldo
            novo_extrato = result[1]
            extrato = novo_extrato

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        result = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saque= LIMITE_SAQUES)

        novo_saldo = result[0]
        if novo_saldo != saldo:
            saldo = novo_saldo
            novo_extrato = result[1]
            extrato = novo_extrato

    elif opcao == "e":
        Fextrato(saldo,extrato=extrato)

    elif opcao == "q":
        break
    elif opcao == "u":
       cadastrar_usuario()
    elif opcao == "c":
        criar_conta()

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")