def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))

    sorted_array = selection_sort(array)

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(' '.join(map(str, sorted_array)))
