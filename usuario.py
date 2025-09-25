usuarios = []

def cadastrar_usuario():
    print("Cadastro de Usuário ")
    while True:
        nome = input("Digite o nome completo (máx. 80 caracteres): ")
        if len(nome) > 80:
            print("Nome muito longo. Digite até 45 caracteres.")
        elif len(nome.strip()) == 0:
            print("Nome não pode ser vazio.")
        elif any(char.isdigit() for char in nome):
            print("O nome não pode conter números.")
        else:
            break
        
    dominios_validos = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com"]
    while True:
        email = input("Digite o email (máx. 150 caracteres): ")
        if len(email) > 150:
            print("Email muito longo. Digite até 150 caracteres.")
        elif "@" not in email:
            print("Email inválido. Deve conter '@'.")
        else:
            dominio = email.split("@")[-1]
            if dominio not in dominios_validos:
                print(f"Domínio inválido. Use apenas: {', '.join(dominios_validos)}")
            else:
                break

    while True:
        senha = input("Digite a senha (mín. 6 caracteres, com letra maiúscula e número): ")
        if len(senha) < 6:
            print("Senha muito curta. Digite pelo menos 6 caracteres.")
        elif not any(c.isupper() for c in senha):
            print("A senha deve conter pelo menos uma letra maiúscula.")
        elif not any(c.isdigit() for c in senha):
            print("A senha deve conter pelo menos um número.")
        else:
            break
        

    print("Tipos disponíveis: leitor / autor / adm")
    tipo = input("Digite o tipo: ").lower()
    if tipo not in ["leitor", "autor", "adm"]:
        print("Tipo inválido. Será definido como 'leitor' por padrão.")
        tipo = "leitor"

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "tipo": tipo
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, u in enumerate(usuarios, start=1):
            print(f"{i}.\n Nome: {u['nome']}  \nEmail: {u['email']}  \nTipo: {u['tipo']}")

while True:
    print(" Início ")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        listar_usuarios()
        break
    else:
        print("Opção inválida. Tente novamente.")
