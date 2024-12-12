def max_heapify(A, i):
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left < len(A) and A[left] > A[i]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)


if __name__ == "__main__":
    A = [3, 1, 6, 5, 2, 4]
    print("Исходный массив:", A)
    build_max_heap(A)
    print("Массив после создания пирамиды:", A)


# ---------------------

def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and A[left] > A[i]:
        largest = left
    if right < heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    global heap_size
    heap_size = len(A)
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(A, i)

def heap_sort(A):
    global heap_size
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0)
        
if __name__ == "__main__":
    A = [3, 1, 6, 5, 2, 4]
    print("Исходный массив:", A)
    heap_sort(A)
    print("Отсортированный массив:", A)
