import random

def generate_max_test_data():
    # Максимальные ограничения
    n = 5000
    max_citation = 1000

    # Генерация массива максимальных значений
    citations = [random.randint(0, max_citation) for _ in range(n)]

    # Запись данных в файл input.txt
    with open('input.txt', 'w') as file:
        file.write(','.join(map(str, citations)))

    print("Тестовые данные сгенерированы и сохранены в input.txt")

generate_max_test_data()
