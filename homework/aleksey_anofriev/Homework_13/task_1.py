import os
import datetime

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt')
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_okulik_file = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(eugene_okulik_file, encoding='utf-8') as eugene_file:
        for line in eugene_file:
            yield line.strip()


def process_line(line, number):
    if line.startswith(f'{number}. '):
        line = line[len(f'{number}. '):]
    

    parts = line.split(' - ', 1)
    date_str = parts[0]
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

    if number == 1:
        new_date = date + datetime.timedelta(days=7)
        print(f'{number}. {new_date} - дата на неделю позже')
    elif number == 2:
        day_of_week = date.strftime('%A')
        print(f"{number}. {date} - это был день недели: {day_of_week}")
    elif number == 3:
        now = datetime.datetime.now()
        days_ago = (now - date).days
        print(f"{number}. {date} - это было {days_ago} дней назад")


line_number = 1
for data_line in read_file():
    process_line(data_line, line_number)
    line_number += 1
