# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.
with open('HWL5_4.txt', 'r', encoding='utf-8') as my_file,  open('HWL5_4_1.txt', 'w', encoding='utf-8') as new_file:
    for line in my_file:
        if line[:line.find(' ')] == 'One':
            new_file.write(line.replace('One', 'Один'))
        elif line[:line.find(' ')] == 'Two':
            new_file.write(line.replace('Two', 'Два'))
        elif line[:line.find(' ')] == 'Three':
            new_file.write(line.replace('Three', 'Три'))
        else:
            new_file.write(line.replace('Four', 'Четыре'))

with open('HWL5_4_1.txt', 'r', encoding='utf-8') as new_file:
    print(new_file.read())
