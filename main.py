# A variável nome é um exemplo de um tipo STRING
nome = input("Seu nome: ")
# a variável idade é um exemplo de um tipo INT
idade = int(input("Sua idade: "))
# a variável altura é um exemplo do tipo FLOAT
altura = float(input("Altura(m): "))
# a variável tem_filhos é um exemplo do tipo BOOL
tem_filhos = input("Tem filhos? (Sim/Não): ").lower() == "sim"

print("- - - - - - - - - - - - - - - - - - -")
print("\nInformações coletadas:")
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Altura:", altura, "metros")
print("Tem filhos:", "sim" if tem_filhos else "não")
print("- - - - - - - - - - - - - - - - - - -")
print(f'Olá {nome}, sua idade é {idade}, tem {altura} m de altura sobre filhos? {"Sim,"if tem_filhos else "não"} tem.')




