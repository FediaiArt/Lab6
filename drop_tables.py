import psycopg2

conn = psycopg2.connect(
    database="mydb",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Видалення таблиць
cur.execute("DROP TABLE IF EXISTS ТранслюванняФільмів;")
cur.execute("DROP TABLE IF EXISTS Фільми;")
cur.execute("DROP TABLE IF EXISTS Кінотеатри;")

conn.commit()
conn.close()
