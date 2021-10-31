# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open("HWL5_1.txt", 'w+') as my_file:
    while True:
        try:
            my_text = input('Введите любой текст, окончание ввода пустая строка ->> ')
            if len(my_text) > 0:
                my_file.write(my_text+'\n')
            else:
                if my_file.readable():
                    for line in my_file:
                        print(my_file.read())
                else:
                    print('Файл не читаемый')
                break
        except IOError:
            print("Ошибка ввода/вывода")
