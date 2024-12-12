from time import perf_counter_ns
from psutil import Process
from os import getpid

start_time = perf_counter_ns()


def vvod():
    from collections import deque

    def medecine(commands):
        q = deque()
        results = []
        for c in commands:
            if c.startswith('+'):
                _, i = c.split()
                q.append(i)
            elif c.startswith('*'):
                _, i = c.split()
                mid = (len(q) + 1) // 2
                q.insert(mid, i)
            elif c.startswith('-'):
                if q:
                    results.append(q.popleft())
        return results

    if __name__ == "__main__":
        with open('input.txt', 'r') as file:
            n = int(file.readline().strip())
            comm = [file.readline().strip() for _ in range(n)]

        results = medecine(comm)

        with open('output.txt', 'w') as file:
            for result in results:
                file.write(result + '\n')


vvod()
print('Время выполнения:', (perf_counter_ns() - start_time) / 10 ** 9, 'с')
print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'Мб')
