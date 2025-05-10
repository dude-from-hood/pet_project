from common.utils.fake_market.generate_utils import generate_new_product

test_data = [
    {
        "description": "Базовая проверка по созданию фейк магазина "
                       "ОР: Успешно, код 200",
        "expected_code": 201,
        "test_data": generate_new_product()

    }

    # todo: добавить проверки: точечные проверки на поля и негативные проверки

]