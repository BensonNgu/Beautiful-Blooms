import keyboard


if __name__ == '__main__':
    price = 30
    new_price = keyboard.read_int('New Price: ')
    if new_price is None:
        print('The price remain the same: $', price)
    else:
        print('The price has been changed\nOld price: ',price)
        price = new_price
        print('New price: ', price)