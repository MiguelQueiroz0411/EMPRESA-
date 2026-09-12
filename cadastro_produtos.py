import os
from colorama import Fore, Style, init
init()


def validar_nome(nome):
    if nome.strip() == "":
        return False
    for char in nome:
        if char.isdigit() or (not char.isalpha() and char != " "):
            return False
        
    return True


def cadastrar_produto():
    print(Fore.LIGHTGREEN_EX + "\n=-=-=-=-=-=-=-=CADASTRAR PRODUTO=-=-=-=-=-=-=-=" + Style.RESET_ALL)
   
    while True:
        nome_produto = input(Fore.LIGHTMAGENTA_EX + "\nDigite o nome do produto: " + Style.RESET_ALL)
        if not validar_nome(nome_produto):
            print(Fore.LIGHTRED_EX + "Nome inválido" + Style.RESET_ALL)
            continue
        else:
            break
    
    while True:
        try:
            preco_produto = float(input(Fore.LIGHTMAGENTA_EX + "Digite o preço do produto: " + Style.RESET_ALL))
            if preco_produto <= 0:
                print(Fore.LIGHTRED_EX + "Preço inválido" + Style.RESET_ALL)
                continue
            else:
                with open("aluno.txt", "a", encoding="utf-8") as a:
                    a.write(f"{nome_produto}; {preco_produto}\n")
                print(Fore.LIGHTGREEN_EX + "\n=-=-=-=-=-=-=-=Produto cadastrado com sucesso=-=-=-=-=-=-=-= " + Style.RESET_ALL)
                print(Fore.LIGHTGREEN_EX + "Produto:", nome_produto + Style.RESET_ALL)
                print(Fore.LIGHTGREEN_EX + f"Preço: R$ {preco_produto:.2f}" + Style.RESET_ALL )
                return
        except ValueError:
            print(Fore.LIGHTRED_EX + "Digite apenas números" + Style.RESET_ALL)
            
cadastrar_produto()