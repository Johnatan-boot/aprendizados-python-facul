#função map!
#aplica a uma função em toda sequencia
#map(fubção sequencia)
precos_em_dolares = [100,50,75,120]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(precos_em_reais)

#função filter
#filtra os elementos de uma sequência com base em uma função
#de teste (retorna true or false)
#filter(função_teste, sequencia)
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

# A ordem importa ...
#Exemplos de mais tuplas e utilizada
vogais = ('a','e','i','o','u')
print(f"Tipo do objeto vogais = {type(vogais)}")
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

#Tupla de convidados
convidados = ("Alice", "Bob","Carol", "David", "Eve")
#Lista de confirmações
confirmados = ["Bob", "David"]
#Indentificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not  in confirmados]

#Exibir os convidados que ainda não confirmaram
print("Convidados que ainda não confirmaram:")
for pessoa in  nao_confirmados:
    print(pessoa)
#Enviar lembretes aos não confirmados
print("\nEnviando lembretes para os convidados que ainda não confirmaram")

