import os,  time, funcoes




while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    funcoes.menu()
    esq = input("Escolha: ")
    if esq.isdigit():
        esq = int(esq)
        if esq in (1, 2, 3):
            if esq == 1:
                funcoes.mostrar_processos()
                input("\nPressione ENTER para voltar ao menu . . .")
            


            elif esq == 2:
                funcoes.mostrar_processos_com_cpu()
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


        

        
    
    
