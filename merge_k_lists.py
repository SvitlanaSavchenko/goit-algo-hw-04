import heapq

def merge_k_lists(lists):
    # Створюємо мін-кучу
    min_heap = []
    
    # Ініціалізуємо мін-кучу з перших елементів кожного списку
    for i, sorted_list in enumerate(lists):
        if sorted_list:  # перевіряємо, що список не порожній
            heapq.heappush(min_heap, (sorted_list[0], i, 0))  # (значення, індекс списку, індекс елемента в списку)

    merged_list = []
    
    # Поки купа не порожня, виймаємо мінімальний елемент і додаємо наступний елемент з того ж списку
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        
        # Якщо в списку є ще елементи, додаємо наступний елемент до купи
        if element_idx + 1 < len(lists[list_idx]):
            next_element = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_element, list_idx, element_idx + 1))
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
