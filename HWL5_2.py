# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
sch = 0
try:
    with open("HWL5_2.txt") as my_file:
        if my_file.readable():
            for line in my_file:
                sch +=1
                pr_line = len(line.split())
                print(f'В {sch} строке {pr_line} слов ')
        else:
            print("Ошибка чтения файла")
except FileNotFoundError:
    print('Файл отсутствует')