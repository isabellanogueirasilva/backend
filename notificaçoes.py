notificacoes = [
    {"id": 1, "mensagem": "Novo livro disponível: 'O Senhor dos Anéis'.", "status": "não lida", "data": "26/09/2025"},
    {"id": 2, "mensagem": "Sua leitura de 'Dom Casmurro' está em 50%.", "status": "lida", "data": "25/09/2025"},
    {"id": 3, "mensagem": "Promoção: livros de fantasia com 30% OFF.", "status": "não lida", "data": "24/09/2025"},
    {"id": 4, "mensagem": "Você ganhou um cupom de desconto para seu próximo livro!", "status": "não lida", "data": "23/09/2025"},
    {"id": 5, "mensagem": "Atualização: nova versão do app com recomendações personalizadas.", "status": "lida", "data": "22/09/2025"}
]

def mostrar_notificacoes():
    print("Notificações")
    if not notificacoes:
        print("Nenhuma notificação disponível.")
    else:
        for n in notificacoes:
            status = "🔴 Não lida" if n["status"] == "não lida" else "🟢 Lida"
            print(f"ID: {n['id']} | {status}\nMensagem: {n['mensagem']}\nData: {n['data']}\n")

def ler_notificacao():
    if not notificacoes:
        print("\nNão há notificações para ler.")
        return
    
    id_escolhido = int(input("Digite o ID da notificação que deseja ler: "))
    for n in notificacoes:
        if n["id"] == id_escolhido:
            print(f"\n📖 Lendo notificação: {n['mensagem']}")
            notificacoes.remove(n) 
            print("✅ Notificação removida da lista.")
            return
    print("⚠️ Notificação não encontrada.")


while True:
    mostrar_notificacoes()
    opcao = input("\nDeseja ler uma notificação? (sim/não): ").lower()
    if opcao == "sim":
        ler_notificacao()
    else:
        print("Saindo")
        break
