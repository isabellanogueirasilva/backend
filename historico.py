historico_leitura = [
    {
        "titulo": "dom casmurro",
        "autor": "machado de assis",
        "data_inicio": "01.09.2025",
        "data_fim": "10.09.2025",
        "status": "concluído"
    },
    {
        "titulo": "o pequeno príncipe",
        "autor": "antoine de saint-exupéry",
        "data_inicio": "15.09.2025",
        "data_fim": "",
        "status": "lendo"
    }
]

def mostrar_historico():
    categorias = ["lendo", "concluído", "abandonado"]
    descricoes = {
        "lendo": "livros que você está lendo:",
        "concluído": "livros que você terminou:",
        "abandonado": "livros que você abandonou:"
    }

    for cat in categorias:
        print("\n" + cat)
        print(descricoes[cat])
        livros = [l for l in historico_leitura if l["status"] == cat]

        if not livros:
            print("  nenhum livro nesta categoria.")
        else:
            for i, livro in enumerate(livros, 1):
                fim = livro["data_fim"] if livro["data_fim"] else "---"
                print(f"  {i}. {livro['titulo']} - {livro['autor']}")
                print(f"     (início: {livro['data_inicio']}, fim: {fim})")

def atualizar_status():
    if not historico_leitura:
        print("não há livros para atualizar.")
        return
    
    mostrar_historico()
    try:
        escolha = int(input("escolha o número do livro que quer atualizar: "))
        livro = historico_leitura[escolha - 1]
        status = input("digite o novo status (lendo / concluído / abandonado): ").lower()
        
        if status not in ["lendo", "concluído", "abandonado"]:
            print("status inválido.")
            return
        
        livro["status"] = status
        if status in ["concluído", "abandonado"]:
            livro["data_fim"] = input("digite a data de término (dd.mm.aaaa): ")
        else:
            livro["data_fim"] = ""
        
        print(f"livro '{livro['titulo']}' atualizado!")
    except (IndexError, ValueError):
        print("número inválido.")

def adicionar_livro():
    titulo = input("digite o título: ")
    autor = input("digite o autor: ")
    data_inicio = input("digite a data de início (dd.mm.aaaa): ")
    status = input("digite o status inicial (lendo / concluído / abandonado): ").lower()
    data_fim = ""
    if status in ["concluído", "abandonado"]:
        data_fim = input("digite a data de término (dd.mm.aaaa): ")
    
    historico_leitura.append({
        "titulo": titulo,
        "autor": autor,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "status": status
    })
    print(f"livro '{titulo}' adicionado!")

while True:
    print("\nmenu")
    print("1 - ver histórico")
    print("2 - adicionar livro")
    print("3 - atualizar status")
    opcao = input("escolha uma opção: ")

    if opcao == "1":
        mostrar_historico()
        input("\naperte enter para voltar ao menu...")
    elif opcao == "2":
        adicionar_livro()
        input("\naperte enter para voltar ao menu...")
    elif opcao == "3":
        atualizar_status()
        input("\naperte enter para voltar ao menu...")
    else:
        print("opção inválida.")
        input("\naperte enter para voltar ao menu...")
