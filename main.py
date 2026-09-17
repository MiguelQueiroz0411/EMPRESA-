from time import sleep

print('--' * 30)
print('BEM VINDO A EMPRESA +')
print("você está na interface de cadastro, tenha cuidado!")
print('-=' * 10)

opcao = 0

while opcao != 3:
    print('''[1] Cadastrar cliente
[2] Cadastrar produto
[3] Sair''')

    entrada = input('>>>>> selecione uma opção: ').strip()

    # Valida se a entrada contém apenas dígitos
    if not entrada.isdigit():
        print('Erro: A entrada contém caracteres inválidos. Digite apenas números (1, 2 ou 3).')
        print('-=' * 10)
        sleep(1.5)
        continue

    opcao = int(entrada)

    if opcao == 1:
        cadastro_cliente = str(input('Digite o nome do cliente que sera cadastrado: ')).strip()
        telefone = str(input('Digite o número do cliente que está sendo cadastrado: ')).strip()
        email = str(input('Insira o email do cliente que está sendo cadastrado: ')).strip()

        with open("clientes.txt", "a", encoding="utf-8") as arquivo_clientes:
            arquivo_clientes.write(f"Nome: {cadastro_cliente} | Tel: {telefone} | Email: {email}\n")
        print(f'Cliente {cadastro_cliente} cadastrado com sucesso.')

    elif opcao == 2:
        cadastro_produto = str(input('Digite o nome do Produto que você quer cadastrar: ')).strip()

        with open("produtos.txt", "a", encoding="utf-8") as arquivo_produtos:
            arquivo_produtos.write(f"Produto: {cadastro_produto}\n")
        print('Produto cadastrado com sucesso.')

    elif opcao == 3:    
        print('FINALIZANDO...')
    else:
        print('Opção inválida: Digite apenas os números correspondentes às opções (1, 2 ou 3).')

    print('-=' * 10)
    sleep(1.5)

print('FIM DO CADASTRO')