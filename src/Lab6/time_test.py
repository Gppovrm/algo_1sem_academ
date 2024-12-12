from time import perf_counter_ns
from psutil import Process
from os import getpid

start_time = perf_counter_ns()


def vvod():
    from numba import njit

    @njit
    def process_hash_table_optimized(N, X, A, B, AC, BC, AD, BD):
        table = set()
        for _ in range(N):
            if X in table:
                A = (A + AC) % 1000
                B = (B + BC) % 10 ** 15
            else:
                table.add(X)
                A = (A + AD) % 1000
                B = (B + BD) % 10 ** 15
            X = (X * A + B) % 10 ** 15
        return X, A, B

    def main():
        with open('input.txt', 'r') as infile:
            N, X, A, B = map(int, infile.readline().split())
            AC, BC, AD, BD = map(int, infile.readline().split())

        X, A, B = process_hash_table_optimized(N, X, A, B, AC, BC, AD, BD)

        with open('output.txt', 'w') as outfile:
            outfile.write(f"{X} {A} {B}\n")

    if __name__ == "__main__":
        main()


vvod()
print('Время выполнения:', (perf_counter_ns() - start_time) / 10 ** 9, 'с')
print('Затраты памяти:', Process(getpid()).memory_info().rss / 1024 ** 2, 'Мб')
