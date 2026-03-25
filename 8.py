def convert_datetime(dt_string):
    parts = dt_string.split(" ")
    if len(parts) != 2:
        print("Ошибка: неверный формат строки")
        return

    date_part, time_part = parts[0], parts[1]
    date_components = date_part.split("/")
    time_components = time_part.split(":")

    if len(date_components) != 3 or len(time_components) != 3:
        print("Ошибка: неверный формат")
        return

    mm, dd, yyyy = date_components
    hr, mn, sec = time_components

    if len(mm) != 2 or len(dd) != 2 or len(yyyy) != 4:
        print("Ошибка: неверный формат даты (ожидается MM/DD/YYYY)")
        return

    if len(hr) != 2 or len(mn) != 2 or len(sec) != 2:
        print("Ошибка: неверный формат времени (ожидается HR:MIN:SEC)")
        return

    if not (mm.isdigit() and dd.isdigit() and yyyy.isdigit() and
            hr.isdigit() and mn.isdigit() and sec.isdigit()):
        print("Ошибка: все компоненты должны быть числами")
        return

    month, day = int(mm), int(dd)
    hour, minute, second = int(hr), int(mn), int(sec)

    if not (1 <= month <= 12):
        print("Ошибка: месяц должен быть от 1 до 12")
        return
    if not (1 <= day <= 31):
        print("Ошибка: день должен быть от 1 до 31")
        return
    if not (0 <= hour <= 23):
        print("Ошибка: часы должны быть от 0 до 23")
        return
    if not (0 <= minute <= 59):
        print("Ошибка: минуты должны быть от 0 до 59")
        return
    if not (0 <= second <= 59):
        print("Ошибка: секунды должны быть от 0 до 59")
        return

    if hour == 0:
        hour_12 = 12
        period = "AM"
    elif 1 <= hour <= 11:
        hour_12 = hour
        period = "AM"
    elif hour == 12:
        hour_12 = 12
        period = "PM"
    else:
        hour_12 = hour - 12
        period = "PM"

    year_short = yyyy[-2:]

    print(f"{dd}.{mm}.{year_short} {hour_12:02d}:{mn}:{sec} {period}")


convert_datetime("04/28/2023 18:12:12")