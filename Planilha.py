import sqlite3

conexao = sqlite3.connect("Planilha.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS planilha (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    categoria TEXT NOT NULL,
    valor REAL NOT NULL,
    data TEXT NOT NULL
)
""")

while True:
    print("""
===== CONTROLE DE GASTOS =====

1. Adicionar gasto
2. Listar gastos
3. Ver total gasto
4. Atualizar
5. Sair

=============================
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Gasto: ")
        descricao = input("Descrição: ")
        categoria = input("Categoria: ")
        valor = float(input("Valor R$: "))
        data = input("Data: ")

        cursor.execute("INSERT INTO planilha (nome, descricao, categoria, valor, data) VALUES (?, ?, ?, ?, ?)", (nome, descricao, categoria, valor, data))

        conexao.commit()

        print("Adicionado na tabela com sucesso: ")

    elif opcao == "2":
        cursor.execute("SELECT * FROM planilha")
        gastos = cursor.fetchall()

        if not gastos:
            print("Nenhum gasto cadastrado")

        else:
            for gasto in gastos:
                print(f"ID: {gasto[0]} | Nome: {gasto[1]} | Descrição: {gasto[2]} | Categoria: {gasto[3]} | Valor: {gasto[4]:.2f} | Data: {gasto[5]}")

    elif opcao == "3":
        cursor.execute("SELECT SUM(valor) FROM planilha")

        total = cursor.fetchone()[0]

        if total is None:
            total = 0

        print(f"Total gasto: R$ {total:.2f}")

    elif opcao == "4":
        id_gasto = int(input("ID do gasto que você quer atualizar: "))
        novo_gasto = input("Gasto: ")
        nova_descricao = input("Descrição: ")
        nova_categoria = input("Categoria: ")
        novo_valor = int(input("Valor R$: "))
        nova_data = input("Data: ")

        cursor.execute("UPDATE planilha SET nome ?, descricao ?, categoria ?, valor ?, data ? WHERE id ?)", (novo_gasto, nova_descricao, nova_categoria, novo_valor, nova_data, id_gasto))
        conexao.commit()

        print("Gasto atualizado!")

    elif opcao == "5":
        print("Saindo...")
        break

conexao.close()
