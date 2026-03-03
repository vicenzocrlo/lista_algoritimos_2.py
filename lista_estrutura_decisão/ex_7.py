print("Olá! Vamos calcular a sua nota?\n")

nota = int(input("Digite o valor da sua nota(0-100): "))

if nota < 60:
    print("O valor da sua nota foi F")
elif nota >= 60 and nota < 70:
    print("O valor da sua nota foi D")
elif nota >= 70 and nota < 80:
    print("O valor da sua nota foi C")
elif nota >= 80 and nota < 90:
    print("O valor da sua nota foi B")
else:
    print("O valor da sua nota foi A")