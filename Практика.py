import random

def find_sum_of_negatives_between_min_max(arr):
    """
    Находит сумму отрицательных элементов, расположенных между максимальным и минимальным элементами в массиве.

    Args:
        arr (list): Список целых чисел.

    Returns:
        int: Сумма отрицательных элементов между min и max, или 0, если таких элементов нет.
             Возвращает None, если массив пуст или содержит менее двух уникальных элементов.
    """
    if not arr or len(arr) < 2:
        print("Массив слишком короткий или пустой для выполнения операции.")
        return None

    # 1. Находим максимальный и минимальный элементы и их индексы
    max_val = arr[0]
    min_val = arr[0]
    max_idx = 0
    min_idx = 0

    for i, val in enumerate(arr):
        if val > max_val:
            max_val = val
            max_idx = i
        if val < min_val:
            min_val = val
            min_idx = i

    print(f"Массив: {arr}")
    print(f"Максимальный элемент: {max_val} (индекс: {max_idx})")
    print(f"Минимальный элемент: {min_val} (индекс: {min_idx})")

    # Если максимальный и минимальный элементы совпадают по значению и индексу,
    # или если они стоят рядом и между ними нет других элементов.
    if abs(max_idx - min_idx) <= 1:
        print("Максимальный и минимальный элементы находятся рядом, между ними нет других элементов.")
        return 0

    # 2. Определяем диапазон индексов (от меньшего к большему)
    start_index = min(max_idx, min_idx)
    end_index = max(max_idx, min_idx)

    # 3. Суммируем отрицательные элементы в диапазоне
    sum_of_negatives = 0
    # Итерируем от индекса следующего за начальным до индекса, предшествующего конечному
    for i in range(start_index + 1, end_index):
        if arr[i] < 0:
            sum_of_negatives += arr[i]
            print(f"  Найден отрицательный элемент в диапазоне: {arr[i]} (индекс: {i})")

    return sum_of_negatives

# --- Основная часть программы для тестирования ---
if __name__ == "__main__":
    print("--- Тест 1: Случайный массив ---")
    # Генерируем массив случайной размерности (от 10 до 20 элементов)
    N = random.randint(10, 20)
    # Заполняем массив случайными числами (от -50 до 50)
    random_array = [random.randint(-50, 50) for _ in range(N)]
    result = find_sum_of_negatives_between_min_max(random_array)
    if result is not None:
        print(f"Сумма отрицательных элементов между максимальным и минимальным: {result}\n")

    print("--- Тест 2: Максимальный и минимальный элементы рядом ---")
    array_2 = [5, -2, 10, -8, 3, 1, -4, 7]
    result_2 = find_sum_of_negatives_between_min_max(array_2)
    if result_2 is not None:
        print(f"Сумма отрицательных элементов между максимальным и минимальным: {result_2}\n")

    print("--- Тест 3: Отрицательные элементы между min и max ---")
    array_3 = [15, -10, 20, -5, -3, 1, -12, 8]
    result_3 = find_sum_of_negatives_between_min_max(array_3)
    if result_3 is not None:
        print(f"Сумма отрицательных элементов между максимальным и минимальным: {result_3}\n")

    print("--- Тест 4: Нет отрицательных элементов между min и max ---")
    array_4 = [1, 6, 3, 9, 2, 5, 0, 7]
    result_4 = find_sum_of_negatives_between_min_max(array_4)
    if result_4 is not None:
        print(f"Сумма отрицательных элементов между максимальным и минимальным: {result_4}\n")

    print("--- Тест 5: Массив с одним элементом ---")
    array_5 = [42]
    result_5 = find_sum_of_negatives_between_min_max(array_5)
    if result_5 is not None:
        print(f"Сумма отрицательных элементов между максимальным и минимальным: {result_5}\n")

    print("--- Тест 6: Пустой массив ---")
    array_6 = []
    result_6 = find_sum_of_negatives_between_min_max(array_6)
    if result_6 is not None:
        print(f"Сумма отрицательных элементов между максимальным и минимальным: {result_6}\n")

    print("--- Тест 7: Все элементы одинаковые ---")
    array_7 = [7, 7, 7, 7, 7]
    result_7 = find_sum_of_negatives_between_min_max(array_7)
    if result_7 is not None:
        print(f"Сумма отрицательных элементов между максимальным и минимальным: {result_7}\n")
