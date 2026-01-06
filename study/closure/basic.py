def countdown(n):
    total = n

    def wrapper():
        nonlocal total # "Используй total из внешней функции countdown !"

        if total > 0:
            print(total)
            total -= 1

        else:
            print(f'Превышен лимит, вы вызвали более {n} раз')

    return wrapper

count = countdown(3)
count()
count()
count()
count()
count()