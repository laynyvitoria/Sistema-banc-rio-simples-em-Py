menu = '''
MENU
[D] Depósito
[S] Sacar
[E] Extrato
[P] Encerrar programa
'''
saldo = 0
quantidades_saques = 0
while True:
    print(menu)
    escolha = input("Escolha o que deseja fazer: \n")

    if escolha == "D":
        valor = float(input("Digite o valor desejado:"))
        saldo += valor
        print(f"Deposito de {valor} reais efetuado com sucesso.")

    elif escolha == "S":
        if quantidades_saques < 3:
            valor = float(input("Digite o valor que seja sacar: \n"))
            saldo_insuficiente = valor > saldo
            limite_saque = 500
            if saldo_insuficiente:
                print("Infelizmente, não há saldo suficiente, tente novamente")
            elif valor > limite_saque:
                print("Você ultrapassou o valor limite do saque")
            else:
                saldo -= valor
                quantidades_saques += 1
                print(f"Saque de {valor} efetuado com sucesso.")
        else:
            print("Limite máximo de saques atingido")
    elif escolha == "E":
        if saldo == 0:
            print("Nenhuma movimentação realizada.")
        else:
            print(f"O valor disponível na sua conta é {saldo: .2f} reais.")
    elif escolha == "P":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
