import linear_search


def test_func_deve_retornar_posic_valor_pesq():
    entrada =  [2,3,4,10,40]
    valor_pesq = 10
    resultado_esperado = 3
    assert linear_search.linear_search(entrada,valor_pesq) == resultado_esperado
    