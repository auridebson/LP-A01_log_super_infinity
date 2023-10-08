nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
tem_filhos = input("Você tem filhos? (Sim/Não): ").lower() == "sim"

print("\nInformações do Usuário:")
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Tem filhos:", "Sim" if tem_filhos else "Não")





