a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат: 2'

def sum(calc):
    num = int(calc.split()[-1])
    result = num + 10
    print(result)

sum(a)
sum(b)
sum(c)
sum(d)
