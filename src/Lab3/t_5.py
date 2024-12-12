def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quicksort(left) + mid + quicksort(right)


def hirsch_i(citations):
    citations = quicksort(citations)
    # citations.sort()
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h


with open('input.txt', 'r') as file:
    citations = list(map(int, file.read().strip().split(',')))

h = hirsch_i(citations)

with open('output.txt', 'w') as file:
    file.write(str(h))
