import os

def mostra_titulo():

    print("""
    ░█████╗░░█████╗░██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░  ██████╗░███████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
    ██║░░╚═╝███████║██║░░██║███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║  ██║░░██║█████╗░░
    ██║░░██╗██╔══██║██║░░██║██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║  ██║░░██║██╔══╝░░
    ╚█████╔╝██║░░██║██████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝  ██████╔╝███████╗
    ░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚══════╝
    ░█████╗░░█████╗░██████╗░██████╗░░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
    ██║░░╚═╝███████║██████╔╝██████╔╝██║░░██║╚█████╗░
    ██║░░██╗██╔══██║██╔══██╗██╔══██╗██║░░██║░╚═══██╗
    ╚█████╔╝██║░░██║██║░░██║██║░░██║╚█████╔╝██████╔╝
    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═════╝░""")

def mostra_escolha():
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. Ativar estoque")
    print("4. Sair")


def escolhe_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    def finalizar_programa():
        os.system('clear')
        print('Finalizando o programa\n')

    def opcao_ivalida():
        print('Esse carácter não é permitido\n')
        input('Aperte qualquer tecla para voltar')
        main()
    try:
        opcao_escolhida = int(input("Escolha uma opção"))

        if opcao_escolhida == 1:
            print('Voce escolheu Cadastrar carros')
        elif opcao_escolhida == 2:
            print('Voce escolheu Listar carros')  
        elif opcao_escolhida == 3:      
            print('Voce escolheu Ativar estoque')
        elif opcao_escolhidae == 4:
            finalizar_programa()
        else:
            finalizar_programa()
        else:
             opção_invalida()
    except:
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if ___name___ == '___main___':
    main(_)

