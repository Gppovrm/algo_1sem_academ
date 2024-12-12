with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                  encoding='utf-8') as output_file:
    a, b = map(int, input_file.read().split())
    output_file.write(str(a + b))

# задание 2 в задаче 1
with open('input2.txt', 'r', encoding='utf-8') as input_file, open('output2.txt', 'w',
                                                                  encoding='utf-8') as output_file:
    a, b = map(int, input_file.read().split())
    output_file.write(str(a + b ** 2))
