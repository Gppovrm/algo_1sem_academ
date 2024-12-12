def stackk(file):
    stack = []
    results = []

    for line in file:
        c = line.strip()
        if c == '-':
            results.append(stack.pop())
        else:
            stack.append(int(c.split()[1]))

    return results


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        m = int(file.readline().strip())
        results = stackk(file)

    with open('output.txt', 'w') as file:
        for result in results:
            file.write(str(result) + '\n')
