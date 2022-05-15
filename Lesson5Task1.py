# 1. Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
with open('text_1.txt', 'w',encoding='utf-8') as f:
    while True:
        line = input('Введите свой текс. Для выхода нажмите Enter: ')
        if not line:
            break
        print(line, file=f)

# Вариант
print("Enter your text and don't be surprised if you won't see it\nFor exit press enter :-))")
with open('text_1.txt', 'w', encoding='utf-8') as my_file:
    while (line := input("Enter your text: ")) != '':
        my_file.write(f"{line}\n")
