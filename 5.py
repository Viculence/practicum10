def phone_card():
    value = int(input("Введите стоимость карты "
                      "($5, $10, $25, $50, $100): "))

    if value == 5 or value == 10:
        return value
    elif value == 25:
        return value + 3
    elif value == 50:
        return value + 8
    elif value == 100:
        return value + 20
    else:
        print("Ошибка: недопустимое значение карты")
        return None


result = phone_card()
if result is not None:
    print(f"Денежный эквивалент карты: ${result}")