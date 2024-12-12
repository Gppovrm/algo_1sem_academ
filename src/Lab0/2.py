with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    n = int(input_file.read())
    fibonacci = [0, 1]
    for i in range(2, n + 1):
        fibonacci.append((fibonacci[-1] + fibonacci[-2]))

    output_file.write(str(fibonacci[n]))
