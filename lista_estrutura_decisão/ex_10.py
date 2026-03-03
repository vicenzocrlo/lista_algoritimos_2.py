saldo = 0 

while True:

    menu = """\n
    =======================MENU==============================

    Bem-vindo a sua Conta Bancária!

    Por favor, para avançar selecione uma das opções abaixo:

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tSair
    """

    print(menu)
    opcao = int(input("Digite sua opção aqui: "))

    if opcao == 1:
        valor = float(input("Qual valor você deseja depositar?: "))
        saldo +=valor
        print(f"O valor de {valor:.2f} reais foi depositado a sua conta!")

    elif opcao == 2:
        valor_2 = float(input("Qual valor você deseja sacar?: "))
        if valor_2 <= saldo:
            saldo -= valor_2
            print(f"Saque de {valor_2:.2f} reais realizado com sucesso!")
        else:
            print("Saldo insuficiente, não foi possível realizar o saque!")

    elif opcao == 3:
        print(f"Seu saldo atual é de {saldo:.2f} reais.")

    elif opcao == 4:
        print("Saindo do sistema.")
        break

    else:
        print(("Opção inválida. Tente novamente."))


