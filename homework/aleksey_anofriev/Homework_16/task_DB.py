import mysql.connector as mysql
import os
import dotenv
import csv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
csv_file = os.path.join(
    project_root,
    'homework', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv'
)

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print("Заголовки колонок CSV:", reader.fieldnames)
    csv_rows = list(reader)

missing_rows = []

query = """
SELECT
    s.id AS student_id
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sub ON l.subject_id = sub.id
JOIN books b ON b.taken_by_student_id = s.id
WHERE
    s.name = %s AND
    s.second_name = %s AND
    g.title = %s AND
    b.title = %s AND
    sub.title = %s AND
    l.title = %s AND
    m.value = %s
LIMIT 1
"""

for row in csv_rows:
    values = (
        row['name'],
        row['second_name'],
        row['group_title'],
        row['book_title'],
        row['subject_title'],
        row['lesson_title'],
        row['mark_value']
    )
    cursor.execute(query, values)
    result = cursor.fetchone()
    if not result:
        missing_rows.append(row)

cursor.close()
db.close()

if missing_rows:
    print("Строки, которых нет в базе данных:")
    for row in missing_rows:
        print(row)
else:
    print("Все данные из файла присутствуют в базе данных.")
