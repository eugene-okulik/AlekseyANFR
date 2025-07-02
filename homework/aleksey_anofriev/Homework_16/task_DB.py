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

csv_file = r'C:\Users\Aleksey Anofriev\Desktop\project_Okulik\AlekseyANFR\homework\eugene_okulik\Lesson_16\data.csv'

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print("Заголовки колонок CSV:", reader.fieldnames)
    csv_rows = list(reader)

missing_rows = []

for row in csv_rows:
    query = (
        "SELECT * FROM students WHERE Name = %s AND last = %s AND city = %s"
    )
    values = (row['Name'], row['last'], row['city'])
    cursor.execute(query, values)
    result = cursor.fetchone()
    if not result:
        missing_rows.append(row)

cursor.close()
db.close()

if missing_rows:
    print("Строки, которых нет в базе:")
    for row in missing_rows:
        print(row)
else:
    print("Все данные из файла присутствуют в базе данных.")
