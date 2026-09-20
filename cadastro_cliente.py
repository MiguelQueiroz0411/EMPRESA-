import os
from colorama import Fore, Style, init
init()

def validar_nome(nome):
    if not nome.strip():
        return False
    for char in nome:
        if char.isdigit() or (not char.isalpha() and char != " "):
            return False
    return True

def validar_telefone(telefone):
    if not telefone.strip():
        return False
    caracteres_permitidos = " ()-+"
    tem_digito = False
    
    for char in telefone:
        if char.isdigit():
            tem_digito = True
        elif char not in caracteres_permitidos:
            return False
            
    return tem_digito

def cadastrar_cliente():
    print(Fore.YELLOW + "--- CADASTRO DE CLIENTE ---" + Style.RESET_ALL)
    
    while True:
        nome = input(Fore.CYAN + "Digite o nome do cliente: " + Style.RESET_ALL).strip()
        if validar_nome(nome):
            break
        print(Fore.RED + "Erro: Nome inválido (não pode conter números, símbolos ou ficar em branco).\n" + Style.RESET_ALL)
        
    while True:
        email = input(Fore.CYAN + "Digite o e-mail: " + Style.RESET_ALL).strip()
        if "@" in email and "." in email:
            break
        print(Fore.RED + "Erro: E-mail inválido. Digite um e-mail que contenha '@' e '.'.\n" + Style.RESET_ALL)
        
    while True:
        telefone = input(Fore.CYAN + "Digite o telefone: " + Style.RESET_ALL).strip()
        if validar_telefone(telefone):
            break
        print(Fore.RED + "Erro: Telefone inválido. Digite apenas números e caracteres válidos (ex: (11) 99999-9999).\n" + Style.RESET_ALL)

    with open("cliente.txt", "a", encoding="utf-8") as a:
        a.write(f"Nome: {nome}; E-mail: {email}; Telefone: {telefone};\n")
    print(Fore.LIGHTGREEN_EX + "\n=-=-=-=-=-=-=-= Cliente cadastrado com sucesso =-=-=-=-=-=-=-=" + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + f"Nome: {nome}" + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + f"E-mail: {email}" + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + f"Telefone: {telefone}" + Style.RESET_ALL)

