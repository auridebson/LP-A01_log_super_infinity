import random

def ln(x):
    print("-"*x)

familia = [
    "auridebson",
    "luciana",
    "levy",
    "guilherme"
]

fam_removidos = []

ln(30)

while len(familia) != 0:
    fam_removidos.append(familia.pop())

print(familia)
ln(30)
print(fam_removidos)