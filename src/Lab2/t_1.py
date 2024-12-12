#Сигналом к остановке должен служить тот факт, что все элементы массива L или R скопированы обратно в массив A, после чего в этот массив копируются элементы, оставшиеся в непустом массиве.
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]

    i = j = 0
    k = p

    # copy элем-ы из массивов L , R обратно в массив A
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # copy оставшиеся эл массива L
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    # copy элементы массива R, если они есть
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        A = list(map(int, file.readline().strip().split()))

    merge_sort(A, 0, n - 1)

    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, A)) + '\n')


if __name__ == "__main__":
    main()


# код как псевокод из лекции
# def merge(A, p, q, r):
#     n1 = q - p + 1
#     n2 = r - q
#     L = [0] * (n1 + 1)
#     R = [0] * (n2 + 1)
#
#     for i in range(n1):
#         L[i] = A[p + i]
#     for j in range(n2):
#         R[j] = A[q + 1 + j]
#
#     L[n1] = float('inf')
#     R[n2] = float('inf')
#     i = j = 0
#
#     for k in range(p, r + 1):
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#         else:
#             A[k] = R[j]
#             j += 1
#
#
# def merge_sort(A, p, r):
#     if p < r:
#         q = (p + r) // 2
#         merge_sort(A, p, q)
#         merge_sort(A, q + 1, r)
#         merge(A, p, q, r)
#     return A
#
#
# def main():
#     with open('input.txt', 'r') as file:
#         n = int(file.readline().strip())
#         A = list(map(int, file.readline().strip().split()))
#
#     merge_sort(A, 0, n - 1)
#
#     with open('output.txt', 'w') as file:
#         file.write(' '.join(map(str, A)) + '\n')
#
#
# if __name__ == "__main__":
#     main()
