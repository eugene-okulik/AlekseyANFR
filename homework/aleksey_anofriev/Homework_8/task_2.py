import sys
sys.set_int_max_str_digits(100000)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def from_generator(gen, n):
    for i in range(n):
        number = next(gen)
    return number

print(from_generator(fibonacci(), 5))
print(from_generator(fibonacci(), 200))
print(from_generator(fibonacci(), 1000))
print(from_generator(fibonacci(), 100000))
