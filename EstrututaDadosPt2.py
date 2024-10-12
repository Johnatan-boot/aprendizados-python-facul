# add(), in e remove()

# Criando um conjunto vazio
meu_conjunto = set()

 #Adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
#Imprimindo o conjunto
print("Conjunto após adicionar elemento:", meu_conjunto)
#Verificando se um elemento eestá no conjunto
elemento = 20
if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto." )
else:
    print(f"{elemento} não está no conjunto." )
#Removendo um elemento do conjunto
meu_conjunto.remove(20)
#Imprimindo o conjunto atualizado
print("Conjunto após remover o elemento 20:", meu_conjunto)

#Exmeplo 1 Criação de um dicionário vázio, seguido de atribuição
#de chaves e valores
dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['idade'] = 25
#Exemplo  2 Criação de um dicionário com pares chave:valor
dici_2 = {'nome':  'Maria ', 'idade': 25}
# Exemplo 3  Criação de um dicionário com lista de tuplas representando chave e valor
dici_3 = dict([('nome', "Maria"), ('idade', 25)])
#Exemplo 4 Criação de um dicionário usando a função built-in zip
dici_4 = dict(zip(['nome','idade'],["Maria",25]))
#Teste se todas as construções resultam os osbjetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4) # Deve imprimir True
print(dici_1)



