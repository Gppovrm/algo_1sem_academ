def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
        k = int(file.readline().strip())
        k_n = list(map(int, file.readline().strip().split()))

    results = []
    for kk in k_n:
        result = binary_search(arr, kk)
        results.append(result)

    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, results)))


if __name__ == "__main__":
    main()
