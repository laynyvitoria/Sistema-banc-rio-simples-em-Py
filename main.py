def exibir_menu():
    menu = '''
    MENU
    [D] Depósito
    [S] Sacar
    [E] Extrato
    [P] Encerrar programa
    '''
    print(menu)

def deposito(saldo):
    valor = float(input("Digite o valor que deseja depositar: \n"))
    saldo += valor
    print(f"Depósito de {valor} reais efetuado com sucesso.")
    return saldo

def saque(saldo, quantidades_saques):
    if quantidades_saques < 3:
        valor = float(input("Digite o valor que deseja sacar: \n"))
        saldo_insuficiente = valor > saldo
        limite_saque = 500
        if saldo_insuficiente:
            print("Infelizmente, não há saldo suficiente, tente novamente.")
        elif valor > limite_saque:
            print("Você ultrapassou o valor limite do saque.")
        else:
            saldo -= valor
            quantidades_saques += 1
            print(f"Saque de {valor} efetuado com sucesso.")
    else:
        print("Limite máximo de saques atingido.")

    return saldo, quantidades_saques

def extrato(saldo):
    if saldo == 0:
        print("Nenhuma movimentação realizada.")
    else:
        print(f"O valor disponível na sua conta é {saldo:.2f}")

def main():
    saldo = 0
    quantidades_saques = 0
    while True:
        exibir_menu()
        escolha = input("Escolha o que deseja fazer: ")
        if escolha == "D":
            saldo = deposito(saldo)
        elif escolha == "S":
            saldo, quantidades_saques = saque(saldo, quantidades_saques)
        elif escolha == "E":
            extrato(saldo)
        elif escolha == "P":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
