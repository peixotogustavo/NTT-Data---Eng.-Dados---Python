
#Inicio do Programa

menu = """
=============================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuario
[5] Criar Conta Corrente
[6] Listar Usuarios
[7] Listar Contas Correntes
[0] Sair
=============================
=> """

LIMITE_SAQUES = 3
AGENCIA = "0001"

dados_usuarios = dict()
dados_conta_corrente = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_conta = 0


def criar_usuario(dados_usuarios):
    #FALTA FAZER A LOGICA DE CONFIRMAR SE JA EXISTE CPF CADASTRADO.
    print("===== Opcao Criando Usuario =====")

    cpf = input("Digite o CPF: ")
    for usuario in dados_usuarios.values():
        if usuario['cpf'] == cpf:
            print("Usuario ja cadastrado!!")
            return dados_usuarios

    nome = input("Digite o Nome do Usuario: ")
    data_nascimento = input("Digite a data de nascimento. Ex: 15/09/1995: ")
    endereco = input("Digite o endereco: Ex: logradouro, numero - bairro - cidade/sigla estado: ")

    usuario_id = f'usuario{len(dados_usuarios) + 1}'

    dados_usuarios[usuario_id] = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    return dados_usuarios

def criar_conta_corrente(dados_conta_corrente,dados_usuarios,AGENCIA,numero_conta):
    usuario_encontrado = False
    
    print("===== Opcao Criando Conta Corrente =====")

    cpf = input("Digite o CPF: ")
    for usuario_id, usuario in dados_usuarios.items():
        if usuario['cpf'] == cpf:
            usuario_encontrado = True

            print("Usuario encontrado! Conta Criada!")

            dados_conta_corrente.append(
                {"agencia": AGENCIA, 
                "numero_conta": numero_conta, 
                "usuario": usuario["nome"]
                })

            return dados_conta_corrente

    if not usuario_encontrado:
        print("Usuário não encontrado!")

    return dados_conta_corrente

def exibir_extrato(saldo,extrao):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def deposito(saldo,extrato):

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo,extrato

def saque(saldo,numero_saques,extrato,limite,LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

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

    return saldo,numero_saques,extrato


while True:

    print(menu)
    opcao = int(input("Digite a opcao escolhida: "))

    if opcao == 1:
       saldo,extrato = deposito(saldo,extrato)
       print(f"Saldo atual = {saldo}")
       
    elif opcao == 2:
        saldo,numero_saques,extrato = saque(saldo=saldo,numero_saques=numero_saques,extrato=extrato,limite=limite,LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == 3:
        exibir_extrato(saldo,extrato = extrato)

    elif opcao == 0:
        print("Voce esta saindo do programa...")
        break
    
    elif opcao == 4:
       dados_usuarios = criar_usuario(dados_usuarios=dados_usuarios)


    elif opcao == 5:
        numero_conta = len(dados_conta_corrente) + 1
        dados_conta_corrente = criar_conta_corrente(dados_conta_corrente=dados_conta_corrente,AGENCIA=AGENCIA,numero_conta=numero_conta,dados_usuarios=dados_usuarios)


    elif opcao == 6:

        print("=== Listando Usuarios ===\n")  

        for usuario_id, usuario_info in dados_usuarios.items():

            print(f"ID: {usuario_id}")
            print(f"Nome: {usuario_info['nome']}")
            print(f"CPF: {usuario_info['cpf']}")
            print(f"Data de Nascimento: {usuario_info['data_nascimento']}")
            print(f"Endereço: {usuario_info['endereco']}")
            print("-" * 30) 
    elif opcao == 7:
        print("=== Listando Contas Correntes ===\n")

        for conta in dados_conta_corrente:
            print(f"Agencia: {conta['agencia']}")
            print(f"Numero da Conta: {conta['numero_conta']}")
            print(f"Usuario: {conta['usuario']}")

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")