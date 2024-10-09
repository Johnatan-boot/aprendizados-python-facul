#Variaveis e tipos de dados
x = 10 #inteiro
nome0 = 'aluno' # string
nota = 8.75 # float
fez_inscricao = True # Booleano
matéria1 = 'Português'
matéria2 = 'Matemática'
matéria3 = 'Ciências'


#Printando informações na tela com a função print
print(type(x)) # função type mostra o tipo do que estou mostrando
print(type(nome0))
print(type(nota))
print(type(fez_inscricao))


nome0 = input("Digite um Nome: ")
print(nome0)

#formatadores de caracteres
print("Olá, %s, bem-vindo à disciplina de programação. Parabéns pelo seu primeiro hello world" % (nome0))
#Olá, Estudante Querido, bem-vindo à disciplina de programação. Parabéns pelo seu primeiro hello world
#F-string



Nota_1 = int(input("Digite a primeira nota:"))

Nota_2 = int(input("Digite a segunda nota:"))

Nota_3 = int(input("Digite a tereceira nota:"))

Nota_4 = int(input("Digite a  quarta nota:"))

#observe que utilizamos a função int(), pois, sem ela, o Python entenderia que as notas seriam String



#condição para a aprovação do aluno.
media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4

if media >= 6:
   situacao = "Aprovado"

else:
   situacao = "Reprovado"



#dadas as notas, mostramos a média final e a situação do aluno.

print("\n =========================="
"\nA média das notas é: %s  "  % (media))

print("A situação do Aluno(a) na matéria de: %s" % (matéria1))
print("Status %s" % (situacao))

#Estrutura decisão  Condicionais
idade = 70

if idade < 18:
  print("Menor de idade")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")

    # Estrutura de repetição
    numeros = [1, 2, 3, 4, 5]
    numero = int(input("Digite um número (ou 0 para sair):"))
    # for
    for num in numeros:
        print(num)

    # while
    while numero != 0:
        if numero % 2 == 0:
            print("O número é par.")
        else:
            print("O número é impar")
        numero = int(input("Digite um número (ou 0 para sair):"))

        # For com range o range(5) ele chega de 0 a 4 é tipo n-1
        for x in range(5):
            print(x)

            for y in range(2, 7):  # o número 7 não entra no Lopping
                print(y)


# for com range o 11 não entra no looping
for z in range(1,11,2):
  print(z)

# Pare ou prossiga com range

for numero in range(1,11):
  if numero % 2 == 0:
    print("O primeiro número para é :", numero)
    break

    for numero in range(1, 11):
        if numero == 5:
            continue
        print(numero)


#lista de Filmes com break

#Bem vindo á Maquina de vendas Automática de ingressos de Cinema!

#Solicita a idade do cliente

idade = int(input("Por favor, digite sua idade:"))



#Verifica a idade para sugestão de filmes
if idade < 12:
    print("Recomendamos o filme infantil Meu Malvado Favorito.")
elif 12 <= idade < 18:
    print("Recomendamos o filme adolescente Liga da Justiça.")
else:
        print("Recomendamos o filme adulto Deadpool e Wolverine")


        #Verifica a disponibilidade de ingressos
        quantidade_ingressos = 0 #Suponha que haja 10 ingressos disponiveis
        quantidade_ingressos = int(input("Por favor, diga a quantidade de ingressos a ser comprado:"))

        if quantidade_ingressos > 0:
           print("Ingressos estão disponiveis. Divirta-se no cinema!")
        else:
           print("Desculpe, todos os ingressos estão esgotados para hoje.")

#usamos o for para uma decisão direta do 1 ate o 5
'''numeros = [1,2,3,4,5]
for num in numeros:
    print(num)


#usamos o while para uma decisão que não sabemos até onde vai...
    numero = int(input("Digite um número (ou 0 para sair.):"))
while numero != 0:
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é impar.")
    numero = int(input("Digite um número (ou 0 para sair.):"))


for x in range(5): #Lembre-se que o range começa do 0 tipo vai até 5-1 4
    print(x)

    for y in range(2,7): # range com limite superior e inferior
        print(y)

        for z in range(1,11,2): #observe que o range pula de 2 em 2 menos
# os numeros selecionados
            print(z)


   #break
for numero in range(10,11):
       if numero % 2 == 0:
           print("O primeiro número par encontrado é:",numero)
           break

    #O primeiro número par encontrado é 10

for numero in range(1,11):
        if numero == 5 :
            print(numero)'''


#Lista de filmes para classificação
filmes = ["Meu malvado favorito","Liga da Justiça","Deadpool e Wolverine","Alien Romulus","The Avengers: Ultimate"]

print(filmes)

#Mensagem de boas-vindas
print("Bem-vindo á classificação de filmes!")
print("Voçê tem cinco Filmes para classificar.")
print("Digite '0'a qualquer momento para parar.\n ")

#Loop para iterar sobre cada filme na lista
for filme in filmes:
    #Solicita a classificação ao usuário
    classificacao = input(f"Como voçê classificaria '{filme}' de 1 a 5 ? (ou 0 para parar):")


#Verifica se o usuario deseja parar
    if classificacao == '0':
       print("Que pena que voçê não irá mais classificar mais os filmes.")
       break
#encerra o Loop principal

   #converte a classificação para um número inteiro
    classificacao = int(classificacao)

   #Verifica se classificação está dentro do intervalo válido
    if classificacao < 1  or classificacao > 5:
        print("Por favor, digite uma classificação válida de 1 a 5.")
    else:
        #Exibe a classificacao e passa para o proximo filme
        print(f"Você classificou '{filme}' com {classificacao} estrelas.\n")

    #Mensagem de agradecimento ao finalizar

        print("Obrigado por classificar os filmes!")

#Funções em python
# 3 tipos Criadas em Python, Built-in, criada pelos úsuarios,


#Python
#Cria uma lista de números
numeros = [1, 2, 3, 4, 5]#,7,8,9,10,11,'a', true]
#usa a função len para calcular o tamanho de uma lista
cumprimento = len(numeros)
#imprime o cumprimento da lista
print("O cumprimento da Lista é: ", cumprimento)




#Built-in




#Criadas pelo usuário ou funções anonimas conhecidas como funções lambda
#Definindo uma função chamada "soma"
def soma(a, b): #def = definição
    resultado = a + b # a soma
    return resultado # e o retorno

resultado_soma = soma(5,3)

#imprimindo o resultado
print("A soma de 5 e 3 é:", resultado_soma)

# Definindo uma função chamada "e_par"
def e_par(numero):
  #operador modulo %
   if numero % 2 == 0:
       return True
   else:
       return False


numero = 5455424515464184542484845221840
if e_par(numero):
    print(f"{numero} é um número par.")
else:
    print(f"{numero} não é número par.")

    # Criadas pelo usuário ou funções anonimas conhecidas como funções lambda

    soma = lambda a, b: a + b
    resultado = soma(3, 4)
    print(resultado)

    # FAZENDO UM UPGRADE NO SISTEMA DE CALCULO DE MEDIA NOTAS
    notas = [7.5, 8.0, 6.5, 9.0, 7.0]  # Criando uma lista de notas


    # Função regular para calcular a média
    def calcular_media(notas):  # definindo a função calcular medias com parametros notas
        total = sum(notas)  # criando uma variavel para armazenar soma de notas
        media = total / len(notas)  # conterá media o total dividido pelo tamano de notas
        return media  # vai retornar a média dos alunos


    # Função lambda para arredondar a média para duas casas decimais
    arredondar_media = lambda media: round(media, 2)

    # Calcular a média
    media = calcular_media(notas)  # a variavel media conterá o calculo de medias trazendo as notas dos alunos
    media_arredondada = arredondar_media(media)

    # Verificar se os estudantes foram aprovados
    situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

    # Resultados
    print("Notas dos estudantes:", notas)
    print("Média das notas", media_arredondada)
    print("Situação do estudante", situacao)

    # Calculadora de porcentagem desconto
    # Solicita ao usuário que insita o valor do produto e o percentual de desconto
    valor_produto = float(input("Digite o valor do produto R$: "))
    percentual_desonto = float(input("Digite o percentual de desconto:"))

    # Verifica se o percentual de desconto está dentro dos limites aceitaveis(0-100%)
    if percentual_desonto < 0 or percentual_desonto > 100:
        print("Erro: o percentural de desconto deve estar entre 0% e 100%.")
    else:
        # Calcula o valor do desconto
        desconto = valor_produto * (percentual_desonto / 100)
        valor_final = valor_produto - desconto

        # Exibe o valor final da compra
        print(f"Valor com desconto: R$ {valor_final: .2f}")

        # Estrutura de dados com python
        # Listas e tuplas com python

        texto = "Explorando a diversidade de linguagens de programação com Python."

        print(f"Tamanho do texto ={len(texto)}")
        print(f"Python in texto ={'Python' in texto}")
        print(f"Quantidade de e no texto = {texto.count('e')}")
        print(f"As 5 primeiras letras são {texto[:5]}")

        # Sequencias mutaveis python
        cores = ['Vermelho', 'Azul', 'Verde', 'Amarelo', 'Roxo']
        for cor in cores:
            print(f'Posição = {cores.index(cor)}, cor= {cor}')



     #LIST COMPRESSION COM A FUNÇÃO LOWER
    linguagens = ["Python","Java","Javascript", "C","C#", "C++", "Swift", "Go", "Kotlin"]
    print("Antes da listcomp = ", linguagens)
    linguagens = [item.lower() for item in linguagens]
    print("\nDepois da listcomp = ", linguagens)







