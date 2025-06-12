
""" Exercício Processos com Detalhes
Escreva um código que:

Liste o nome, o PID, o uso de RAM em MB e o uso de CPU (%) de todos os processos.

Só mostre os processos que estiverem usando mais de 0% de CPU.

Exiba tudo bem formatado, assim: """

processos = []

import psutil
for proc in psutil.process_iter():
    try:
        ram_usada = proc.memory_info().rss / (1024 ** 2)
        cpu_uso = proc.cpu_percent(interval=1)
        if cpu_uso > 0:
            print(f'Nome: {proc.name():<25}   |   PID: {proc.pid:<6}   |   Ram: {ram_usada:<6.2f} MB   |   CPU: {cpu_uso:<6}%')
    except:
        continue
