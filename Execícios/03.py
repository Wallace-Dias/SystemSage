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
""" for proc in psutil.process_iter(['pid'], ['name']):
    cpu = psutil.cpu_percent(interval=0.1)
    if cpu > 0:
        try:
            print(proc.name(), f'Está usando: {cpu} % da CPU')
        except:
            continue """
    

""" Exercício 3 Mostrar uso de RAM dos processos
Objetivo: Escreva um código que mostre o nome do processo e 
quanto de memória RAM (em MB) ele está usando. """

# 03
""" for proc in psutil.process_iter(['pid'],['name']):
    ram = psutil.virtual_memory()
    ram_mb = ram.total / (1024 ** 2)
    try:
        print(proc.name(), f'Está usando {ram_mb:.2f} MB')
    except:
        continue
 """


