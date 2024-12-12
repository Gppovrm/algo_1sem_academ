from random import randint


def partition(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def random_qs(a, l, r):
    if l < r:
        k = randint(l, r)
        a[l], a[k] = a[k], a[l]
        m = partition(a, l, r)
        random_qs(a, l, m - 1)
        random_qs(a, m + 1, r)


with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    a = list(map(int, file.readline().strip().split()))

random_qs(a, 0, n - 1)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, a)))
