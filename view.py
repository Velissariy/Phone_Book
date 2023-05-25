import text_fields as tf


def input_choice(size: int, message: str):
        while True:
             number = input(message)
             if number.isdigit() and 0 < int(number) < size+1:
              return int(number)
        else:
              print(tf.wrong_choice(size))


def main_menu() -> int:
    print(*tf.menu, sep='\n')
    return input_choice(len(tf.menu)-1, tf.input_choice)

def show_contact(book: list[dict[str,str]], message: str):
    if book:
        print('\n' + '=' * 72)
        for i, contact in enumerate(book, 1):
            print(f'{i:<3} | {contact["name"]:<20} | {contact["phone"]:<20} '
                  f'| {contact["comment"]:<20}')
        print('=' * 72 + '\n')
    else:
        print(message)

def print_message(message: str):
        print('\n' + '=' * len(message))
        print(message)
        print('=' * len(message) + '\n')

def input_contact(message: list[str]) -> dict[str,str]:
    contact = {}
    name = input(message[0])
    phone = input(message[1])
    comment = input(message[2])
    if name:
        contact['name'] = name
    if phone:
        contact['phone'] = phone
    if comment:
        contact['comment'] = comment
    return contact


def enter_keyword() -> str:
    print()
    key_word = input(tf.input_keyword)
    return key_word

def input_index(book: list, message: str) -> int:
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) + 1:
            return int(choice)

def edit_contact(book: list, message: str) -> tuple[int, dict[str, str]]:
    index = 0
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) + 1:
            index = int(choice)
            break
    print(tf.enter_or_empty)
    contact = new_contact()
    return index, contact

def new_contact() -> dict[str, str]:
    print()
    name = input(tf.new_name)
    phone = input(tf.new_phone)
    comment = input(tf.new_comment)
    return {'name': name, 'phone': phone, 'comment': comment}


def confirm(message: str):
    answer = input(message + ' (y/n)')
    if answer.lower() == 'y':
        return True
    return False