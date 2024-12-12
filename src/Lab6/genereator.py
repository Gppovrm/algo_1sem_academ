import random

def generate_max_input(filename):
    N = 10**7
    X = 10**15 - 1
    A = 10**15 - 1
    B = 10**15 - 1
    AC = 999
    BC = 10**15 - 1
    AD = 999
    BD = 10**15 - 1

    with open(filename, 'w') as file:
        file.write(f"{N} {X} {A} {B}\n")
        file.write(f"{AC} {BC} {AD} {BD}\n")

if __name__ == "__main__":
    generate_max_input('input.txt')
