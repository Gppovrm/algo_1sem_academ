def linear_search(A, V):
    indices = [i for i, x in enumerate(A) if x == V]
    if indices:
        return len(indices), indices
    else:
        return -1

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        A = list(map(int, file.readline().strip().split()))
        V = int(file.readline().strip())


    result = linear_search(A, V)

    with open('output.txt', 'w') as file:
        if result == -1:
            file.write(str(result))
        else:
            file.write(f"{result[0]}\n")
            file.write(','.join(map(str, result[1])) + '\n')




# ПОИСК СВИНЬИ :)
# def linear_search(words, target):
#     indices = [i for i, word in enumerate(words) if word == target]
#     if indices:
#         return len(indices), indices
#     else:
#         return -1
#
#
# def add_word_to_dictionary(words, new_word):
#     words.append(new_word)
#     return words
#
#
# if __name__ == "__main__":
#     with open('input.txt', 'r', encoding='utf-8') as file:
#         words = file.readline().strip().split()
#         target = file.readline().strip()
#
#     result = linear_search(words, target)
#
#     with open('output.txt', 'w', encoding='utf-8') as file:
#         if result == -1:
#             file.write(str(result))
#         else:
#             file.write(f"{result[0]}\n")
#             file.write(','.join(map(str, result[1])) + '\n')
#
#     new_word = "Пеликан"
#     updated_words = add_word_to_dictionary(words, new_word)

