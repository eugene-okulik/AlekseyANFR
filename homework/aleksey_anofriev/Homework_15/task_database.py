import mysql.connector as mysql

# Подключение к базе данных
db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute(
    "INSERT INTO students (name, second_name) VALUES (%s, %s)",
    ('Alolik', 'Alolov')
)
student_id = cursor.lastrowid
print(f"Создан студент с id={student_id}")

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
    ('ALEX testers', '2025-05-25', '2025-07-25')
)
group_id = cursor.lastrowid
print(f"Создана группа с id={group_id}")

cursor.execute(
    "UPDATE students SET group_id = %s WHERE id = %s",
    (group_id, student_id)
)
print(f"Обновлён студент id={student_id} с group_id={group_id}")

book_titles = ['Книга 1', 'Книга 2', 'Книга 3']

books_data = []
for title in book_titles:
    books_data.append((title, student_id))

cursor.executemany(
    "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
    books_data
)
print(f"Созданы книги: {book_titles}")


subjects = ['Математика', 'История', 'Физика']
subject_ids = []
for subj in subjects:
    cursor.execute(
        "INSERT INTO subjets (title) VALUES (%s)",
        (subj,)
    )
    subject_ids.append(cursor.lastrowid)
print(f"Созданы предметы с id: {subject_ids}")

lesson_ids = []
for subj_id in subject_ids:
    for i in range(1, 3):
        lesson_title = f"Lesson {i} по предмету {subj_id}"
        cursor.execute(
            "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
            (lesson_title, subj_id)
        )
        lesson_ids.append(cursor.lastrowid)
print(f"Созданы занятия с id: {lesson_ids}")

marks_data = []
for lesson_id in lesson_ids:
    marks_data.append((5, lesson_id, student_id))

cursor.executemany(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
    marks_data
)
print(f"Поставлены оценки студенту id={student_id} для всех занятий")

db.commit()

cursor.execute("""
        SELECT m.value, l.title AS lesson_title, sub.title AS subject_title
        FROM marks m
        JOIN lessons l ON m.lesson_id = l.id
        JOIN subjets sub ON l.subject_id = sub.id
        WHERE m.student_id = %s
    """, (student_id,))
marks = cursor.fetchall()
print("\nОценки студента:")
for mark in marks:
    print(f"{mark['subject_title']} - {mark['lesson_title']}: {mark['value']}")

cursor.execute("""
        SELECT title FROM books WHERE taken_by_student_id = %s
    """, (student_id,))
books = cursor.fetchall()
print("\nКниги студента:")
for book in books:
    print(book['title'])

cursor.execute("""
        SELECT
            s.id AS student_id, s.name, s.second_name,
            g.title AS group_title,
            b.title AS book_title,
            m.value AS mark_value,
            l.title AS lesson_title,
            sub.title AS subject_title
        FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON b.taken_by_student_id = s.id
        LEFT JOIN marks m ON m.student_id = s.id
        LEFT JOIN lessons l ON m.lesson_id = l.id
        LEFT JOIN subjets sub ON l.subject_id = sub.id
        WHERE s.id = %s
    """, (student_id,))
full_info = cursor.fetchall()

print("\nПолная информация о студенте:")
for row in full_info:
    print(f"Студент: {row['name']} {row['second_name']}, "
          f"Группа: {row['group_title']}, "
          f"Книга: {row['book_title']}, "
          f"Оценка: {row['mark_value']}, "
          f"Занятие: {row['lesson_title']}, "
          f"Предмет: {row['subject_title']}")

cursor.close()
db.close()
