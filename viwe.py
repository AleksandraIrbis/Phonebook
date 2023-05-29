
def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    second_name = input('Введите отчество: ')
    info.append(second_name)
    phone_number = input('Введите номер телефона: ')
    while len(phone_number) < 11:
        phone_number = input('Количествво символов не верное. Повторите ввод: ')
    for i in phone_number:
        if i not in '-()0123456789 ':
            phone_number = input(f'Номер введен не верно (символ ({i})). Повторите ввод: ')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info

def get_change_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(f'| {last_name} ')
    first_name = input('Введите имя: ')
    info.append(f'| {first_name} ')
    second_name = input('Введите отчество: ')
    info.append(f'| {second_name} ')
    phone_number = input('Введите номер телефона: ')
    while len(phone_number) < 11:
        phone_number = input('Количествво символов не верное. Повторите ввод: ')
    for i in phone_number:
        if i not in '-()0123456789 ':
            phone_number = input(f'Номер введен не верно (символ ({i})). Повторите ввод: ')
    info.append(f'| {phone_number} ')
    description = input('Введите описание: ')
    info.append(f'| {description} | ')
    return info

def search():
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    flag = 1
    name = input('Введите данные для поиска: ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('Введенных данных нет в справочнике')

def ind_search():
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    count = 0
    name = input('Введите данные для поиска: ')
    flag = 1
    for line in data:
        if name in line:
            flag = 0
    if flag: print(f'\nВведенных данных нет в справочнике. Повторите команду.')
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    for line in data:
        count += 1
        if name in line:
            count -= 1
            return count

def ind_search():
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    count = 0
    name = input('Введите данные строки для удаления: ')
    flag = 1
    for line in data:
        if name in line:
            flag = 0
    if flag: print(f'\nВведенных данных нет в справочнике. Повторите команду.')
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    for line in data:
        count += 1
        if name in line:
            count -= 1
            return count

def creating ():
    with open ('Phonebook.csv', 'w', encoding = 'utf-8') as data:
        data.write(f'| Фамилия | Имя | Отчество | Номер телефона | Описание |\n')

def writing_scv_txt():
    info = get_info()
    with open ('Phonebook.csv', 'a', encoding = 'utf-8') as data:
        data.write(f'| {info[0]} | {info[1]} | {info[2]} | {info[3]} | {info[4]} |\n')
    with open ('Phonebook.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nОтчество: {info[2]}\nНомер телефона: {info[3]}\nОписание: {info[4]}\n\n')
