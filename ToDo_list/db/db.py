import psycopg2 as psq

DB_NAME = "Todo"
DB_USER = "postgres"
DB_PASSWORD = "12345678"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psq.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
