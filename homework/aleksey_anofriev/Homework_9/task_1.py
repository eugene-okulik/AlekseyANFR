import datetime

my_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')

full_name = python_date.strftime('%B')
print(full_name)

format_date = python_date.strftime('%d.%m.%Y, %H:%M')
print(format_date)
