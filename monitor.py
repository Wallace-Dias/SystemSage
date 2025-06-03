import psutil, time

# Cria ou abre o arquivo de log
with open("Monitoramento.txt", "a") as arquivo:
    
    #Cabeçalho
    arquivo.write("Monitoramento de Sistema CPU | RAM | DISCO\n")
    arquivo.write("-"*40 + "\n")

#coleta os dados a cada 5 segundos, 10 vezes
    for i in range(10):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        #Escreve no arquivo
        arquivo.write(f"CPU: {cpu}% | RAM: {ram}% | DISCO: {disk}%\n")

        #Aguarda 5 segundos
        time.sleep(5)


