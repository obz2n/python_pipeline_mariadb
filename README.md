# python_pipeline_mariadb

Pipeline ETL utilizando Pandas, MariaDB e Airflow.

## Airflow local

Inicie os serviços com `docker compose up -d --build`. O Airflow ficará em
http://localhost:8081. As credenciais locais padrão são `airflow` e
`local-airflow-admin`; defina `AIRFLOW_ADMIN_USER` e `AIRFLOW_ADMIN_PASSWORD`
no `.env` antes de compartilhar ou expor o serviço.

Abra a DAG `google_ads_etl` e acione **Trigger DAG** para executar a extração,
transformação e carga. O processamento é manual, sem agendamento recorrente.
O MariaDB permanece disponível como fonte de dados em `db:3306` dentro da rede
do Compose.
