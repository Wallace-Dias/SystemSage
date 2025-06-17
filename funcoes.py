import psutil
def menu():
    print("[1] - Mostrar Processos \n[2] - Mostrar Processos com CPU \n[3] - Sair")

def mostrar_processos():
    print("Processos")
    for proc in psutil.process_iter():
        try:
            ram_usada = proc.memory_info().rss / (1024 ** 2)
            cpu_uso = proc.cpu_percent(interval=1)

            print(f"Nome: {proc.name():<25} | PID: {proc.pid:<15} | RAM: {ram_usada:<15.2f} MB | CPU {cpu_uso:<15}%")
        except:
            continue

def mostrar_processos_com_cpu ():
    print("Processos com CPU")

    for proc in psutil.process_iter():
        try:
            ram_usada = proc.memory_info().rss / (1024 ** 2)
            cpu_uso = proc.cpu_percent(interval=1)

            if cpu_uso > 0:
                print(f"Nome: {proc.name():<25} | PID: {proc.pid:<15} | RAM: {ram_usada:<15.2f} MB | CPU {cpu_uso:<15}%")
        except:
            continue

