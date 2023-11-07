import psycopg2

conn = psycopg2.connect(
    database="mydb",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE Фільми (
    "Код фільму" SERIAL PRIMARY KEY,
    "назва фільму" VARCHAR(255),
    жанр VARCHAR(255),
    тривалість INT,
    рейтинг REAL
);
""")
cur.execute("""
CREATE TABLE Кінотеатри (
    "Код кінотеатру" SERIAL PRIMARY KEY,
    "назва кінотеатру" VARCHAR(255),
    "ціни на квітки" DECIMAL(10, 2),
    "кількість місць" INT,
    адреса VARCHAR(255),
    телефон VARCHAR(20)
);
""")
cur.execute("""
CREATE TABLE ТранслюванняФільмів (
    "Код транслювання" SERIAL PRIMARY KEY,
    "Код фільму" INT,
    "Код кінотеатру" INT,
    "Дата початку показів" DATE,
    "Термін показу" INT,
    FOREIGN KEY ("Код фільму") REFERENCES Фільми("Код фільму"),
    FOREIGN KEY ("Код кінотеатру") REFERENCES Кінотеатри("Код кінотеатру")
);
""")

conn.commit()
conn.close()
