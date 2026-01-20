import pytest  
from main import * 

def test_multiplicacao_inteiros():
    # função de teste reconhecida automaticamente pelo pytest por começar com "test_"
    # verifica se a multiplicação de dois inteiros retorna o resultado correto
    assert multiplicacao(3, 4) == 12  # assert valida se o valor retornado é o esperado

def test_operacao_inteiro_string():
    # testa um cenário onde ocorre uma operação inválida
    # pytest.raises garante que uma exceção específica seja lançada
    with pytest.raises(TypeError):
        multiplicacao(3, "4")  # o teste só passa se TypeError for lançado

def test_divisao_por_zero():
    # valida o comportamento da função ao tentar dividir por zero
    with pytest.raises(ZeroDivisionError):
        divisao(10, 0)  # espera explicitamente um erro de divisão por zero

def test_soma_floats():
    # testa a soma de números de ponto flutuante
    assert soma(1.5, 2.5) == 4.0  # compara o resultado retornado com o valor esperado
    
def test_subtracao_negativa():
    # Valida se a subtração resulta em um número negativo corretamente
    assert subtracao(5, 10) == -5.0