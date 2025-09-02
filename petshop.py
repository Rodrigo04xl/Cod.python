#   E:\petshop\petshop.py

animais = []
raca = []
tipo = [] 


def menu():                                            #mostra o menu e as opções.
    print("\nMenu da pet. Seja bem vindo!")
    print("1. Cadastrar animal.")
    print("2. Deletar animal.")
    print("3. Mostrar animais cadastrados.")
    print("4. Modificar animal.")
    print("5. Sair.")
    escolha()


def cadastro(): #Validações de nome antes
    while True:
        N = input("\nDigite o nome do seu animal: ").strip()
        if not N:
            print("\nEntrada vazia. Digite alguma coisa.")
            continue
        if N.isdigit():
            print("\nNao aceitamos numeros sozinhos, misture com letras")
            continue
        break


    while True:
        R = input("\nDigite a raça do seu animal: ").strip()
        if not R:
            print("\nEntrada vazia. Digite alguma coisa.")
            continue
        if R.isdigit():
            print("\nNao aceitamos numeros sozinhos, misture com letras.")
            continue
        break

    while True:
        T = input("\nDigite o tipo do seu animal: ").strip()
        if not T:
            print("\nEntrada vazia. Digite alguma coisa.")
            continue
        if T.isdigit():
            print("\nNao aceitamos numeros sozinhos, misture com letras.")
            continue
        break

    animais.append(N)
    raca.append(R)                              #adicionam as informações recebidas
    tipo.append(T)
    print(f"\nSeu novo animal cadastrado é: {N}, da raça: {R}, e do tipo {T}.")
    menu()


def delete():
    

    if not animais:
        print("Nenhum animal cadastrado")
        menu()

    mostrar() 
    
    while True:
        delet = input("Digite o nome do animal que deseja deletar ou 'Sair' para voltar: ")
        if delet.lower() == "sair":
            menu()
            return
        if delet in animais:
            index = animais.index(delet)
            animais.pop(index)
            raca.pop(index)
            tipo.pop(index)
            print(f"{delet} foi removido com sucesso.")
            break
        else:
            print("Animal não encontrado. Tente novamente.")
    menu()


def mostrar():
    print("\nLista de Animais:")
    for i in range(len(animais)):
        print(f"{i+1}. Animal: {animais[i]}, Raça: {raca[i]}, Tipo: {tipo[i]}")
    menu()


















#Trocar por match case
def escolha():      #recebe, verifica e analisa a resposta do usuario.

    try:
        resposta = int(input("Escolha uma opçao 1-5: "))
    except ValueError:
        resposta = -1

    match resposta:
        case 1:
            cadastro()
        case 2:
            delete()
        case 3:
            mostrar()
        case 4:
            Modificar()
        case 5:
            sair()
        case _:
            print("Digite uma opçao de 1-5 por favor.\n")
            menu()      


menu()
