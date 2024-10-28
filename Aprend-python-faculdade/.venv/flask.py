from flask import Flask

#criacao da aplicação flask
app= Flask(__name__)

#Rota para pagina inicial
@app.route('/')
def hello():
    return 'Bem-vindo ao back-end simples com Flask!'

#Executa a aplicação no host e na porta especificados
if __name__ == '__main__':
    app.run(host= 'localhost', port=5000)
    