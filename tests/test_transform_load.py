import unittest
from unittest.mock import MagicMock, patch

import pandas as pd

from src.load import carregar_dados
from src.transform import transformar_dados


class TransformLoadTests(unittest.TestCase):
    def test_transformar_dados_normaliza_valores_e_preserva_entrada(self):
        original = pd.DataFrame(
            {
                "Cost": ["$10.50"],
                "Sale_Amount": ["$100"],
                "Location": [" bengluru "],
                "Device": ["mobile"],
                "Ad_Date": ["20-11-2024"],
            }
        )

        transformed = transformar_dados(original)

        self.assertEqual(transformed.loc[0, "Cost"], 10.50)
        self.assertEqual(transformed.loc[0, "Sale_Amount"], 100.0)
        self.assertEqual(transformed.loc[0, "Location"], "Bangalore")
        self.assertEqual(transformed.loc[0, "Device"], "Mobile")
        self.assertEqual(str(transformed.loc[0, "Ad_Date"].date()), "2024-11-20")
        self.assertEqual(original.loc[0, "Cost"], "$10.50")

    def test_carregar_dados_grava_em_transacao(self):
        engine = MagicMock()
        connection = engine.begin.return_value.__enter__.return_value
        dataframe = pd.DataFrame({"Ad_ID": ["A1000"], "Cost": [10.5]})

        with patch.object(dataframe, "to_sql") as to_sql:
            linhas = carregar_dados(dataframe, engine=engine)

        self.assertEqual(linhas, 1)
        engine.begin.assert_called_once_with()
        to_sql.assert_called_once_with(
            name="stg_google_ads",
            con=connection,
            schema=None,
            if_exists="replace",
            index=False,
            chunksize=1000,
            method="multi",
        )


if __name__ == "__main__":
    unittest.main()