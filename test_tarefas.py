import tempfile
import unittest
from pathlib import Path

from tarefas import adicionar, carregar, concluir, salvar


class TestTarefas(unittest.TestCase):
    def test_adicionar_e_concluir(self):
        tarefas = []
        item = adicionar(tarefas, 'Estudar Git')
        self.assertEqual(item['id'], 1)
        self.assertFalse(item['concluida'])
        concluir(tarefas, 1)
        self.assertTrue(item['concluida'])

    def test_persistencia(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = Path(pasta) / 'dados.json'
            salvar(arquivo, [adicionar([], 'Teste')])
            self.assertEqual(carregar(arquivo)[0]['titulo'], 'Teste')

    def test_titulo_vazio(self):
        with self.assertRaises(ValueError):
            adicionar([], '  ')


if __name__ == '__main__':
    unittest.main()
