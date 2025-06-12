import psutil
#01
""" for proc in psutil.process_iter(['pid'], ['name']):
    try:
        print(proc.info['name'])
    except:
        continue


# 02
for proc in psutil.process_iter(['pid', 'name']):
    try:
        uso = proc.cpu_percent(interval=0.1)
        if uso > 0:
            print(f"{proc.info['name']} está usando {uso}% da CPU")
    except:
        continue
 """
# 03
""" Ordenar processos por uso de CPU
Tente por conta própria repetir o que já fez na missão anterior, 
mas ordenando pela RAM usada (dica: proc.memory_info().rss converte RAM para bytes). """


for proc in psutil.process_iter(['pid'], ['name']):
    try:
        print(proc.memory_info().rss)
    except:
        continue
