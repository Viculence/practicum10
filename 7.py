# функция принимает 3 параметра: числа a и b, и верхнюю границу n
def general_multiples(a, b, n):
    for i in range(1, n + 1):
        if i % a == 0 and i % b == 0:
            print(i)


general_multiples(3, 5, 105)
