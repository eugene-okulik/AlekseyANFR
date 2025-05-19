PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {k: int(v[:-1]) for k, v in (item.split() for item in PRICE_LIST.split('\n'))}
print(price_dict)


def operation_selector(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')
    return wrapper


@operation_selector
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
 

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = calc(num1, num2)
print(f'Результат {result}')
