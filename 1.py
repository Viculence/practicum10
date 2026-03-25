def count_letters(sentence):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "бвгджзйклмнопрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"

    vowel_count = 0
    consonant_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    print(f"Гласных: {vowel_count}")
    print(f"Согласных: {consonant_count}")


count_letters("Ослу образованье дали. Он стал умней? Едва ли.")