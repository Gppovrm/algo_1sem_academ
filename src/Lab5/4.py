def min_heapify(A, n, i, swaps):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < n and A[left] < A[smallest]:
        smallest = left

    if right < n and A[right] < A[smallest]:
        smallest = right

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        swaps.append((i, smallest))
        min_heapify(A, n, smallest, swaps)
        print(swaps)


def build_min_heap(A):
    n = len(A)
    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(A, n, i, swaps)
    return swaps


if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        n = int(input_file.readline().strip())
        arr = list(map(int, input_file.readline().strip().split()))

    swaps = build_min_heap(arr)

    with open('output.txt', 'w') as output_file:
        output_file.write(f"{len(swaps)}\n")
        output_file.writelines(f"{i} {j}\n" for i, j in swaps)
