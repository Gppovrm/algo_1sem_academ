def count(A, l, r, x):
    return sum(1 for i in range(l, r + 1) if A[i] == x)


def maj(A, l, r):
    if l == r:
        return A[l]

    mid = (l + r) // 2
    left_maj = maj(A, l, mid)
    right_maj = maj(A, mid + 1, r)

    if left_maj == right_maj:
        return left_maj

    l_count = count(A, l, r, left_maj)
    r_count = count(A, l, r, right_maj)

    return left_maj if l_count > r_count else right_maj


def is_majority(A, elem):
    count = sum(1 for x in A if x == elem)
    return count > len(A) // 2


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        A = list(map(int, file.readline().strip().split()))

    result = 1 if is_majority(A, maj(A, 0, n - 1)) else 0

    with open('output.txt', 'w') as file:
        file.write(str(result) + '\n')

if __name__ == "__main__":
    main()

