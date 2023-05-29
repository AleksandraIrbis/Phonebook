import controller 

def n():
    return 


def menu():
    print(
        '1 - Показать все контакты\n'
        '2 - Добавить контакт\n'
        '4 - Изменить контакт\n'
        '3 - Удалить контакт\n'
        '4 - Поиск контакта\n'
        '5 - Выход\n'
    )

def error():
    return 

def show_contacts():
    return 

def su():
    return 

def s():
    return 

def search():
    data = open('Phonebook.csv', 'r', encoding = 'utf-8')
    flag = 1
    name = input('Введите данные для поиска: ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('Введенных данных нет в справочнике')





if __name__=='__main__':
    menu()