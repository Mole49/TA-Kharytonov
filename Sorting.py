def linear_search(arr, x):
    k = 0
    for i in range(len(arr)):
        k += 1
        if arr[i] == x:
            print("Лінійний пошук: знайдено", x, "на позиції", i, "кількість дій:", k)
            return i
    print("Лінійний пошук: елемент", x, "не знайдено, кількість дій:", k)
    return -1

def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    k = 0
    while l <= r:
        k += 1
        m = (l + r) // 2
        if arr[m] == x:
            print("Двійковий пошук: знайдено", x, "на позиції", m, "кількість дій:", k)
            return m
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    print("Двійковий пошук: елемент", x, "не знайдено, кількість дій:", k)
    return -1

def bubble_sort(arr):
    n = len(arr)
    k = 0
    print("\nСортування бульбашкою:")
    for i in range(n):
        for j in range(0, n - i - 1):
            k += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("Після", i + 1, "ітерації:", arr, "дій:", k)
    return arr

def quick_sort(arr, k=[0]):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    left, mid, right = [], [], []
    for el in arr:
        k[0] += 1
        if el < p:
            left.append(el)
        elif el == p:
            mid.append(el)
        else:
            right.append(el)
    print("pivot =", p, "left =", left, "mid =", mid, "right =", right, "дій:", k[0])
    return quick_sort(left, k) + mid + quick_sort(right, k)

n = int(input("Введіть кількість елементів масиву: "))
arr = []
for i in range(n):
    el = int(input("Елемент " + str(i + 1) + ": "))
    arr.append(el)

print("Початковий масив:", arr)

x = int(input("Введіть число для пошуку: "))
linear_search(arr, x)

sorted_arr = bubble_sort(arr.copy())
binary_search(sorted_arr, x)

print("\nШвидке сортування:")
qs = quick_sort(arr.copy())
print("Результат швидкого сортування:", qs)

input("\nНатисніть Enter, щоб закрити програму...")
