
array = [11, 3, 5, 0, 1, 6, 0, 1]

def selection_sort(arr):

    # Создаем копию, чтобы не ломать исходный список при удалении
    source = arr.copy()
    sort_arr = []

    # Проходим столько раз, сколько элементов в исходном массиве
    for i in range(len(arr)):
        # Защита от пустого списка
        if not source:
            break

        # 1. Сбрасываем минимум для текущего прохода
        smallest_elem = arr[0]
        smallest_idx = 0

        # 2. Ищем реальный минимум во всем оставшемся списке
        for j in range(1, len(source)):
            if smallest_elem > source[j]:
                smallest_elem = source[j]
                smallest_idx = j

        # 3. ТОЛЬКО ТЕПЕРЬ (после поиска) добавляем минимальный элемент в отсортированный список
        sort_arr.append(source.pop(smallest_idx))

    return sort_arr

if __name__ == '__main__':

    print(selection_sort(array))
