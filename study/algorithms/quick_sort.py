import random

def QuickSort(A: list):
    if len(A) <= 1:
        return A
    else:
        pivot = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < pivot:
                L.append(elem)
            elif elem > pivot:
                R.append(elem)
            else:
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)


if __name__ == '__main__':

    some_list = [random.randint(1, 9) for _ in range(10)]

    # [3, 7, 1, 7, 7, 1, 5, 1, 3, 9]
    print(some_list)
    print("*** магия сортировки ***")
    print(QuickSort(some_list))
    # [1, 1, 1, 3, 3, 5, 7, 7, 7, 9]



