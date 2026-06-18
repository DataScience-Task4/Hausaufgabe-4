import matplotlib.pyplot as plt


def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.bar(range(len(my_list)), my_list, color="steelblue")
ax1.set_title("Unsortiert")
ax1.set_xlabel("Index")
ax1.set_ylabel("Wert")

mergeSort(my_list)

ax2.bar(range(len(my_list)), my_list, color="seagreen")
ax2.set_title("Sortiert")
ax2.set_xlabel("Index")
ax2.set_ylabel("Wert")

plt.suptitle("Mergesort Algorithmus – Vorher und Nachher")
plt.tight_layout()
plt.show()
