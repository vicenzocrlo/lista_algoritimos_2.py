menu = """ \n
===================CALCULADORA=====================

Bem vindo a sua calculadora!

Escolha a operação que você gostaria de realizar:

[1]\tadição
[2]\tsubtração 
[3]\tmultiplicação
[4]\tdivisão

"""

print(menu)

operacao = int(input("Digite sua opção abaixo: "))
valor_1 = float(input("Digite o primeiro valor que deseja calcular: "))
valor_2 = float(input("Digite o segundo valor que deseja calcular: "))

soma = valor_1 + valor_2
sub = valor_1 - valor_2
mult = valor_1 * valor_2
div = valor_1 / valor_2

if operacao == 1:
    print(soma)
elif operacao == 2:
    print(sub)
elif operacao == 3:
    print(mult)
else:
    print(div)