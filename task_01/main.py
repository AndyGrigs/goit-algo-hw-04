
# Реалізація сортування вставками
def insertion_sort(arr):
    for element in range(1, len(arr)): # Починаємо з другого елемента

        element_to_isert = arr[element] # Ключовий елемент, який потрібно вставити

        element_before = element - 1 # Індекс для попередніх елементів
            # Порівнюємо з попередніми елементами  зміщуємо елементи вправо
        while element_before >= 0 and element_to_isert < arr[element_before]:

            arr[element_before + 1] = arr[element_before] # Зсуваємо елемент вправо

            element_before -= 1 # Переходимо до попереднього елемента

        arr[element_before + 1] = element_to_isert  # Вставляємо ключовий елемент у правильне місце
    return arr


print(insertion_sort([12, 11, 13, 5, 6]))

# Реалізація сортування злиттям