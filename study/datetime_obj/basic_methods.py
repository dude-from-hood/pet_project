if __name__ == '__main__':
    from datetime import datetime, timedelta
    import pytz
    import os

    # задать часовой пояс
    msk_tz = pytz.timezone('Europe/Moscow')

    # текущее время - 7 мин в Москве = datetime
    time_msk = datetime.now(tz=msk_tz) - timedelta(minutes=7)
    print(time_msk)

    # время в UTC - datetime
    time_utc = time_msk.astimezone(tz=pytz.UTC)
    print(time_utc)

    # время в UTC - str на конце Z
    time_utc_with_z = time_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
    print(time_utc_with_z)

    # unix
    unix_time = int(time_msk.timestamp())
    print(unix_time)

    # Обратное преобразование: timestamp → aware datetime в UTC, затем в Москву
    dt_utc = datetime.fromtimestamp(unix_time, tz=pytz.UTC)
    print(dt_utc)
    dt_moscow_roundtrip = dt_utc.astimezone(msk_tz)
    print(dt_moscow_roundtrip)

    # абсолютный путь к текущей директории
    abs_path_dir = os.path.abspath(os.path.dirname(__file__))
    print(abs_path_dir)

    # абсолютный путь к текущему файлу
    abs_path_file = os.path.abspath(__file__)
    print(abs_path_file)
