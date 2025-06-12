""" 
Exercícios para fixar
[] - Exercício 1 – Usando try/except
Crie um código que peça um número ao usuário e trate o erro se ele digitar uma letra.

[] - Exercício 2 – Usando continue
Liste os números de 1 a 10, mas pule os números pares.

[] - Exercício 3 – Usando .append()
Crie uma lista com os 3 jogos que você mais gosta, um por vez, usando .append(). 
"""

# Exercício 1
try:
    n = int(input("Digite um número: "))
except:
    print("Erro de sintaxe")
print("\n")

# Exercício 2

for n in range(10):
    if n % 2 == 0:
        continue
    else:
        print(n)
    
print("\n")

# Exercício 3
jogos = []
jogos.append("Resident Evil")
jogos.append("Need for Speed")
jogos.append("Silent Hill")
print(jogos)
