age = int(input("Digite o valor da sua idade: "))

if age < 18:
    print(f"Você tem {age} anos e é menor de idade")
elif age >= 18 and age < 65:
    print(f"Você tem {age} anos e é maior de idade")
else:
    print(f"Você tem {age} anos e é idoso")


