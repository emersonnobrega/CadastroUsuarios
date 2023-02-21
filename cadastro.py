usuarios = {}

# função para adicionar um novo usuário
def adicionar_usuario():
    email = input("Digite o e-mail do usuário: ")
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    sexo = input("Digite o sexo do usuário: ")
    usuarios[email] = {'nome': nome, 'idade': idade, 'sexo': sexo}
    print("Usuário adicionado com sucesso!")

# função para alterar os dados de um usuário existente
def alterar_usuario():
    email = input("Digite o e-mail do usuário que deseja alterar: ")
    if email in usuarios:
        nome = input("Digite o novo nome do usuário: ")
        idade = int(input("Digite a nova idade do usuário: "))
        sexo = input("Digite o novo sexo do usuário: ")
        usuarios[email] = {'nome': nome, 'idade': idade, 'sexo': sexo}
        print("Dados do usuário atualizados com sucesso!")
    else:
        print("Usuário não encontrado!")

# função para consultar os dados de um usuário existente
def consultar_usuario():
    email = input("Digite o e-mail do usuário que deseja consultar: ")
    if email in usuarios:
        print("Nome:", usuarios[email]['nome'])
        print("Idade:", usuarios[email]['idade'])
        print("Sexo:", usuarios[email]['sexo'])
    else:
        print("Usuário não encontrado!")

# função para excluir um usuário existente
def excluir_usuario():
    email = input("Digite o e-mail do usuário que deseja excluir: ")
    if email in usuarios:
        del usuarios[email]
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado!")


while True:
    print("Selecione uma opção:")
    print("1 - Adicionar usuário")
    print("2 - Alterar usuário")
    print("3 - Consultar usuário")
    print("4 - Excluir usuário")
    print("0 - Sair")

    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        adicionar_usuario()
    elif opcao == 2:
        alterar_usuario()
    elif opcao == 3:
        consultar_usuario()
    elif opcao == 4:
        excluir_usuario()
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")
