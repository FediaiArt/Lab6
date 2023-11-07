import psycopg2

conn = psycopg2.connect(
    database="mydb",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def display_table(table_name):
    cur.execute(f"SELECT * FROM {table_name};")
    data = cur.fetchall()
    columns = [desc[0] for desc in cur.description]

    # Виведення назв стовпців з роздільниками
    header = " | ".join(columns)
    separator = "+".join(["-" * len(col) for col in columns])
    print(f"Дані з таблиці {table_name}:")
    print(header)
    print(separator)

    for row in data:
        # Виведення даних рядка з роздільниками
        row_data = " | ".join(map(str, row))
        print(row_data)
        print(separator)

# Виведення даних для всіх таблиць після заповнення
display_table("Фільми")
display_table("Кінотеатри")
display_table("ТранслюванняФільмів")

# Запит 1: Відобразити всі комедії та відсортувати фільми по рейтингу
print("\nЗапит 1: Відобразити всі комедії та відсортувати фільми по рейтингу")
cur.execute("""
SELECT "назва фільму", рейтинг
FROM Фільми
WHERE жанр = 'комедія'
ORDER BY рейтинг DESC;
""")
results = cur.fetchall()
for row in results:
    print(row[0], row[1])

# Запит 2: Порахувати останню дату показу фільму для кожного транслювання
print("\nЗапит 2: Порахувати останню дату показу фільму для кожного транслювання")
cur.execute("""
SELECT Фільми."назва фільму", Кінотеатри."назва кінотеатру", "Дата початку показів", "Термін показу",
    "Дата початку показів" + '1 day'::interval * "Термін показу" AS "Кінцева дата показу"
FROM "ТранслюванняФільмів"
JOIN Фільми ON "ТранслюванняФільмів"."Код фільму" = Фільми."Код фільму"
JOIN Кінотеатри ON "ТранслюванняФільмів"."Код кінотеатру" = Кінотеатри."Код кінотеатру";
""")
results = cur.fetchall()
for row in results:
    print(row[0], row[1], row[2], row[3], row[4])

# Запит 3: Порахувати суму максимального прибутку для кожного кінотеатру від одного показу
print("\nЗапит 3: Порахувати суму максимального прибутку для кожного кінотеатру від одного показу")
cur.execute("""
SELECT Кінотеатри."назва кінотеатру", MAX("ціни на квітки" * "кількість місць") AS "Максимальний прибуток"
FROM "ТранслюванняФільмів"
JOIN Кінотеатри ON "ТранслюванняФільмів"."Код кінотеатру" = Кінотеатри."Код кінотеатру"
GROUP BY Кінотеатри."назва кінотеатру";
""")
results = cur.fetchall()
for row in results:
    print(row[0], row[1])

# Запит 4: Відобразити всі фільми заданого жанру
genre = 'комедія'
print(f"\nЗапит 4: Відобразити всі фільми у жанрі '{genre}'")
cur.execute("""
SELECT "назва фільму"
FROM Фільми
WHERE жанр = %s;
""", (genre,))
results = cur.fetchall()
for row in results:
    print(row[0])

# Запит 5: Порахувати кількість фільмів кожного жанру (підсумковий запит)
print("\nЗапит 5: Порахувати кількість фільмів кожного жанру (підсумковий запит)")
cur.execute("""
SELECT жанр, COUNT(*) AS "Кількість фільмів"
FROM Фільми
GROUP BY жанр;
""")
results = cur.fetchall()
for row in results:
    print(row[0], row[1])

# Запит 6: Порахувати кількість мелодрам, комедій, бойовиків, які транслюються в кожному кінотеатрі (перехресний запит)
print("\nЗапит 6: Порахувати кількість мелодрам, комедій, бойовиків, які транслюються в кожному кінотеатрі (перехресний запит)")
cur.execute("""
SELECT Кінотеатри."назва кінотеатру", 
       SUM(CASE WHEN Фільми.жанр = 'мелодрама' THEN 1 ELSE 0 END) AS "Мелодрами",
       SUM(CASE WHEN Фільми.жанр = 'комедія' THEN 1 ELSE 0 END) AS "Комедії",
       SUM(CASE WHEN Фільми.жанр = 'бойовик' THEN 1 ELSE 0 END) AS "Бойовики"
FROM "ТранслюванняФільмів"
JOIN Кінотеатри ON "ТранслюванняФільмів"."Код кінотеатру" = Кінотеатри."Код кінотеатру"
JOIN Фільми ON "ТранслюванняФільмів"."Код фільму" = Фільми."Код фільму"
GROUP BY Кінотеатри."назва кінотеатру";
""")
results = cur.fetchall()
for row in results:
    print(row[0], f"Мелодрами: {row[1]}, Комедії: {row[2]}, Бойовики: {row[3]}")

conn.close()
