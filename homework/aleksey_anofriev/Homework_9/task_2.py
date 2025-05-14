temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]


def new_num(x):
    return x > 28


new_list = list(filter(new_num, temperatures))
print(new_list)

print(max(new_list))
print(min(new_list))
print(sum(new_list) / len(new_list))
