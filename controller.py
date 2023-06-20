import view
import model
d = {}

def start():
    view.greetings()              #приветствие пользователя
    while True:
        view.menu()                # тут во вкладке вью должны быть прописаны команды под номерами
        answer = input('Введите команду, которую вы хотите сделать: ')
        if answer == '1':                        #показывает весь список
            view.show_contacts(model.get_all())
        elif answer == '2':
            phone, name = input('Введите номер телефона и через пробел имя, фамилию с разделением через нижнее подчеркивание: ').split()
            model.add_contact(name, phone)                     # добавить контакт
            view.result()                        #выводит результат успешно или нет
        elif answer == '3':
            name = input('Введите имя контакта для поиска: ')    #поиск контакта по любой характеристике
            result = model.find_name(name)                  
            view.show_contacts(result)
        elif answer == '4':
            name = input('Введите имя удаляемого контакта: ')    #удаление контакта по любым данным
            model.delete_name(name)
            view.delete_contacts(name)          #должен выдавать сообщение об удалении контакта
        elif answer == '5':
            name = input('Введите имя контакта, которое хотите изменить: ')   #данные  для изменения по любым данным
            new_name=input("введите новое имя контакта") 
            model.change_name(name, new_name)    # тут вводится новое значение
            view.change_contacts(new_name)     #тут должен выдавать результат об изменении
        elif answer == '6':
            phone= input('Введите номер контакта, который хотите изменить: ')   #данные  для изменения по любым данным
            new_phone=input("введите новый номер контакта")    # тут вводится новое значение
            result = model.change_phone(phone, new_phone) 
            view.change_contacts(result)     #тут должен выдавать результат об изменении
        elif answer == '7':     #выход из программы
            print("the end")
        else:
            view.error()         #бьет ошибку ввода, если введена неверная цифраъ
            

start()
