import psutil, os,  time

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




while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
    esq = input("Escolha: ")
    if esq.isdigit():
        esq = int(esq)
        if esq in (1, 2, 3):
            if esq == 1:
                mostrar_processos()
                input("\nPressione ENTER para voltar ao menu . . .")
            


            elif esq == 2:
                mostrar_processos_com_cpu()
                input("\nPressione ENTER para voltar ao menu . . .")

            elif esq == 3:
                print("Saindo . . .")
                time.sleep(2)
                break
        else:
            print("Opção inválida, Escolha novamente: ")
            time.sleep(1.5)
    else:
        print("Não é um número, tente novamente!")
        time.sleep(1.5)


        

        
    
    
