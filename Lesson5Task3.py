# 3. Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
def task_1():
    wages = {}
    try:
        with open('../examples5/text_3.txt', 'r', encoding='utf-8') as f:
            for line in f:
                wages[line.split()[0]] = float(line.split()[1])
        print("Меньше 20000р получают: ")
        for name, wage in wages.items():
            if wage < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Бухгалтер уволился.')


task_1()
