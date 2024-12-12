from time import perf_counter_ns
from psutil import Process
from os import getpid

start_time = perf_counter_ns()


def vvod():
    pass


vvod()
print('Время выполнения:', (perf_counter_ns() - start_time) / 10 ** 9, 'с')
print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'Мб')
