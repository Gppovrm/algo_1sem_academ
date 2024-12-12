def max_heapify(arr, n, i):
    while i < n:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            break


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        n = int(input_file.readline().strip())
        arr = list(map(int, input_file.readline().strip().split()))

    heap_sort(arr)

    with open('output.txt', 'w') as output_file:
        output_file.write(" ".join(map(str, arr)))
