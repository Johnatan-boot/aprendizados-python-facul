from flask import Flask

# Corrected the variable name to __name__
app = Flask(__name__)

#Rota para pagina inicial
@app.route('/')
def hello():
    return 'Bem vindo ao backend simples com Flask!'

#Executa a aplicação no host e na porta especifica
# Corrected the variable name to __main__
if __name__ == '__main__' :
  app.run(host= 'localhost', port = 5000)