def var_generator(group_num, group_size, surname, student_number):
    A = int(str(group_num)[-2:])

    def next_prime(n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        prime = n + 1
        while not is_prime(prime):
            prime += 1
        return prime

    p = next_prime(group_size)  # Следующее простое число большее, чем количество человек в группе

    # Сумма кодов ASCII всех букв фамилии
    B = sum(ord(char) for char in surname)

    task1 = (A * student_number % p) % 9
    task2 = ((A * student_number + B) % p) % 9

    # Проверка на подряд идущие задачи
    if task1 == task2 or task1 + 1 == task2:
        task2 = (task2 + 2) % 9

    task3 = (task1 + 2) % 9
    if task3 == task2 or task3 + 1 == task2 or task3 - 1 == task2 or task3 + 1 == task1 or task3 - 1 == task1:
        task3 = (task3 + 2) % 9

    return task1, task2, task3


group_num = 3241
group_size = 35
surname = "Савченко"
student_number = 25

task1, task2, task3 = var_generator(group_num, group_size, surname, student_number)
print(f"Номер первой задачи: {task1}")
print(f"Номер второй задачи: {task2}")
print(f"Номер третьей задачи: {task3}")

