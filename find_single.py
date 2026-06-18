def find_single(arr):
    """Find the single element that appears exactly once in the array.

    All other elements appear exactly twice. Uses XOR: a ^ a = 0 and a ^ 0 = a,
    so duplicate elements cancel out, leaving only the unique element.

    Time complexity: O(n). Space complexity: O(1).

    Args:
        arr: List of integers with odd length where every element except one
             appears exactly twice.

    Returns:
        The single element that appears exactly once.

    Raises:
        TypeError: If arr is not a list.
        ValueError: If arr is empty or has even length.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if len(arr) == 0:
        raise ValueError("List must not be empty.")
    if len(arr) % 2 == 0:
        raise ValueError("List must have odd length.")

    result = 0
    for num in arr:
        result ^= num
    return result
