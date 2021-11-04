# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("HWL5_5.txt", 'w+') as my_file:
    try:
        my_text = input('Введите числа разделенные пробелом ->> ')
        if len(my_text) > 0:
            my_file.write(my_text)
    except IOError:
        print('Ошибка ввода')

with open("HWL5_5.txt") as my_file:
    print(f"Сумма чисел равна = {sum([int(x) for x in my_file.read().split(' ')])}")

