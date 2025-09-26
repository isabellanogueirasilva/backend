avaliacoes = [
    {
        "usuario": "Maria123",
        "id_livro": 9783161484100,
        "livro": "O Pequeno Príncipe",
        "nota": 5,
        "comentario": "Livro incrível! Muito inspirador.",
        "data": "2025-09-26"
    },
    {
        "usuario": "Joao456",
        "id_livro": 9780131103627,
        "livro": "1984",
        "nota": 4,
        "comentario": "Boa leitura, mas alguns capítulos são lentos.",
        "data": "2025-09-25"
    }
]

def mostrar_avaliacoes():
    print("\n Avaliações de Livros \n")
    for avaliacao in avaliacoes:
        print(f"Usuário: {avaliacao['usuario']}")
        print(f"ID Livro: {avaliacao['id_livro']} - Livro: {avaliacao['livro']}")
        print(f"Nota: {'⭐' * avaliacao['nota']}")
        print(f"Comentário: {avaliacao['comentario']}")
        print(f"Data da avaliação: {avaliacao['data']}")
        print("-" * 50)

mostrar_avaliacoes()

novo_usuario = input("Nome do usuário: ")

while True:
    try:
        novo_id_livro = int(input("ID do livro (exatamente 13 dígitos): "))
        if len(str(novo_id_livro)) == 13:
            break
        else:
            print("ID inválido! Deve ter exatamente 13 dígitos.")
    except ValueError:
        print("Digite apenas números!")

novo_livro = input("Nome do livro: ")
nova_nota = int(input("Sua nota (1 a 5): "))
novo_comentario = input("Seu comentário: ")

avaliacoes.append({
    "usuario": novo_usuario,
    "id_livro": novo_id_livro,
    "livro": novo_livro,
    "nota": nova_nota,
    "comentario": novo_comentario,
    "data": "2025-09-26"
})

print("\nAvaliação adicionada com sucesso!")
mostrar_avaliacoes()
