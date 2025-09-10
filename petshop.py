#   E:\petshop\petshop.py
animais = []
raca = []
tipo = []

# NOTE reordenei as funções para facilitar a leitura do código
# NOTE aqui temos as funçoes que podem ser reutilizadas em outras partes do código


def escolha():
    try:
        return int(input("Opção: "))
    except ValueError:
        return -1


def listar_pets():  # NOTE alterei o nome para algo mais descritivo
    print("\nLista de Animais:")
    for i in range(len(animais)):
        print(
            f"{i + 1}. Animal: {animais[i]}, Raça: {raca[i]}, Tipo: {tipo[i]}")


# NOTE alterei a numeração para facilitar a adição de mais funções caso necessário
# NOTE removi a chamada da escolha() de dentro do menu() por que na main ela ja é chamada
def menu():  # mostra o menu e as opções.
    print("\nMenu da pet. Seja bem vindo!")
    print("1. Cadastrar animal.")
    print("2. Deletar animal.")
    print("3. Mostrar animais cadastrados.")
    print("4. Modificar animal.")
    print("0. Sair.")


# NOTE aqui temos as funções principais do programa
def cadastro():  # Validações de nome antes
    # NOTE coloquei nomes de variaveis mais descritivos para facilitar a leitura do código
    while True:
        nome_pet = input("\nDigite o nome do seu animal: ").strip()
        if not nome_pet:
            print("\nEntrada vazia. Digite alguma coisa.")
            continue
        if nome_pet.isdigit():
            print("\nNao aceitamos numeros sozinhos, misture com letras")
            continue
        break

    while True:
        raca_pet = input("Digite a raça do seu animal: ").strip()
        if not raca_pet:
            print("\nEntrada vazia. Digite alguma coisa.")
            continue
        if raca_pet.isdigit():
            print("\nNao aceitamos numeros sozinhos, misture com letras.")
            continue
        break

    while True:
        tipo_pet = input("Digite o tipo do seu animal: ").strip()
        if not tipo_pet:
            print("\nEntrada vazia. Digite alguma coisa.")
            continue
        if tipo_pet.isdigit():
            print("\nNao aceitamos numeros sozinhos, misture com letras.")
            continue
        break

    animais.append(nome_pet)  # adicionam as informações recebidas as listas
    raca.append(raca_pet)
    tipo.append(tipo_pet)
    print(
        f"\n\nSeu novo animal cadastrado é: {nome_pet}, da raça: {raca_pet}, e do tipo {tipo_pet}."
    )


def delete():
    if not animais:
        print("Nenhum animal cadastrado")
        return

    listar_pets()

    while True:
        print("\nEscolha uma opção:")
        print("1. Deletar animal")
        print("2. Sair")
        # strip tira todos os espaços vazios do começo e do fim da string, exemplo: "  oi  " vira "oi"
        opcao = escolha()  # NOTE alterei para usar a função escolha() que já trata erros

        if opcao == 1:  # NOTE alterei para usar numeros ao invés de strings
            delet = input(
                "Digite o nome do animal que deseja deletar: ").strip()
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

        elif opcao == 2:
            return

        else:
            print("Opção inválida. Digite 1 ou 2.")


def modificar():#XXX A modificação de dados não tem as mesmas validações que o cadastro
    if not animais:
        print("Nenhum animal cadastrado")
        return

    listar_pets()

    while True:
        print("\nEscolha uma opção:")
        print("1. Modificar animal")
        print("2. Sair")
        opcao = escolha()  # NOTE alterei para usar a função escolha() que já trata erros

        if opcao == 1: # NOTE alterei para usar numeros ao invés de strings
            modifi = input(
                "Digite o nome do animal que deseja modificar: ").strip()
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

                print(
                    f"\nAnimal modificado com sucesso! Novo cadastro: "
                    f"{novo_nome}, Raça: {nova_raca}, Tipo: {novo_tipo}"
                )
                break
            else:
                print("Animal não encontrado. Tente novamente.")

        elif opcao == 2:
            return
        else:
            print("Opção inválida. Digite 1 ou 2.")


def main():
    while True:  # NOTE com esse loop o programa roda até o usuário escolher sair
        menu()

        resposta = escolha()

        match resposta:
            case 1:
                cadastro()
            case 2:
                delete()
            case 3:
                listar_pets()
            case 4:
                modificar()
            case 0:  # NOTE alterei para 0 para facilitar a adição de mais funções caso necessário
                # NOTE aqui pode ser direto a mensagem e o break, nao é necessario criar uma função só pra isso
                print("\nAté mais!")
                break
            case _:
                print("Digite uma opçao de válida por favor.\n")


# NOTE com esse comando o programa roda apenas se for o arquivo principal (main)
if __name__ == "__main__":
    main()
