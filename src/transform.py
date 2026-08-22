import pandas as pd
from extract import extrair_dados_bronze

def ler_datraframe_csv(file_path: str, encoding: str = "utf-8") -> pd.DataFrame:
    """
    Lê um arquivo CSV e retorna um DataFrame.
    """
    try:
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica transformações nos dados do DataFrame.
    Exemplo: renomear colunas, filtrar linhas, etc.
    """
    # Exemplo de transformação: renomear colunas para minúsculas
    df.columns = [col.lower() for col in df.columns]

    # Exemplo de transformação: remover linhas com valores nulos
    df = df.dropna()

    return df
