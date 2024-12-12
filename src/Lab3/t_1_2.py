from random import randint


# разбиваем массив на три части
def partition(a, l, r):
    x = a[l]
    m1 = l
    m2 = r
    i = l
    while i <= m2:
        if a[i] < x:
            a[m1], a[i] = a[i], a[m1]
            m1 += 1
            i += 1
        elif a[i] > x:
            a[m2], a[i] = a[i], a[m2]
            m2 -= 1
        else:
            i += 1
    return m1, m2


def random_qs(a, l, r):
    if l < r:
        k = randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition(a, l, r)
        random_qs(a, l, m1 - 1)
        random_qs(a, m2 + 1, r)


with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    a = list(map(int, file.readline().strip().split()))

random_qs(a, 0, n - 1)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, a)))
