import unittest

from src.extract import extrair_dados_bronze


class ExtractTests(unittest.TestCase):
    def test_extrair_dados_bronze_ler_todos_os_csv(self):
        dataframes = extrair_dados_bronze()

        self.assertEqual(set(dataframes.keys()), {"aluno", "escola", "item"})

        self.assertIn("aluno", dataframes)
        self.assertIn("escola", dataframes)
        self.assertIn("item", dataframes)

        self.assertGreater(len(dataframes["aluno"].columns), 1)
        self.assertGreater(len(dataframes["aluno"]), 0)
        self.assertGreater(len(dataframes["escola"].columns), 1)
        self.assertGreater(len(dataframes["escola"]), 0)
        self.assertGreater(len(dataframes["item"].columns), 1)
        self.assertGreater(len(dataframes["item"]), 0)


if __name__ == "__main__":
    unittest.main()
