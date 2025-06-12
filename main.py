""" 
Missão 1: Coletar Informações de Sistema
Objetivo: Criar um script Python que:

[x] - Mostre o uso da CPU (%)

[x] - Mostre o uso da RAM (em MB e %)

[x] - Mostre o uso do Disco (em GB e %)

[x] - Liste os 5 processos que mais consomem CPU


 """

# Monitor Básico.py

import psutil, time
#Lista para armazenar os processos com seus uss de CPU
processos = []

cpu = psutil.cpu_percent(interval=1)
ram_porcentagem = psutil.virtual_memory().percent
ram = psutil.virtual_memory()
disk = psutil.disk_usage("/")
disk_porcentagem = psutil.disk_usage("/").percent

#converter para MB
ram_total_mb = ram.total / (1024 ** 2)
ram_uso_mb = ram.used / (1024 ** 2)

#Converter para GB
disk_total_gb = disk.total / (1024 ** 3)
disk_uso_gb = disk.used / (1024 ** 3)


print(f"CPU: {cpu}% \nRAM: {ram_porcentagem}% \nDISCO: {disk_porcentagem}%\n")
#print(f"Ram Total: {ram_total_mb:.2f} MB")
print(f"Ram usada: {ram_uso_mb:.2f} MB")
#print(f"DISCO Total: {disk_total_gb:.2f} GB")
print(f"DISCO Usado: {disk_uso_gb:.2f} GB")

print("\nProcessos que mais consomem CPU: \n")

#Iterar pelos processos
for proc in psutil.process_iter(['pid', 'name']):
    try:
        uso_cpu = proc.cpu_percent(interval=0.1)
# Mede o uso de CPU em %
        processos.append((proc.info['pid'], proc.info['name'], uso_cpu)) 
    except (psutil.NoSuchProcess, psutil.AcessDenied):
        continue #ignora  processos que não podem ser acessados





#Ordena do maior para o menor uso de CPU
processos.sort(key=lambda x: x[2], reverse=True)

#Mostra os 5 primeiros
print("Top 5 processos que mais usam CPU: ")
for pid, nome, cpu in processos[:5]:
    print(f"PID: {pid: <6} | Nome: {nome: <25} | CPU: {cpu:.2f}%")

    
