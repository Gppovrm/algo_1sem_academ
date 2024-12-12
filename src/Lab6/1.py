# def my_set(operations):
#     my_set = set()
#     results = []
#
#     for operation in operations:
#         splited = operation.split()
#         op_type = splited[0]
#         key = int(splited[1])
#
#         if op_type == 'A':
#             my_set.add(key)
#         elif op_type == 'D':
#             my_set.discard(key)
#         elif op_type == '?':
#             if key in my_set:
#                 results.append('Y')
#             else:
#                 results.append('N')
#     return results
#
#
# if __name__ == "__main__":
#     with open('input.txt', 'r') as input_file:
#         n = int(input_file.readline().strip())
#         operations = [input_file.readline().strip() for _ in range(n)]
#         print(operations)
#     ans = my_set(operations)
#     with open('output.txt', 'w') as output_file:
#         output_file.write("\n".join(ans))
class HashTable:
    def __init__(self):
        self.table = set()

    def add_key(self, key):
        self.table.add(key)

    def remove_key(self, key):
        self.table.discard(key)

    def check_key(self, key):
        return key in self.table

def my_set(operations):
    hash_table = HashTable()
    results = []

    for operation in operations:
        splited = operation.split()
        op_type = splited[0]
        key = int(splited[1])

        if op_type == 'A':
            hash_table.add_key(key)
        elif op_type == 'D':
            hash_table.remove_key(key)
        elif op_type == '?':
            if hash_table.check_key(key):
                results.append('Y')
            else:
                results.append('N')
    return results

if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        n = int(input_file.readline().strip())
        operations = [input_file.readline().strip() for _ in range(n)]
    ans = my_set(operations)
    with open('output.txt', 'w') as output_file:
        output_file.write("\n".join(ans) + "\n")
