#Importações para todos os códigos neste arquivo.
import psutil


""" 
Exercício 1 Listando nomes de processos
Objetivo: Escreva um código que imprima o nome de todos os 
processos ativos no seu sistema. """

# 01
for proc in psutil.process_iter():
    try:
        print(proc.name())
    except:
        continue



"""  Exercício 2 Processos que usam CPU
Objetivo: Escreva um código que mostre apenas os 
processos que estão usando mais de 0% de CPU. """

#02

for proc in psutil.process_iter(['pid', 'name']):
    try:
        uso = proc.cpu_percent(interval=0.1)
        if uso > 0:
            print(proc.name(), f"está usando {uso:.2f}% da CPU")
    except:
        continue






""" Exercício 3 Mostrar uso de RAM dos processos
Objetivo: Escreva um código que mostre o nome do processo e 
quanto de memória RAM (em MB) ele está usando. """

# 03

for proc in psutil.process_iter(['pid', 'name']):
    try:
        ram_usada = proc.memory_info().rss / (1024 ** 2)
        print(proc.name(), f"está usando {ram_usada:.2f} MB de RAM")
    except:
        continue
