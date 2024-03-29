import keyboard
from datetime import date


if __name__ == '__main__':
    deliver_date = date(2024,12,30)
    print(deliver_date.strftime('%d %b %Y'))
