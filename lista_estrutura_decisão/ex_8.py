print("Vamos descobrir a classificação do seu IMC?\n")

peso = float(input("Digite o seu peso atual: "))
altura = float(input("Digite a sua altura atual: "))

imc = peso / (altura ** 2)

print(f"{imc:.2f}")

if imc < 18.5:
    print("Você está Abaixo do peso.")
elif imc >= 18.5 and imc < 25:
    print("Você está no seu peso normal.")
elif imc >= 25 and imc < 30:
    print("Você está com Sobrepeso.")
else:
    print("Você está obeso.")



