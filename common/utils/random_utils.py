def add(a, b):
    """Функция сложения двух чисел"""
    return a + b

# def helper(sms_message: str, max_length: int=10):
#
#     if not isinstance(sms_message, str):
#         raise TypeError("Не строка sms_message")
#
#     if 1 <= len(sms_message) <= max_length:
#         return sms_message
#
#     elif sms_message == "":
#         print("sms_message является пустой строкой")
#         return sms_message
#
#     elif len(sms_message) > max_length:
#         print(f'Truncated message to {max_length=}')
#         return sms_message[:max_length - 3] + '...'