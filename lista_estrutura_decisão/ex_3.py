age = int(input("Digite o valor da sua idade: "))

if age <= 12:
    print(f"Você é uma Criança.")
elif age >= 13 and age <= 17:
    print(f"Você é um Adolescente.")
elif age >= 18 and age <= 64:
    print("Você é um Adulto.")
else:
    print("Você é um Idoso.")