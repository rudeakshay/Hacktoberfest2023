def selection_sort(arr):
    """
    Sorts a list in ascending order using the Selection Sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(unsorted_list)
print("Sorted list:", unsorted_list)
