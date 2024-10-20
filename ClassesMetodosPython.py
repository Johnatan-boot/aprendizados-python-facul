#DEFINE UMA CLASSE CHAMADA PESSOA
class Pessoa:
    #O Metodo __init__ é um constructor, chamado quando
    #um objeto da classe é criado.
    #Ele incializa os atributos da classe.
    def __init__(self, nome, idade, genero): # Changed _init_ to __init__
        #SELF É UMA CONVENÇÃO EM PYTHON QUE SE REFERE
        #A PROPRIA INSTANCIA DA CLASSE.
        #PARÂMETROS NOME, IDADE E GENÊRO SÃO PASSADOS DURANTE
        #A CRIAÇÃO DO OBJETO.
        #ELES SÃO USADOS PARA INICIALIZAR OS ATRIBUTOS DA INSTÂNCIA.
        self.nome = nome # Atribui o valor de nome ao atributo nome da instancia
        self.idade = idade = idade #Atribui o Valor de idade ao atributo idade na instância
        self.genero = genero #Atribui o valor de genero ao atributo genero da instancia.
    # O metodo cumprimentar retorna uma saudação com o nome da pessoa.
    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}."
    #O metodo aniversario aumenta a idade da pessoa em 1.
    def aniversario(self):
        self.idade += 1

#Cria um instância da classe "PESSOA" com os valores "JOAO", 30 E "MASCULINO" PARA NOME, IDADE E GENERO,
#RESPECTIVAMENTE.
pessoa1 =  Pessoa("João", 30, "Masculino") # Moved instance creation outside the class
#chama o método "Cumprimentar" na instância pessoa1 e imprime sua idade.
print(pessoa1.cumprimentar()) #Saida: "Olá meu nome é João."
#Acessa o atributo da idade da instância pessoa1 e imprime
#sua idade.
print(f"idade: {pessoa1.idade}")# Saida: "Idade:30"
#chama o metodo "aniversario" na instância pessoa1 e imprime sua idade.
pessoa1.aniversario()
#Acessa o atributo idade atualizado da instância pessoa1 a nova idade
print(f"Nova idade: {pessoa1.idade}")#saida: "Nova idade: 31"


class Animal:
    def __init__(self, nome): # Corrected the constructor to __init__
        self.nome = nome

    def fazer_barulho(self):
        pass

class Cachorro(Animal):
    def fazer_barulho(self):
        return "Latir"

class Gato(Animal):
    def fazer_barulho(self):
        return "Miar"

rex =     Cachorro("Rex")
whiskers = Gato("Whiskers")

print(f"{rex.nome} faz: {rex.fazer_barulho()}")
print(f"{whiskers.nome} faz: {whiskers.fazer_barulho()}")


class Veiculo:
    def __init__(self, marca, modelo, ano):  # Changed _init_ to __init__
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} Km/h"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):  # Changed _init_ to __init__
        super().__init__(marca, modelo, ano)  # Changed _init_ to __init__
        self.potencia = potencia

    def acelerar(self, incremento):
        # Carros podem acelerar mais rápido
        self.velocidade += incremento + self.potencia


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):  # Changed _init_ to __init__
        super().__init__(marca, modelo, ano)  # Changed _init_ to __init__
        self.tipo = tipo

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano:{self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} Km/h "  # Changed self.Velocidade to self.velocidade


# CRIANDO OBJETOS
carro1 = Carro("Toyota", "Corolla", 2022, 150)
bicicleta1 = Bicicleta("Trek", "Moutain Bike", 2021, "MTB")

# Acelerando e verificando o status
carro1.acelerar(50)
bicicleta1.acelerar(20)

# Exibindo o status dos Veículos
print("Status do carro:")
print(carro1.status())

print("\nStatus da Bicicleta:")
print(bicicleta1.status())



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