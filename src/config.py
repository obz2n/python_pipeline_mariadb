from pathlib import Path

# ========================
# Diretórios
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_BRONZE_PATH = BASE_DIR / "data"
LOG_PATH = BASE_DIR / "logs"

# ========================
# Banco de dados
# ========================
SCHEMA_NAME_BRONZE = "staging"
TABLE_NAME_BRONZE = "stg_"
PATTERN_CSV = "*.csv"
PATTERN_TXT = "*.txt"
PATTERN_PARQUET = "*.parquet"

ENCODINGS = [
    "utf-8",
    "utf-8-sig",  # UTF-8 com BOM — comum em exports do Excel
    "cp1252",  # Windows-1252 — padrão em sistemas Windows BR
    "iso-8859-1",  # Latin-1 — arquivos legados
    "cp860",  # MS-DOS Portuguese
    "latin-1",
    "utf-16",
    "MacTurkish",
]
