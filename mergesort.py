import matplotlib.pyplot as plt


def merge_sort(arr):
    """Sort a list in-place using the merge sort algorithm.

    The algorithm works by recursively dividing the list into two halves,
    sorting each half independently, and then merging the sorted halves
    back together. Time complexity: O(n log n). Space complexity: O(n).

    Args:
        arr: The list to sort in-place.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        left_idx = 0
        right_idx = 0
        i = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                arr[i] = left[left_idx]
                left_idx += 1
            else:
                arr[i] = right[right_idx]
                right_idx += 1
            i += 1

        while left_idx < len(left):
            arr[i] = left[left_idx]
            left_idx += 1
            i += 1

        while right_idx < len(right):
            arr[i] = right[right_idx]
            right_idx += 1
            i += 1


if __name__ == "__main__":
    data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    x = range(len(data))
    plt.plot(x, data)
    plt.title("Before Sorting")
    plt.show()
    merge_sort(data)
    x = range(len(data))
    plt.plot(x, data)
    plt.title("After Sorting")
    plt.show()
