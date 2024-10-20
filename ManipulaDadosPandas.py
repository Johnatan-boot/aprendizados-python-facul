#primeiro Modulo
import math
math.sqrt(25)
math.log2(1024)
math.cos(45)
import math as m

m.sqrt(25)
m.log2(1024)
m.cos(45)

#terceiro modulo
from math import sqrt, log2, cos

sqrt(25)
log2(1024)
cos(45)


import matplotlib.pyplot as plt

#Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]
#Criar um grafico de linha
plt.plot(x,y)

#Adicionar rótulos aos eixos
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')


#Adicionar um titúlo ao gráfico
plt.title('Exemplo de grafico de linha')


#Mostrar o gráfico
plt.show()

#Dados de exemplo
meses = ['janeiro', 'Fevereiro', 'Março', 'Abril','Maio']
vendas = [120, 90, 80, 200, 150] # added a value to vendas to match the length of meses

#Criar um gráfico de barras
plt.bar(meses, vendas, color = 'royalblue')

#Adicionar rótulos aos eixos
plt.xlabel('Mês')
plt.title('Vendas em (unidades)')

#Adicionar um titulo ao grafico
plt.title('Vendas Mensais')


#Mostrar graficos
plt.show()

import matplotlib.pyplot as plt

#Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}"import matplotlib.pyplot as plt

#Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}"

    # Criando uma lista de livros
    biblioteca = []

    # Lista para armazenar anos de publicacão
    anos = []

    # Função para adicionar um livro á biblioteca
    def adicionar_livro(titulo, autor, ano_publicacao):
        novo_livro = Livro(titulo, autor, ano_publicacao)
        biblioteca.append(novo_livro)
        anos.append(ano_publicacao)  # Adicionar o ano á lista anos
        print(f"O livro '{titulo}' foi adionado á biblioteca.")

        # Função para listar totods os livros na biblioteca
        def listar_livros():
            print("Livro na Biblioteca:")
            for livro in biblioteca:
                print(livro)

        # Acionar algun livros á biblioteca
        adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
        adicionar_livro("Orgulho e Preconceito", "Jane Austen", 1813)
        adicionar_livro("1984", "George Orwell", 1949)
        adicionar_livro("Cem Anos de Solidão", "Gabriel Garcia Marquez", 1967)
        adicionar_livro("Apanhador no Campo de Centeio", "J.D Sallinger", 1951)


import sqlite3

# 1. Conectar ao banco de dados (ou cria um novo)
conn = sqlite3.connect('exemplo.db')

# 2. Cria um objeto cursor
cursor = conn.cursor()  # Get a cursor object from the active connection

# 3. Criar a tabela
create_table = """
 CREATE TABLE IF NOT EXISTS Produtos (
 id INTEGER PRIMARY KEY,
 nome TEXT NOT NULL,
 preco REAL NOT NULL,
 estoque INTEGER
 );
 """

# 4. Executar o comando SQL para criar a tabela
cursor.execute(create_table)

# 5. Confirmar as alterações (commit)
conn.commit()

# 6. Fechar a conexão com o banco de dados
conn.close()
#Adicionar produto
import sqlite3
#Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# Dados do novo produto
novo_produto = ('Camiseta', 19.99, 50)
#Comando SQL para inserir o novo produto na tabela
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES(?, ?, ?)"
#executando o comando SQL para inserção
cursor.execute(inserir_produto, novo_produto)
#Confirmando as alterações
conn.commit()
#Fechando a conexão
conn.close()

import sqlite3


#Visualizar produto

#Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
#Comando SQL para selecionar todos os produtos
selecionar_produtos = "SELECT * FROM Produtos"
#executando o comando SQL
cursor.execute(selecionar_produtos)
#Obtendo todos os registros e exibindo-os
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)
#fechando a conexão
conn.close()

#atualizar produto
import sqlite3
#Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
#novo preço e id do produto a ser atualizado
novo_preco = 24.99
produto_id = 1 # Suponhamos que queremos atualizar o produto  com ID 1

#Comando SQL para atualizar o preço do produto
atualizar_preco = "UPDATE Produtos SET preco = ? where id = ? "
#Executando o comando SQL de atualização
cursor.execute(atualizar_preco, (novo_preco, produto_id))
#Confirmando alterações
conn.commit()
#Fechando conexão
conn.close()

#excluir produto
import sqlite3
#Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# ID do produto a ser excluido
produto_id = 2  #Suponhamos que queremos excluir o produto com id=2
#Comando SQL para excluir produto
excluir_produto = "DELETE FROM Produtos WHERE id = ?"

#Executndo o comando SQL DE EXCLUSAO
cursor.execute(excluir_produto, (produto_id,))
#Confirmando as alterações
conn.commit()
#Fechando a conexão
conn.close()

import sqlite3
#CREATE (criação da tabela e inserção de dados de exemplo)
conn = sqlite3.connect(' contatos.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT,
      email TEXT,
      telefone TEXT
    )
""")
dados_fake = [
    ('João', 'joão@mail.com', '123-456-7890'),
    ('Maria', 'maria@mail.com', '987-654-3210'),
    ('Carlos', 'carlos@mail.com', '555-555-5555'),


]

cursor.executemany('INSERT INTO Contatos (nome, email, telefone) VALUES( ?, ?, ?)', dados_fake)
conn.commit()

#READ (LEITURA E EXIBIÇÃO DOS CONTATOS)
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print("Contatos:")
for contato in contatos:
    print(contato)
#UPDATE (Atualização do número de telefone do contato com ID 2)


novo_telefone = '999-999-9999'
contato_id = 2
cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_telefone, contato_id))
conn.commit()

#Executndo o comando SQL DE EXCLUSAO
# Corrected line: Added a comma to make it a tuple.
cursor.execute('DELETE FROM Contatos WHERE id = ?', (contato_id_para_excluir,))
#Confirmando as alterações
conn.commit()
#Fechando a conexão
conn.close()





#IMPORTAÇÃO DA BIBLIOTECA PANDAS
import pandas as pd
url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

df_bancos = dfs[0]

print(df_bancos.shape)

print(df_bancos.dtypes)


df_bancos.head()

import pandas as pd

#Criando uma lista de valores
exemplo1 = [10, 20, 30, 40, 50]

#Criando uma serie aparrtir da lista
serie1 = pd.Series(data = exemplo1)

print(serie1)

#Criando um dicionário com pares chave-valor
Exemplo2 = {'A': 100, 'B': 200, 'C':300, 'D':400, 'E': 500 }
# Criando uma Series a partir do dicionário
series2 = pd.Series(data = Exemplo2)

print(series2)

import pandas as pd

dados = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
    'Idade': [25, 30,22, 35, 28]
}

#Criar uma serie a partir do dicionário
serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])
# Exibir a Série de idades
print("Série de idades:")
print(serie_idades)
#Calcular a média das idades
media_idades = serie_idades.mean()
print("\nMédia de Idades:", media_idades)


#MANIPULAÇÃO DE DADOS COM PANDAS BIBLIOTECA
import pandas as pd
df_selic = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')

print(df_selic.info())
print(df_selic)


#Verificando duplicidade de linhas (passo muito importante), ultilizando a função
#drop_duplicates()
df_selic.drop_duplicates(keep='last', inplace=True)
#mantém o ultimo registro (keep='last')
#através do parâmetro inplace=True, faz com que a transformação seja do DataFrame
#no nosso caso não existe linhas duplicadas.

print(df_selic)



#Adicionando colunas
from datetime  import date
from datetime import datetime as dt

data_extracao = dt.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Autor"

print(df_selic.info())
df_selic.head()


teste = df_selic['valor'] < 0.01
print(type(teste))

print(teste)


#CRIANDO UM DATAFRAME COM 5 LINHAS DE DADOS
import pandas as pd

data = {
    'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto E'],
    'quantidade de itens comprados': [3,1,4,3,2],
    'tipo de item': ['Eletrônico', 'Vestuário', 'Alimento', 'Eletrônicos', 'Alimento'],
    'receita total': [120, 80, 60, 120, 90]
}

df = pd.DataFrame(data)

print(df)


#Duplicando uma Linha
df.drop_duplicates(keep='last', inplace=True)
print(df)


#Calculando a coluna 'preço do item'
df['preco do item'] = df['receita total'] / df ['quantidade de itens comprados']
#Selecionando preco do item acima de 50 reais
itens_acima_de_50 = df[df['preco do item'] > 50]


print("Itens acima de 50 reais:")
print(itens_acima_de_50)

# Banco de dados gestão de funcionários

import sqlite3
#Passo 1 : Conectar ao banco de dados SQLITE (ou cria-lo se não existir)
conn = sqlite3.connect("funcionarios.db")


#Passo 2 : Criar a tabela de Funcionários

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
  id INTEGER PRIMARY KEY,
  nome TEXT,
  cargo TEXT,
  salario REAL
)
""")


#Passo 3 Inserir um novo funcionário na tabela
#novo_funcionario = (1, 'João', "Analista", 5000.00)
novo_funcionario =  (2, 'Lucas', "Backend", 8000.00)
#novo_funcionario =  (3, 'Amanda', "Marketing", 2500.00)
#novo_funcionario =  (4, 'Souza', "Frontend", 3000.00)
#novo_funcionario = (5, 'Roberta', "Cientista Dados", 10000.00)


cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?)", novo_funcionario)
conn.commit()


# Passo 4 : Consultar e exibir funcionários
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()
print("Funcionário(s) Cadastrado(s) com Sucesso em nossa base de dados!:")
for funcionario in funcionarios:
    print(funcionario)

    # Passo 5: Atualizar informações de um funcionário
    atualizacao = ("João Silva", 5500.00, 1)
    cursor.execute("UPDATE funcionarios SET nome = ?, salario = ? WHERE id = ?", atualizacao)
    conn.commit()

    # Passo 6: Deletar um funcionário da tabela
    id_funcionario_para_deletar = 1
    cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_funcionario_para_deletar,))
    conn.commit()



















