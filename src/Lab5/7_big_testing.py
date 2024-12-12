import sys
import random
import time

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

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high, max_depth):
    if low < high:
        if max_depth == 0:
            insertion_sort(arr[low:high + 1])
        else:
            pi = randomized_partition(arr, low, high)
            randomized_quicksort(arr, low, pi - 1, max_depth - 1)
            randomized_quicksort(arr, pi + 1, high, max_depth - 1)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m+1]
    R = arr[m+1:r+1]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] >= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def gen_rev_sort_arr(n):
    return list(range(n, 0, -1))

def gen_sort_arr(n):
    return list(range(1, n + 1))

def gen_arr_w_few_unique(n, unique_elements):
    return [random.choice(unique_elements) for _ in range(n)]

def gen_random_arr(n):
    return [random.randint(-10**9, 10**9) for _ in range(n)]

def big_testing():
    sizes = [10**3, 10**4, 10**5, 10**9]
    for n in sizes:
        arrays = {
            "reverse_sorted": gen_rev_sort_arr(n),
            "sorted": gen_sort_arr(n),
            "few_unique": gen_arr_w_few_unique(n, [1, 2, 3, 4, 5]),
            "random": gen_random_arr(n),
        }

        for name, arr in arrays.items():
            print(f"Тест {name} на массиве размером {n}")

            for sort_name, sort_func in [
                ("HeapSort", heap_sort),
                ("QuickSort", lambda arr: randomized_quicksort(arr, 0, len(arr) - 1, sys.getrecursionlimit() // 2)),
                ("MergeSort", lambda arr: merge_sort(arr, 0, len(arr) - 1)),
                ("InsertionSort", insertion_sort)

            ]:
                arr_copy = arr.copy()
                start_time = time.time()
                sort_func(arr_copy)
                duration = time.time() - start_time
                print(f"{sort_name}: {duration:.6f} сек")

if __name__ == "__main__":
    big_testing()
