import random

def ln(x):
    print("-"*x)

serasa = [
    ["auridebson",2],
    ["luciana",5],
    ["guilherme",11],
    ["levy",14],
]

paises = (
    "Brasil",
    "Canadá",
    "Austrália",
    "Espanha",
    "Índia",
    "Estados Unidos da América"
)

carrinho = [
    ("maça",12.4),
    ("banana",3.4),
    ("pera",15.7),
    ("goiaba",4.5),
]

# 1
# for divida in serasa:
#     print(divida[1]**2)

# 2
# for pais in paises:
#     print(f"O país é {pais} e tem {len(pais)} letras.")

# 3
# total_carrinho = 0

# for item in carrinho:
#     total_carrinho += item[1]

# ln(40)
# print(f"O valor total do carrinho é R$ {total_carrinho}")
# ln(40)

#  4
palavras = [
    "Python",
    "é",
    "uma",
    "linguagem",
    "poderosa"
    
]

for palavra in palavras:
    if (len(palavra) > 4):
        print(f"|{palavra}| com {len(palavra)} letras")
