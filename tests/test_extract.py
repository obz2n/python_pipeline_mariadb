import unittest

from src.extract import extrair_dados_bronze


class ExtractTests(unittest.TestCase):
    def test_extrair_dados_bronze_ler_todos_os_csv(self):
        dataframes = extrair_dados_bronze()

        self.assertEqual(len(dataframes), 6)
        self.assertIn("TS_ALUNO_2014.csv", dataframes)
        self.assertIn("TS_ESCOLA_2014.csv", dataframes)
        self.assertIn("TS_ITEM_2014.csv", dataframes)
        self.assertIn("TS_ALUNO_2016.csv", dataframes)
        self.assertIn("TS_ESCOLA_2016.csv", dataframes)
        self.assertIn("TS_ITEM_2016.csv", dataframes)

        item_2014 = dataframes["TS_ITEM_2014.csv"]
        self.assertGreater(len(item_2014.columns), 1)
        self.assertGreater(len(item_2014), 0)


if __name__ == "__main__":
    unittest.main()
