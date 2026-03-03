print("Vamos definir sua classificação no time?\n")

idade = int(input("Digite sua idade: "))
categoria = input("Digite sua categoria(juvenil, adulto ou veterano): ")

if categoria == "juvenil":
    print("Você está no time de base.")
elif categoria == "adulto":
    print("Você está no time profissional.")
else:
    print("Você está no time Master.")
    
