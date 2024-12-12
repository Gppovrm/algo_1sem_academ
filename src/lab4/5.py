class stack_w_max:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            if value == self.max_stack[-1]:
                self.max_stack.pop()
            return value

    def max(self):
        if self.max_stack:
            return self.max_stack[-1]

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        stack = stack_w_max()
        results = []

        for _ in range(n):
            command = file.readline().strip().split()
            if command[0] == "push":
                stack.push(int(command[1]))
            elif command[0] == "pop":
                stack.pop()
            elif command[0] == "max":
                results.append(stack.max())

    with open('output.txt', 'w') as file:
        for result in results:
            file.write(str(result) + '\n')
