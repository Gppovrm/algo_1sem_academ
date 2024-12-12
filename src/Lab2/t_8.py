def plussing_p(A, B):
    return [a + b for a, b in zip(A, B)]


def subtract_p(A, B):
    return [a - b for a, b in zip(A, B)]


def karatsuba(A, B):
    n = len(A)

    if n == 1:
        return [A[0] * B[0]]

    m = n // 2

    A0, A1 = A[:m], A[m:]
    B0, B1 = B[:m], B[m:]

    t0, t2 = karatsuba(A0, B0), karatsuba(A1, B1)
    t1 = karatsuba(plussing_p(A0, A1), plussing_p(B0, B1))
    t1 = subtract_p(subtract_p(t1, t0), t2)

    result = [0] * (2 * n)
    for i in range(len(t0)):
        result[i] += t0[i]
    for i in range(len(t1)):
        result[i + m] += t1[i]
    for i in range(len(t2)):
        result[i + 2 * m] += t2[i]

    return result


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        A = list(map(int, file.readline().strip().split()))
        B = list(map(int, file.readline().strip().split()))

    # доп-е нулями
    while len(A) < len(B):
        A.append(0)
    while len(B) < len(A):
        B.append(0)
    while len(A) & (len(A) - 1) != 0:
        A.append(0)
        B.append(0)

    C = karatsuba(A, B)

    # удаляем лишние нулей для вывода
    while len(C) > 1 and C[-1] == 0:
        C.pop()

    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, C)))


if __name__ == "__main__":
    main()
