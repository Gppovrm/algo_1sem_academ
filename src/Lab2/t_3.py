def inv_count(A, l, q, r):
    n1 = q - l + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = A[l + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]

    i = j = 0
    k = l
    icounter = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            icounter += (n1 - i)
            j += 1
        k += 1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

    return icounter


def merge_sort(A, AA, l, r):
    icounter = 0
    if l < r:
        q = (l + r) // 2
        icounter += merge_sort(A, AA, l, q)
        icounter += merge_sort(A, AA, q + 1, r)
        icounter += inv_count(A, l, q, r)
    return icounter


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        A = list(map(int, file.readline().strip().split()))

    AA = [0] * n
    icounter = merge_sort(A, AA, 0, n - 1)

    with open('output.txt', 'w') as file:
        file.write(str(icounter) + '\n')


if __name__ == "__main__":
    main()
