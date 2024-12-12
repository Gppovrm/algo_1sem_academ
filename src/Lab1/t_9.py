def binary_addition(A, B):
    n = len(A)
    C = [0] * (n + 1)
    curr = 0

    for i in range(n - 1, -1, -1):
        total = A[i] + B[i] + curr
        C[i + 1] = total % 2
        curr = total // 2

    C[0] = curr
    return C


def read_input_file():
    with open('input.txt', 'r') as file:
        line = file.readline().strip()
    A_str, B_str = line.split()
    A = list(map(int, A_str))
    B = list(map(int, B_str))
    return A, B


def write_output_file(C):
    with open('output.txt', 'w') as file:
        file.write(''.join(map(str, C)) + '\n')


if __name__ == "__main__":
    A, B = read_input_file()
    array = binary_addition(A, B)
    write_output_file(array)
