# функция, примисающая число N
def fibonacci(n):
    if n <= 0:
        print("N должно быть положительным числом")
        return

    a, b = 1, 1

    for i in range(n):
        print(a)
        a, b = b, a + b


fibonacci(993)
