
d = {}

def add_contact(name, phone):# добавить контакт
     d.setdefault(name, []).append(phone)

def delete_name(name):# удалить контакт
    del d[name]


def see_all(d):# посмотреть весь список
        import pprint
def find_name(name):# найти по имени
    result=d.get(name)

def change_phone(phone, new_phone):# изменить номер
        global d
        d[phone] =new_phone


def change_name(name, new_name): # изменить имя
    global d
    d[new_name] = d.pop(name)


