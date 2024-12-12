def brackets(s):
    stack = []

    for char in s:
        if char in '([':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return "NO"
        elif char == ']':
            if not stack or stack.pop() != '[':
                return "NO"

    return "YES" if not stack else "NO"


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        results = []
        for line in file:
            results.append(brackets(line.strip()))

    with open('output.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')
