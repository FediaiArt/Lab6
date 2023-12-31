import psycopg2

conn = psycopg2.connect(
    database="mydb",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Додавання даних до таблиці Фільми
cur.execute("""
INSERT INTO Фільми ("Код фільму", "назва фільму", жанр, тривалість, рейтинг)
VALUES
  (1, 'Фільм 1', 'комедія', 120, 4.5),
  (2, 'Фільм 2', 'мелодрама', 150, 4.2),
  (3, 'Фільм 3', 'бойовик', 130, 4.8),
  (4, 'Фільм 4', 'комедія', 110, 4.0),
  (5, 'Фільм 5', 'бойовик', 140, 4.7),
  (6, 'Фільм 6', 'драма', 125, 4.1),
  (7, 'Фільм 7', 'комедія', 118, 4.3),
  (8, 'Фільм 8', 'драма', 155, 4.4),
  (9, 'Фільм 9', 'бойовик', 128, 4.6),
  (10, 'Фільм 10', 'мелодрама', 135, 4.9),
  (11, 'Фільм 11', 'комедія', 122, 4.7);
""")

# Додавання даних до таблиці Кінотеатри
cur.execute("""
INSERT INTO Кінотеатри ("Код кінотеатру", "назва кінотеатру", "ціни на квітки", "кількість місць", адреса, телефон)
VALUES
  (1, 'Кінотеатр 1', 10.0, 200, 'Адреса 1', '+380123456789'),
  (2, 'Кінотеатр 2', 12.0, 150, 'Адреса 2', '+380987654321'),
  (3, 'Кінотеатр 3', 9.0, 180, 'Адреса 3', '+380555555555'),
  (4, 'Кінотеатр 4', 11.5, 220, 'Адреса 4', '+380111111111'),
  (5, 'Кінотеатр 5', 13.0, 170, 'Адреса 5', '+380999999999');
""")

# Додавання даних до таблиці ТранслюванняФільмів
cur.execute("""
INSERT INTO ТранслюванняФільмів ("Код транслювання", "Код фільму", "Код кінотеатру", "Дата початку показів", "Термін показу")
VALUES
  (1, 1, 1, '2023-11-01', 7),
  (2, 2, 1, '2023-11-05', 5),
  (3, 3, 2, '2023-11-02', 6),
  (4, 4, 3, '2023-11-03', 5),
  (5, 5, 3, '2023-11-06', 4),
  (6, 6, 1, '2023-11-04', 5),
  (7, 7, 2, '2023-11-07', 6),
  (8, 8, 1, '2023-11-05', 4),
  (9, 9, 3, '2023-11-01', 7),
  (10, 10, 2, '2023-11-08', 6),
  (11, 11, 3, '2023-11-10', 5),
  (12, 5, 1, '2023-11-09', 4),
  (13, 7, 2, '2023-11-12', 7),
  (14, 2, 1, '2023-11-11', 6),
  (15, 10, 3, '2023-11-13', 4);
""")

conn.commit()
conn.close()
