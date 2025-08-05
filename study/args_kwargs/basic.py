"""
ARGS - произвольное кол-во Позиционных аргументов
KWARGS - произвольное кол-во Именованных аргументов

"""


def upd_dict(*args, **kwargs):
    s = dict()

    # Обрабатываем args
    for i, arg in enumerate(args):
        s[f"arg_{i}"] = arg

    # Обрабатываем kwargs
    s.update(kwargs)

    # можно также и вручную хэндлить kwargs
    # for key, value in kwargs.items():
    #     s[key] = value

    return s


print(upd_dict('sdr', 555, [1, 2, 3], a=1, b=2, c=3, d=4))
