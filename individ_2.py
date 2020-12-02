#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

#   Для варианта задания лабораторной работы 8 необходимо дополнительно
#   реализовать сохранение и чтение данных из файла формата JSON. Необходимо проследить за
#   тем, чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной
#   работы.

if __name__ == '__main__':
    # Список работников.
    students = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные о работнике.
            n = 5
            name = input("Введите фамилию и имя: ")
            group = input("Введите группу: ")
            marks = list(map(int, input("Введите пять оценок студента, в формате - x y z: ").split(None, n)[:n]))

            if 5 > marks[0] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            if 5 > marks[1] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            if 5 > marks[2] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            if 5 > marks[3] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            if 5 > marks[4] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            # Создать словарь.
            person = {
                'name': name,
                'group': group,
                'marks': marks,
            }

            students.append(person)
            if len(students) > 1:
                students.sort(key=lambda item: item.get('name', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8,
                '-' * 8,
                '-' * 8,
                '-' * 8,
                '-' * 8,
                '-' * 11
            )
            print(line)
            print(
                '| {:^3} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} | {:^8} | {:^8} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Группа",
                    "1-ая оценка",
                    "2-ая оценка",
                    "3-ая оценка",
                    "4-ая оценка",
                    "5-ая оценка"
                )
            )
            print(line)
            # Вывести данные о всех сотрудниках.
            for idx, person in enumerate(students, 1):
                print(
                    '| {:>3} | {:<30} | {:<20} | {:>11} | {:>11} | {:>11} | {:>11} | {:>11} |'.format(
                        idx,
                        person.get('name', ''),
                        person.get('group', ''),
                        person.get('marks[0]', f'{marks[0]}'),
                        person.get('marks[1]', f'{marks[1]}'),
                        person.get('marks[2]', f'{marks[2]}'),
                        person.get('marks[3]', f'{marks[3]}'),
                        person.get('marks[4]', f'{marks[4]}')
                    )
                )
            print(line)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            period = int(parts[1])

            count = 0
            for person in students:
                if 2 in marks:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, person.get('name', ''))
                    )
            # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("Нет студентов, которые получили оценку - 2.")
        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            # Прочитать данные из файла JSON.
            with open(parts[1], 'r') as f:
                students = json.load(f)
        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            # Сохранить данные в файл JSON.
            with open(parts[1], 'w') as f:
                json.dump(students, f)
        elif command == 'help':
            # Вывести справку о работе с программой.
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("select <оценка> - найти студентов которые получили такую оценку;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
