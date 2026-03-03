valor = float(input("Digite o valor do seu produto: "))

if valor >= 100:
    desconto = (valor * 0.1)
    final = (valor - desconto)
    print(f"O valor do seu produto após o desconto aplicado foi {final:.2f} reais.")

else:
    print(f"Não foi possível aplicar o desconto ao seu produto, o valor final foi {valor:.2f} reais.")