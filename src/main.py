import sys
from loguru import logger
from config import DATA_BRONZE_PATH
from extract import detectar_encoding
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
    1. Extrai os dados do arquivo CSV.
    """
    try:
        logger.info("Iniciando pipeline...")
        encoding = detectar_encoding(DATA_BRONZE_PATH)
        logger.info(f"Encoding detectado: {encoding}")
    except Exception as e:
        logger.error(f"Erro no pipeline: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()