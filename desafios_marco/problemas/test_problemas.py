import pangram

def test_func_deve_retornar_pangran():
    entrada = "welcome to geeksforgeeks"
    resultado_esperado = "adglvyz"
    assert pangram.verifica_pangrama(entrada) == resultado_esperado
