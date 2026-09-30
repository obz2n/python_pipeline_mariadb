from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def executar_pipeline() -> int:
    from src.config import DATA_BRONZE_PATH, SCHEMA_NAME_BRONZE, TABLE_NAME_BRONZE
    from src.extract import extrair_dados_bronze
    from src.load import carregar_dados
    from src.transform import transformar_dados

    dados = extrair_dados_bronze(DATA_BRONZE_PATH)
    if dados is None or dados.empty:
        raise ValueError(f"Nenhum dado encontrado em {DATA_BRONZE_PATH}")

    dados_transformados = transformar_dados(dados)
    linhas_carregadas = carregar_dados(
        dados_transformados,
        tabela=TABLE_NAME_BRONZE,
        schema=SCHEMA_NAME_BRONZE,
    )
    return linhas_carregadas


with DAG(
    dag_id="google_ads_etl",
    description="Extrai, transforma e carrega o CSV de campanhas no MariaDB",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    max_active_runs=1,
    default_args={
        "owner": "data-engineering",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    tags=["google-ads", "mariadb", "etl"],
) as dag:
    executar_etl = PythonOperator(
        task_id="extrair_transformar_carregar",
        python_callable=executar_pipeline,
    )