# (без numba)

# class HashTable:
#     def __init__(self):
#         self.table = set()
#
#     def add_key(self, key):
#         self.table.add(key)
#
#     def remove_key(self, key):
#         self.table.discard(key)
#
#     def check_key(self, key):
#         return key in self.table
#
#
# if __name__ == "__main__":
#     with open('input.txt', 'r') as input_file:
#         N, X, A, B = map(int, input_file.readline().split())
#         AC, BC, AD, BD = map(int, input_file.readline().split())
#
#     hash_table = HashTable()
#
#     for _ in range(N):
#         if hash_table.check_key(X):
#             A = (A + AC) % 1000
#             B = (B + BC) % 10 ** 15
#         else:
#             hash_table.add_key(X)
#             A = (A + AD) % 1000
#             B = (B + BD) % 10 ** 15
#
#         X = (X * A + B) % 10 ** 15
#
#     with open('output.txt', 'w') as output_file:
#         output_file.write(f"{X} {A} {B}")
from numba import njit


@njit
def hash_table(N, X, A, B, AC, BC, AD, BD):
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


if __name__ == "__main__":
    with open('input.txt', 'r') as infile:
        N, X, A, B = map(int, infile.readline().split())
        AC, BC, AD, BD = map(int, infile.readline().split())

    X, A, B = hash_table(N, X, A, B, AC, BC, AD, BD)

    with open('output.txt', 'w') as outfile:
        outfile.write(f"{X} {A} {B}")
