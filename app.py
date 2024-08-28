import os

carros = [
    {'nome': 'bmw', 'modelo': 'Gt', 'ativo': True},
    {'nome': 'volkswagen', 'modelo': 'GtI', 'ativo': False},
    {'nome': 'Fiat', 'modelo': 'uno', 'ativo': True}
]

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

def mostra_escolhas():
    print("1. Cadastrar carro")
    print("2. Listar carros")
    print("3. Ativar estoque")
    print("4. Sair")

def escolhe_opcao():
    
    def exibir_subtitulo(texto):
        os.system('clear')
        print(texto)
        print('')

    def retorna_menu():
        input('Digite uma tecla para voltar ao menu principal')
        main()

    def cadastra_carros():
        exibir_subtitulo('Cadastrar carro')
        nome_carro = input('Digite o nome do carro: ')
        modelo_carro = input('Digite o modelo do carro: ')
        ativo_carro = input('O carro está ativo? (s/n): ').lower() == 's'
        carros.append({'nome': nome_carro, 'modelo': modelo_carro, 'ativo': ativo_carro})
        print(f'O carro {nome_carro} foi cadastrado com sucesso\n')
        retorna_menu()

    def listar_carros():
        exibir_subtitulo('Lista de carros cadastrados')
        for carro in carros:
            nome_carro = carro['nome']
            modelo_carro = carro['modelo']
            ativo = 'Ativo' if carro['ativo'] else 'Inativo'
            print(f' - {nome_carro} | {modelo_carro} | {ativo}')
        retorna_menu()

    def finalizar_programa():
        os.system('clear')
        print('Finalizando o programa\n')

    def opcao_invalida():
        print('Essa opção não é válida\n')
        input('Aperte qualquer tecla para voltar')
        main()

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastra_carros()
        elif opcao_escolhida == 2:
            listar_carros()
        elif opcao_escolhida == 3:
            print('Você escolheu Ativar estoque')
            retorna_menu()
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()
