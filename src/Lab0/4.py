from time import perf_counter_ns
from psutil import Process
from os import getpid

start_time = perf_counter_ns()


def testing():
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.read())
        fibonacci = [0, 1]
        for i in range(2, n + 1):
            fibonacci.append((fibonacci[-1] + fibonacci[-2]) % 10)

        output_file.write(str(fibonacci[n]))


testing()
print('Время выполнения:', (perf_counter_ns() - start_time) / 10 ** 9, 'с')
print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'Мб')
