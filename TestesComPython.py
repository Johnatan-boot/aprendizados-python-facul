from unittest import TestCase

from ManipulaDadosPandas import teste
from aprendizadosIniciaisPython import media


def divide(x, y):
    #AS ASSERTIONS = ASSERT SÃO EXPRESSÕES ULTILIZADAS PARA VERIFICAR
    #CONDIÇÕES DE VERDADE DURANTE A EXECUÇÃO DO CÓDIGO. ELAS SÃO FUNDAMENTAIS
    #PARA A DETECÇÃO  PRECOCE DE ERROS, GARANTINDO QUE AS SUPOSIÇÕES SOBRE O
    # COMPORTAAMENTO DO PROGRAMA SEJAM ATENDIDAS
    assert y != 0, "Divisão por zero!"
    return  x / y

result = divide(6,0)
print(result)

def calcular_media(notas):
    assert  len(notas) > 0, "A lista de notas não pode estar vazia"
    soma = sum(notas)
    media = soma / len(notas)
    return  media

#Exemplo 1: Lista de Notas vazia
notas_vazias = []
media = Calcular_media(notas_vazias) # Isso lançará uma AssertionError

#Exemplo 2: Lista de notas válida
notas_validas = [8, 7, 9, 6, 8]
media = calcular_media(notas_validas) # Isso funcionará corretamente
print(media)


#DOCTESTS
import  doctest
def square(x):
    """
    Retorna o quadrado de um número.

    Exemplos:
    >>> square(3)
    9
    >>> square(-2)
    4
    >>> square(0)
    0
    """
    return x * x
doctest.testmod()

# A função square é acompanhada por uma string de documentação que inclui
#exemplos de uso. Esses exemplos estão formatados de maneira especial, usando
# o prompt >>>, que indica um bloco de código Python.

#No caso do exemplo , doctest.testmod() executará a função square(3),
#Verificará se o resultado é igual a 9, executará squate(-2) e verificará se o
#resultado  é igual a 4, assim por diante.
#Se todos os testes passarem, doctest não produzirá nenhuma saída.
#Se houver uma discrepância a saída real e a esperada, doctest imprimirá uma
#mensagem onde ocorreu o problema.
#A principal vantagem do doctest é que ele permite que voçê mantenha exemplos
# na documentação e ao mesmo tempo use esses exemplos como testes automatizados
#Isso ajuda a garantir que a documentação esteja sempre em Sincronia com o codigo
# real.



#UNITEST
import unitest

def add( a, b):
    return  a + b

class TestAddition(unittest, TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2,3), 5)
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2,-3), -5)

if _name_ == '_main_':
    import unittest

    if __name__ == '__main__':
        if __name__ == '__main__':
            unitest.main(argv=['first-arg-is-ignored'], exit = false)
            print("Os testes foram executados com sucesso!")


# A função add simplesmente soma dois números, cria uma classe que herda de
#unittest.TestCase(). isso indica que essa classe contém testes unitários.
#Dentro da classe de teste, voçê define métodos de teste.
#Cada metodo de teste deve começar com a palavra-chave test.
#Dentro desses métodos, voçê usa Assertivas (como self.assertEqual)
# A condição if __name__ == '__main__': garante que a suíte de testes seja
# executada somente se o script for executado diretamente.
# não se for importado como um módulo em outro script. o unittest.main()
#Executa todos os testes definidos na classe TestAddition.


#ASSERT
def sum_numbers(numbers):
    assert  sum([1,2,3,4]) == 10
    assert  sum([-1,0,1]) == 0
    assert  sum([]) == 0
    return sum(numbers)
teste = sum_numbers([1,2,3,5])
print(teste)


#doctest
def sum_numbers(numbers):
    """
    Soma os números em uma lista.

    Exemplos:
    >>> sum_numbers([1,2,3,4])
    10
    >>> sum_numbers([-1,0,1])
    0
    >>> sum_numbers([])
    0
   """

    return sum(numbers)
if _name_ == "_main_":
    import  doctest
    doctest.testmod()


#UNITTEST
import unittest
def sum_numbers(numbers):
    return  sun(numbers)

class TestNumbers(unittest.TestCase):
    def test_sum_numbers_positive(self):
        self.assertEqual(sum_numbers([1,2,3,4]),10)

    def test_sum_numbers_mixed(self):
        self.assertEqaul(sum_numbers([-1,0,1]),0)
    def test_sum_numbers_empty(self):
        self.assertEqual(sum_numbers([]),0)

if _name_ == '_main_':
    unittest.main(argv =['first-arg-is-ignored'], exit= False)





