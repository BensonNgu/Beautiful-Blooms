from tabulate import tabulate


def read_string(prompt):
    return input(prompt)


def read_int(prompt):
    while True:
        try:
            ans = input(prompt)
            if ans == '':
                return None
            return int(ans)
        except ValueError:
            print('Please enter whole number only !!!')


def read_double(prompt):
    while True:
        try:
            ans = float(input(prompt))
            return ans
        except ValueError:
            print('Please enter decimal point number only !!!')


def read_char(prompt):
    while True:
        ans = read_string(prompt)
        if len(ans) > 0:
            print('Please enter one character only !!!')
        else:
            return ans


def choose_option(data, prompt):
    table_data = []
    for i in range(0, len(data)):
        table_data.append((i+1, data[i]))

    headers = ['Idx', 'Option']
    print(tabulate(table_data, headers=headers, tablefmt='simple'))
    while True:
        ans = read_int(prompt)
        if 1 <= ans <= len(data):
            return data[ans-1]
        else:
            print('Please choose option in range 0 - ', len(data))


def choose_options(data, prompt, last_option=None):
    table_data = []
    for i in range(0, len(data)):
        table_data.append((i+1, data[i]))
    if last_option is not None:
        table_data.append((0, last_option))
    headers = ['Idx', 'Option']
    print(tabulate(table_data, headers=headers, tablefmt='simple'))
    while True:
        ans = read_int(prompt)
        if 1 <= ans <= len(data):
            return ans
        else:
            print('Please choose option in range 0 - ', len(data))


def print_title(title):
    # Calculate the length of the title for formatting
    title_length = len(title)

    # Print the title surrounded by a border
    print("╔" + "═" * title_length + "╗")
    print("║" + title + "║")
    print("╚" + "═" * title_length + "╝")


def display_menu(title, menu, last_option):
    print_title(title)

    # Print each menu option
    for i, option in enumerate(menu, start=1):
        print(f"{i}. {option}")

    # Print the last option
    print(f"0. {last_option}")


def get_user_option(title, menu, last_option):
    display_menu(title, menu, last_option)
    while True:
        ans = read_int('Enter option: ')
        if 0 <= ans <= len(menu):
            return ans
        else:
            print('Please choose option in range 0 - ', len(menu))