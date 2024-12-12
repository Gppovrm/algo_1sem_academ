def valid_heap(arr):
    n =len(arr)
    for i in range(n // 2):
        if 2 * i + 1 < n and arr[i] > arr[2 * i + 1]:
            return "NO"
        if 2 * i + 2 < n and arr[i] > arr[2 * i + 2]:
            return "NO"
    return "YES"


if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        n = int(input_file.readline().strip())
        arr = list(map(int, input_file.readline().strip().split()))

    ans = valid_heap(arr)

    with open('output.txt', 'w') as output_file:
        output_file.write(ans)
