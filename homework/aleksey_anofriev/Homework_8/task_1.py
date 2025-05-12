import random
salary = int(input('Введите число: '))
bonus = random.choice([True, False])

if bonus:
    bonus_amount = random.randint(1, 500)
    result = salary + bonus_amount
else:
    result = salary

print(f"{salary}, {bonus} - '${result}'")
