def Swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def InsertionSortDescending(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            Swap(A, i, i + 1)
            i = i - 1
        A[i + 1] = key
    return A


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))

    sort_array = InsertionSortDescending(arr)

    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, sort_array)))
