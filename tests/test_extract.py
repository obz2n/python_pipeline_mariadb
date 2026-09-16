import unittest

from src.config import DATA_BRONZE_PATH
from src.extract import extrair_dados_bronze


class ExtractTests(unittest.TestCase):
    def test_extrair_dados_bronze_ler_csv_configurado(self):
        dataframe = extrair_dados_bronze(DATA_BRONZE_PATH)

        self.assertIsNotNone(dataframe)
        self.assertGreater(len(dataframe.columns), 1)
        self.assertGreater(len(dataframe), 0)


if __name__ == "__main__":
    unittest.main()
