""" Exercício Preparatório
Antes da missão, faça este exercício:

🧪 Crie um programa com:
Uma função chamada mostrar_mensagem() que imprime "Sistema Jarvis Alpha 0.1 iniciado!".

Outra função chamada menu() que:

Mostra as opções 1 - Ver algo | 2 - Sair

Recebe a escolha do usuário com input() e imprime o que ele escolheu. """


def mostrar_mensagem():
    print("Sistema Jarvis Alpha 0.1 Iniciado!")

def menu():
    print("[1] - Ver algo\n[2] - Sair")
    esc = int(input("Digite algo: "))

    if esc == 1:
        print("Mensagem")
    else:
        print("Saindo.")

mostrar_mensagem()
menu()