"""
Jennifer Larsen
10/17/2023
This program is to sort and search arrays.
"""
import array as arr


def sort_array(arr):
    arr.sort()


"""There is no return statement as the original list is sorted."""


def search_array(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1


def main():
    my_array = [8, 3, 1, 6, 2, 7, 4, 5]
    print("My Array:", my_array)

    # Sort the list using the sort_array function
    sort_array(my_array)

    # Print the sorted list
    print("Sorted Array:", my_array)

    # Define a target value
    target = 3

    # Search for the target value in the sorted list using the search_array function
    index = search_array(my_array, target)

    # Check if the target value was found
    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found in the list.")


if __name__ == "__main__":
    main()
