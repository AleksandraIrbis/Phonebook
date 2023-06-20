import json
d = {}

def get_all(): #показать все, что есть
  global d
  return d

def add_contact(name, phone):# добавить контакт
    global d
    d[name] = phone
    with open('dictionary.json', 'w') as file:
        json.dump(d, file)
    return True
     

def delete_name(name):# удалить контакт
    global d
    if name in d:
        del d[name]
        with open('dictionary.json', 'w') as file:
                json.dump(d, file)
        return True
    return False
     
    




def find_name(name):# найти по имени
    global d
    if name in d:
        result=d.get(name)
        return result
    return False
     


def change_phone(name, new_phone):# изменить номер
        global d
        if name in d:
            d[name] = new_phone
            with open('dictionary.json', 'w') as file:
                json.dump(d, file)
            return True
        return False




def change_name(name, new_name): # изменить имя
    global d
    if name in d:
        d[new_name] = d.pop(name)
        with open('dictionary.json', 'w') as file:
                json.dump(d, file)
        return True
    return False


