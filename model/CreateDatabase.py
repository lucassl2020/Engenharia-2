from model.ApplySqlCommand import abrir_banco_de_dados, fechar_banco_de_dados, apply_sql_command

def create_database():
    conexao, cursor = abrir_banco_de_dados()

    sql_command = """CREATE TABLE IF NOT EXISTS Pecas(
                codigo INTEGER PRIMARY KEY UNIQUE NOT NULL,
                nome TEXT NOT NULL,
                valor_de_custo REAL NOT NULL,
                valor_de_venda REAL NOT NULL,
                codigo_fornecedor INTEGER NOT NULL,
                CONSTRAINT fk_peca_fornecedor FOREIGN KEY (codigo_fornecedor) REFERENCES Fornecedores (codigo)
            );"""
    apply_sql_command(cursor, sql_command)

    sql_command = """CREATE TABLE IF NOT EXISTS Vendas(
                codigo INTEGER PRIMARY KEY AUTOINCREMENT, 
                quantidade INTEGER NOT NULL,
                valor_total REAL NOT NULL,
                data TEXT NOT NULL,
                cpf_cliente INTEGER NOT NULL, 
                codigo_peca INTEGER NOT NULL,
                CONSTRAINT fk_venda_cliente FOREIGN KEY (cpf_cliente) REFERENCES Clientes (cpf),
                CONSTRAINT fk_venda_peca FOREIGN KEY (codigo_peca) REFERENCES Pecas (codigo)
            );"""
    apply_sql_command(cursor, sql_command)

    sql_command = """CREATE TABLE IF NOT EXISTS Clientes(
                cpf INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                data_de_nascimento TEXT NOT NULL,
                telefone TEXT NOT NULL             
            );"""
    apply_sql_command(cursor, sql_command)


    sql_command = """CREATE TABLE IF NOT EXISTS Fornecedores(
                cnpj TEXT PRIMARY KEY UNIQUE NOT NULL,
                nome_fantasia TEXT NOT NULL,
                razao_social TEXT NOT NULL,
                telefone TEXT NOT NULL,
                endereco TEXT NOT NULL,
                inscricao_estadual TEXT NOT NULL,
                email TEXT NOT NULL
            );"""
    apply_sql_command(cursor, sql_command)

    fechar_banco_de_dados(conexao)


create_database()
