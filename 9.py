# Вычисляет количество секунд от начала года до указанной даты/времени
# Формат входной строки: "DD/MM/YYYY HR:MIN:SEC"
# Возвращает: целое число секунд
def seconds_since_year_start(dt_string):
    parts = dt_string.split(" ")
    date_part, time_part = parts[0], parts[1]

    mm, dd, yyyy = date_part.split("/")
    hr, mn, sec = time_part.split(":")

    month, day, year = int(mm), int(dd), int(yyyy)
    hour, minute, second = int(hr), int(mn), int(sec)

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total_days = sum(days_in_months[:month - 1])
    total_days += day - 1

    total_seconds = total_days * 86400 + hour * 3600 + minute * 60 + second

    return total_seconds


print(seconds_since_year_start("21/03/2026 09:03:37"))
