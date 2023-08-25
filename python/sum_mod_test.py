import unittest

# em python todos arquivos sao modulos e as funcoes/classes ao acessiveis
# para isso uncionar precisa do arquivo __init__.py no diretorio
from sum_mod import sum

# classe de teste extende TestCase e termina com sufixo *Test
class SumTest(unittest.TestCase):
    # metodo de teste comeca com test_*
    def test_normal_flow(self):
        self.assertEqual(sum(3, 5), 8)

    def test_abnormal_flow(self):
        self.assertEqual(sum(0, 4), 1)


if __name__ == '__main__':
    unittest.main()
