import sys

from loguru import logger

from config import DATA_BRONZE_PATH
from extract import extrair_dados_bronze
from logger_config import setup_logger

# ============================================================================
# Pipeline Final
# ============================================================================
setup_logger()
logger = logger


@logger.catch
def main():
    """
    Função principal do pipeline.
    1. Extrai os dados CSV da pasta bronze.
    2. Registra um resumo da extração.
    """
    try:
        logger.info("Iniciando pipeline...")
        dataframes = extrair_dados_bronze()
        logger.info(f"Arquivos extraídos: {len(dataframes)}")
        for nome, df in dataframes.items():
            logger.info(f"- {nome}: {len(df)} linhas x {len(df.columns)} colunas")
    except Exception as e:
        logger.error(f"Erro no pipeline: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
