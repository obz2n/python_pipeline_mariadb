import os
from typing import Literal
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import URL, Engine, create_engine
from loguru import logger

# Procurar .env na raiz do projeto (pai do diretório src/)
env_path = Path(__file__).parent.parent / ".env"

if not env_path.exists():
    logger.warning(f"Arquivo .env não encontrado em {env_path}")

# Carregar variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path=env_path)

logger.debug(f"Carregando variáveis de ambiente de: {env_path}")


def _obter_variavel_obrigatoria(nome: str) -> str:
    valor = os.getenv(nome)
    if not valor:
        raise RuntimeError(f"Variável de ambiente obrigatória ausente: {nome}")
    return valor


def conectar_mariadb() -> Engine:
    """
    Conecta ao banco de dados MariaDB usando variáveis de ambiente.
    Retorna uma engine SQLAlchemy.
    """
    user = _obter_variavel_obrigatoria("MARIADB_USER")
    password = _obter_variavel_obrigatoria("MARIADB_PASSWORD")
    host = os.getenv("MARIADB_HOST", "127.0.0.1")
    database = os.getenv("MARIADB_DATABASE") or _obter_variavel_obrigatoria("MARIADB_DB")
    port = int(os.getenv("MARIADB_PORT", "3306"))

    url = URL.create(
        "mysql+pymysql",
        username=user,
        password=password,
        host=host,
        port=port,
        database=database,
    )
    engine = create_engine(url, pool_pre_ping=True)
    logger.info("Engine MariaDB criada para {}:{}/{}", host, port, database)
    return engine

logger.debug(
    "Configuração MariaDB carregada: host={}, port={}, database={}, "
    "user=***, password=***, dialect=mysql+pymysql",
    os.getenv("MARIADB_HOST", "127.0.0.1"),
    os.getenv("MARIADB_PORT", "3306"),
    os.getenv("MARIADB_DATABASE") or os.getenv("MARIADB_DB", "***"),
)

def carregar_dados(
    df: pd.DataFrame,
    engine: Engine | None = None,
    tabela: str = "stg_google_ads",
    schema: str | None = None,
    if_exists: Literal["fail", "replace", "append", "delete_rows"] = "replace",
    chunksize: int = 1_000,
) -> int:
    """Carrega o DataFrame em uma tabela MariaDB e retorna as linhas gravadas."""
    if df.empty:
        logger.warning("Nenhum dado para carregar no MariaDB")
        return 0
    if chunksize <= 0:
        raise ValueError("chunksize deve ser maior que zero")

    managed_engine = engine is None
    engine = engine or conectar_mariadb()
    try:
        with engine.begin() as connection:
            df.to_sql(
                name=tabela,
                con=connection,
                schema=schema,
                if_exists=if_exists,
                index=False,
                chunksize=chunksize,
                method="multi",
            )
        logger.info("{} linhas carregadas em {}", len(df), tabela)
        return len(df)
    finally:
        if managed_engine:
            engine.dispose()