a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'
text_index = a.index(':')
number = a[text_index + 2:]
print(int(number) + 10)

text_index = b.index(':')
number = b[text_index + 2:]
print(int(number) + 10)

text_index = c.index(':')
number = c[text_index + 2:]
print(int(number) + 10)
