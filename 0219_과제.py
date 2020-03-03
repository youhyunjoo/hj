for i in range(10):
    print((" " * i) + ("*" * (10 - i)))

for i in range(10):
    print((" " * (10 - i)) + ("*" * (1 + i)) + ("*" * i))

for i in range(1, 9):
    print((" " * (9 - i)) + (" *" * (1 + i)))
