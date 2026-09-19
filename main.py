from cadastro_produtos import cadastrar_produto
from cadastro_cliente import cadastrar_cliente
import os
from colorama import Fore, Style, init
init()


def menu():
    while True:
        try:
            print(Fore.LIGHTGREEN_EX + "\n=-=-=-=-=-=-=-=MENU=-=-=-=-=-=-=-=")
            print(Fore.LIGHTYELLOW_EX + "\n1 - Cadastro Produto" + Style.RESET_ALL)
            print(Fore.LIGHTCYAN_EX + "2 - Cadastro Cliente" + Style.RESET_ALL)
            print(Fore.LIGHTGREEN_EX + "3 - Sair" + Style.RESET_ALL)
            opcao = int(input(Fore.LIGHTBLUE_EX + "\nEscolha uma opção: " + Style.RESET_ALL))
            if opcao == 1:
                cadastrar_produto()
                
            elif opcao == 2:
                cadastrar_cliente()
                
            elif opcao == 3:
                break
            
            else:
                print(Fore.LIGHTRED_EX + "Opção invalida" + Style.RESET_ALL)

        except ValueError:
            print(Fore.LIGHTRED_EX + "Valor invalido" + Style.RESET_ALL)

menu()
