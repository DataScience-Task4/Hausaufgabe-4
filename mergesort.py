import matplotlib.pyplot as plt


def merge_sort(items: list[int]) -> None:
    """Sorts a list of integers in ascending order using the Merge Sort algorithm.

    This sorting operation is done in-place.

    Args:
        items: A list of integers to be sorted.
    """
    # Simply check if the list has more than one element (KISS)
    if len(items) > 1:
        midpoint = len(items) // 2
        left_half = items[:midpoint]
        right_half = items[midpoint:]

        # Recursively divide and sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Clear tracking indices 
        left_idx = 0
        right_idx = 0
        merged_idx = 0

        # Merge the temporary halves back into the main items array
        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] <= right_half[right_idx]:
                items[merged_idx] = left_half[left_idx]
                left_idx += 1
            else:
                items[merged_idx] = right_half[right_idx]
                right_idx += 1
            merged_idx += 1

        # Collect any remaining elements from the left subarray
        while left_idx < len(left_half):
            items[merged_idx] = left_half[left_idx]
            left_idx += 1
            merged_idx += 1

        # Collect any remaining elements from the right subarray
        while right_idx < len(right_half):
            items[merged_idx] = right_half[right_idx]
            right_idx += 1
            merged_idx += 1


def plot_list_state(data: list[int], title: str) -> None:
    """Renders a simple line plot showing the values of a list.

    Args:
        data: The dataset sequence to plot.
        title: Title of the visualization.
    """
    indices = range(len(data))
    plt.figure(figsize=(7, 4))
    plt.plot(indices, data, marker="o", linestyle="-", color="royalblue")
    plt.title(title)
    plt.xlabel("Position Index")
    plt.ylabel("Data Value")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    # Reusing plot function to keep the execution stream clean (DRY)
    plot_list_state(my_list, "Array State: Before Merge Sort")

    merge_sort(my_list)

    plot_list_state(my_list, "Array State: After Merge Sort")