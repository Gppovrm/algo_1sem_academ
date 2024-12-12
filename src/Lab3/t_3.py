def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


def pugalo(arr, k):
    n = len(arr)
    for i in range(n - k):
        if arr[i] > arr[i + k]:
            arr[i], arr[i + k] = arr[i + k], arr[i]
    return 'ДА' if is_sorted(arr) else 'НЕТ'


if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as file:
        n, k = map(int, file.readline().strip().split())
        arr = list(map(int, file.readline().strip().split()))

    result = pugalo(arr, k)

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(result)
