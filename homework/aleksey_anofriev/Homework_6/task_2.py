for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FuzzBuzz")
        else:
            print("Fuzz")
    else:
        if i % 5 == 0:
            print("Buzz")
        else:
            print(i)
