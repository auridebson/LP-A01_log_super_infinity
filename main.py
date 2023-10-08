nome = input("Seu nome: ")
idade = int(input("Sua idade: "))
altura = float(input("Altura(m): "))
tem_filhos = input("Tem filhos? (Sim/Não): ").lower() == "sim"

print("- - - - - - - - - - - - - - - - - - -")
print("\nInformações coletadas:")
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Tem filhos:", "sim" if tem_filhos else "não")
print("- - - - - - - - - - - - - - - - - - -")
print(f'Olá {nome}, sua idade é {idade}, tem {altura} m de altura sobre filhos? {"Sim,"if tem_filhos else "não"} tem.')




