from sys import argv as arg
from datetime import datetime as dt


def today(current_date: str, date: str) -> bool:
    return True if current_date == date else False


if __name__ == '__main__':
    _, *args = arg
    date = args.pop() if args else ''
    current_date = dt.now().date().strftime("%d.%m.%Y")
    message = f'Все правильно, сегодня {current_date}' if today(current_date, date) \
        else f'Нет, не так, сегодня {current_date}'
