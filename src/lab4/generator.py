import random


def gener_test(filename, num_commands, max_value):
    with open(filename, 'w') as file:
        file.write(f"{num_commands}\n")
        for _ in range(num_commands):
            cmd_type = random.choice(['+', '*', '-'])
            if cmd_type in ['+', '*']:
                value = random.randint(1, max_value)
                file.write(f"{cmd_type} {value}\n")
            else:
                file.write(f"{cmd_type}\n")


if __name__ == "__main__":
    gener_test('input.txt', 100000, 100000)
