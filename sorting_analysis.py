import random
import timeit
from tabulate import tabulate

# Реалізація алгоритму сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Рекурсивний виклик сортування для лівої і правої частини
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Злиття двох половинок
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Перевірка залишків
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація алгоритму сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для генерації тестових даних
def generate_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reversed":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Unsupported data type: choose 'random', 'sorted', or 'reversed'")

# Функція для вимірювання часу виконання алгоритму сортування
def time_sorting_algorithm(algorithm, data):
    start_time = timeit.default_timer()
    algorithm(data)
    end_time = timeit.default_timer()
    return end_time - start_time

# Основна функція для тестування алгоритмів
def test_algorithms():
    sizes = [100, 1000, 10000]
    data_types = ["random", "sorted", "reversed"]
    results = []

    for size in sizes:
        for data_type in data_types:
            data = generate_data(size, data_type)

            # Копіюємо дані для кожного алгоритму, щоб забезпечити однакові умови
            data_for_merge_sort = data.copy()
            data_for_insertion_sort = data.copy()
            data_for_timsort = data.copy()

            # Вимірюємо час виконання кожного алгоритму
            try:
                merge_sort_time = time_sorting_algorithm(merge_sort, data_for_merge_sort)
            except Exception as e:
                merge_sort_time = f"Error: {e}"

            try:
                insertion_sort_time = time_sorting_algorithm(insertion_sort, data_for_insertion_sort)
            except Exception as e:
                insertion_sort_time = f"Error: {e}"

            try:
                timsort_time = time_sorting_algorithm(sorted, data_for_timsort)
            except Exception as e:
                timsort_time = f"Error: {e}"

            results.append((size, data_type, merge_sort_time, insertion_sort_time, timsort_time))

    return results

# Функція для аналізу і виведення результатів у вигляді таблиці
def analyze_results(results):
    # Додаємо заголовки стовпців для таблиці
    headers = ["Size", "Data Type", "Merge Sort (s)", "Insertion Sort (s)", "Timsort (s)"]
    # Форматуємо таблицю з використанням tabulate
    table = tabulate(results, headers=headers, tablefmt="grid", floatfmt=".6f")
    print(table)

# Запуск тестування та аналіз результатів
results = test_algorithms()
analyze_results(results)
