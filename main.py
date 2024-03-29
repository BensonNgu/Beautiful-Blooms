import csv
import keyboard
from tabulate import tabulate

# bring all the class from model
from model import Product
from model import Addon
from model import Order

products = []
addons = []
orders = []
categories = ['Romantic', 'Birthday', 'Grand Opening', 'Condolence', 'Anniversary']


# file io
def open_inventory():
    try:
        file = open("Products.txt", "r")
        csvreader = csv.reader(file)
        for row in csvreader:
            code = row[0]
            name = row[1]
            category = row[2]
            price = int(row[3])
            status = row[4]
            b = Product(code, name, price, category, status)
            products.append(b)
        file.close()
    except FileNotFoundError:
        print('No product found')


def save_inventory():
    file = open("Products.txt", "w")
    for product in products:
        file.write(product.export_csv())
    file.close()


def open_addon():
    try:
        file = open("Addons.txt", "r")
        csvreader = csv.reader(file)
        for row in csvreader:
            code = row[0]
            name = row[1]
            price = int(row[2])
            status = row[3]
            b = Addon(code, name, price, status)
            addons.append(b)
        file.close()
    except FileNotFoundError:
        print('No add-on found')


def save_addon():
    file = open("Addons.txt", "w")
    for addon in addons:
        file.write(addon.export_csv())
    file.close()


# sample sorting algo
def sort_by_code():
    products.sort(key=lambda x: x.code)


# sample filtering algo
def filtering():
    return filter(lambda product: product.category == 'Anniversary', products)


# load the data into the system
def initiate():
    open_inventory()
    open_addon()


def tabulating(table_data, headers):
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


def show_products():
    table_data = [product.display() for product in products]
    headers = ["Item Code", "Item Name", "Price", "Category", "Status"]
    tabulating(table_data, headers)


def show_addon():
    table_data = [addon.display() for addon in addons]
    headers = ["Item Code", "Name", "Price", "Status"]
    tabulating(table_data, headers)


def show_order():
    table_data = [order.display() for order in orders]


def check_unique_code(code, array):
    for item in array:
        if item.code == code:
            return False
    return True


# inventory
def search_inventory(code):
    for product in products:
        if product.code == code:
            return product
    return None


def add_new_product():
    keyboard.print_title('New Product')
    name = keyboard.read_string('Name: ')
    code = keyboard.read_string('Code (Auto generated if left blank): ')
    price = keyboard.read_int('Price: ')
    category = keyboard.choose_option(categories, 'Select one of the category: ')
    if code == '':
        code = category[0]
        idx = 1
        for product in products:
            if product.code[0] == code:
                idx = idx + 1
        code = code + str(idx).zfill(3)
    else:
        check_unique_code(code, products)
    products.append(Product(code, name, price, category, 'Available'))
    save_inventory()


# addon
def search_addon(code):
    for addon in addons:
        if addon.code == code:
            return addon
    return None


def update_item(target, array):
    print(target.show())
    # edit price
    new_price = keyboard.read_int('Enter new price (left blank to keep the old data): ')
    if new_price is not None:
        target.price = new_price
    # edit status
    new_status = keyboard.read_string('Enter new status (left blank to keep the old data): ')
    if new_status != '':
        target.status = new_status
    # # edit status
    # update the array
    for i in range(0, len(array)):
        if array[i].code == target.code:
            array[i] = target


def add_new_addon():
    keyboard.print_title('New Add-Ons')
    name = keyboard.read_string('Name: ')
    while True:
        code = keyboard.read_string('Code (Auto generated if left blank): ')
        if check_unique_code(code, addons):
            if code == '':
                idx = 1
                for addon in addons:
                    if addon.code[0:2] == 'ADD':
                        idx = idx + 1
                code = 'ADD' + str(idx).zfill(3)
                break
        else:
            print('The code entered has been taken !!!\nPlease choose another one.')
    price = keyboard.read_int('Price: ')
    addons.append(Addon(code, name, price))
    save_addon()


def inventory_management():
    title = 'Inventory Management'
    menu = ['View/Update Blooms', 'Add New Blooms', 'View/Update Add-Ons', 'Add new Add-Ons']
    last_option = 'Back to Main Menu'
    while True:
        option = keyboard.get_user_option(title, menu, last_option)
        match option:
            case 0:
                print('Going back to main menu...')
                break
            case 1:
                while True:
                    show_products()
                    print('To update an item, enter the item code. Or enter 0 to go back to previous menu.')
                    result = keyboard.read_string('> ')
                    try:
                        if int(result) == 0:
                            print('Going back to Inventory Management Page...\n')
                            break
                        else:
                            print('Invalid option...')
                    except ValueError:
                        target = search_inventory(result)
                        if target is None:
                            print('Code entered does not exist\nGoing back to Inventory Management Page...\n')
                            break
                        else:
                            update_item(target, products)
                            save_inventory()
            case 2:
                add_new_product()
            case 3:
                while True:
                    show_addon()
                    print('To update an item, enter the item code. Or enter 0 to go back to previous menu.')
                    result = keyboard.read_string('> ')
                    try:
                        if int(result) == 0:
                            print('Going back to Inventory Management Page...\n')
                            break
                        else:
                            print('Invalid option...')
                    except ValueError:
                        target = search_addon(result)
                        if target is None:
                            print('Code entered does not exist\nGoing back to Inventory Management Page...\n')
                        else:
                            update_item(target, addons)
                            save_addon()
            case 4:
                add_new_addon()


def order_item():
    while True:
        code = keyboard.read_string('Please enter item code": ')
        if search_inventory(code) is None:
            print('The code entered does not exist !!!')
        else:
            break

    orders.append(code)


def create_order():
    show_products()
    selections = ['Filter products by category', 'Sort products by price', 'Order item']
    prompt = '> '
    option = keyboard.choose_option(selections, prompt)
    match option:
        case 0:
            filtering_criteria = keyboard.choose_option(categories, prompt)

        # case 1:
        #
        # case 2:


def sales_management():
    title = 'Sales Management'
    menu = ['Create Order', 'View Order']
    last_option = 'Back to main menu'
    while True:
        option = keyboard.get_user_option(title, menu, last_option)
        match option:
            case 0:
                print('Going back to main menu...')
                break
            case 1:
                create_order()



def main_menu():
    while True:
        option = keyboard.get_user_option('Beautiful Blooms', ['Inventory Management', 'Sales Management'], 'Exit')
        match option:
            case 0:
                print('Good bye')
                break
            case 1:
                # TODO: inventory - done
                inventory_management()
            case 2:
                # TODO: sales - in progress
                sales_management()


if __name__ == '__main__':
    initiate()
    main_menu()
