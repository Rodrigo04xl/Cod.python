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
        R = input("Digite a raça do seu animal: ").strip()
        if not R:
            print("\nEntrada vazia. Digite alguma coisa.")
            continue
        if R.isdigit():
            print("\nNao aceitamos numeros sozinhos, misture com letras.")
            continue
        break

    while True:
        T = input("Digite o tipo do seu animal: ").strip()
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
    print(f"\n\nSeu novo animal cadastrado é: {N}, da raça: {R}, e do tipo {T}.")
    menu()







def delete():
    if not animais:
        print("Nenhum animal cadastrado")
        menu()
        return

    açao_mostrar()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Deletar animal")
        print("2. Sair")
        opcao = input("Digite o número da opção: ").strip() #strip tira todos os espaços vazios

        if opcao == '1':
            delet = input("Digite o nome do animal que deseja deletar: ").strip()
            nomes_animais_lower = [a.lower() for a in animais]
            if delet.lower() in nomes_animais_lower:
                index = nomes_animais_lower.index(delet.lower())
                removed_animal = animais.pop(index)
                raca.pop(index)
                tipo.pop(index)
                print(f"{removed_animal} foi removido com sucesso.")
                break  # Sai do loop e volta para o menu
            else:
                print("Animal não encontrado. Tente novamente.")

        elif opcao == '2':
            menu()
            return

        else:
            print("Opção inválida. Digite 1 ou 2.")

    menu()







def açao_mostrar():
    print("\nLista de Animais:")
    for i in range(len(animais)):
        print(f"{i+1}. Animal: {animais[i]}, Raça: {raca[i]}, Tipo: {tipo[i]}")

def mostrar_menu():
    print("\nLista de Animais:")
    for i in range(len(animais)):
        print(f"{i+1}. Animal: {animais[i]}, Raça: {raca[i]}, Tipo: {tipo[i]}")
    menu()







def modificar():
    if not animais:
        print("Nenhum animal cadastrado")
        menu()
        return

    açao_mostrar()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Modificar animal")
        print("2. Sair")
        opcao2 = input("Digite o número da opção: ").strip()
        
        if opcao2 == '1':
            modifi = input("Digite o nome do animal que deseja modificar: ").strip()
            nomes_animais_lower = [a.lower() for a in animais]
            if modifi.lower() in nomes_animais_lower:
                index = nomes_animais_lower.index(modifi.lower())

                # Solicita novos dados
                novo_nome = input("Digite o novo nome do animal: ").strip()
                nova_raca = input("Digite a nova raça: ").strip()
                novo_tipo = input("Digite o novo tipo: ").strip()

                # Atualiza nas listas
                animais[index] = novo_nome
                raca[index] = nova_raca
                tipo[index] = novo_tipo

                print(f"\nAnimal modificado com sucesso! Novo cadastro: "
                      f"{novo_nome}, Raça: {nova_raca}, Tipo: {novo_tipo}")
                break
            else:
                print("Animal não encontrado. Tente novamente.")

        elif opcao2 == '2':
            menu()
            return
        else:
            print("Opção inválida. Digite 1 ou 2.")

    menu()







def sair():
    print("\nAté mais!")







def  escolha(): 

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
            mostrar_menu()
        case 4:
            modificar()
        case 5:
            sair()
        case _:
            print("Digite uma opçao de 1-5 por favor.\n")
            menu()      


menu()
