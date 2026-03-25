def filter_numbers(a, b):
    if a > b:
        a, b = b, a

    plenty = {"1", "3", "4", "8", "9"}

    for i in range(a, b + 1):
        if set(str(i)) <= plenty:
            print(i)


filter_numbers(1, 100)