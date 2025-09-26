def personalizar_perfil():
    print("Personalizar Perfil")

    nome_completo = input("\nNome completo: ")
    apelido = input("Nome de usuário (sem espaços): ")
    while True:
        avatar = input("URL da foto de perfil (https): ")
        if avatar.startswith("https://"):
            break
        print("Use um link que comece com https://")
    dominios = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com"]
    while True:
        email = input("Email: ").lower()
        if "@" in email and email.split("@")[-1] in dominios:
            break
        print(" Email inválido. Use gmail, hotmail, outlook ou yahoo.")
    while True:
        tipo = input("Tipo de usuário (leitor / autor / admin): ").lower()
        if tipo in ["leitor", "autor", "admin"]:
            break
        print(" Escolha entre: leitor, autor ou admin.")

    while True:
        telefone = input("Telefone com DDD (só números): ")
        if telefone.isdigit() and len(telefone) in [10, 11]:
            break
        print("Digite apenas números com DDD (10 ou 11 dígitos).")

    while True:
        senha = input("Senha (precisa ter pelo menos 1 letra maiúscula e 1 número): ")
        if any(c.isupper() for c in senha) and any(c.isdigit() for c in senha):
            break
        print("A senha deve conter pelo menos uma letra maiúscula e um número.")

    return {
        "nome": nome_completo,
        "usuario": apelido,
        "avatar": avatar,
        "email": email,
        "tipo": tipo,
        "telefone": telefone,
        "senha": senha
    }

def mostrar_perfil(perfil):
    print("\nPerfil")
    for chave, valor in perfil.items():
        print(f"{chave.capitalize()}: {valor}")


perfil = personalizar_perfil()
mostrar_perfil(perfil)
