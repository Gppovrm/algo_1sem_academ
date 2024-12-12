import random

def generate_random_array(n, filename):
    arr = [random.randint(-10**9, 10**9) for _ in range(n)]
    with open(filename, 'w') as file:
        file.write(f"{n}\n")
        file.write(" ".join(map(str, arr)) + "\n")

if __name__ == "__main__":
    n = 10

    filename = 'input.txt'
    generate_random_array(n, filename)
    print(f"Случайный массив из {n} элементов записан в файл {filename}")
