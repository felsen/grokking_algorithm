# Apply the binary search algorithm, after sorting the list, otherwise it won't work.
# using Divide and Conquer technique
# O(n) - n is number of operations.

def linear_search(my_list, item):

    """ Linear Search Algorithm, it takes longer time to search the number.
    O(n) in linear time.
    """

    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = low + high
        guess = my_list[mid]

        print(f"Linear Search: {guess}")

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1

        if guess < item:
            low = mid + 1

    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Position: {linear_search(my_list, 1)}")


print("----------------------------------------")


def binary_search(my_list, item):

    """ Binary Search algorithm, it takes shorter time to search the elements from the list.
    It finds the middle number and splits the list into two parts and search the elements so it takes very shorter time.
    O log(n) - in Logarithmic Time.
    """

    my_list = sorted(my_list)

    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = my_list[mid]

        print(f"Binary Search: {guess}")

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = list(range(0, 101))
print(f"Position: {binary_search(my_list, 0)}")

print("--------------------------------")

print("Some common big O notation.")
print(" O(n) is the linear time, simple search algorithm.")
print(" O(log n) is the log time, binary search algorithm.")
print(" O(n * log n) is the fast searching algorithm, Ex: quick sort.")
print(" O(n**2) is the slow sort algorithm. Ex: selection sort algorithm.")
print(" O(n!) really slow sort algorithm.")

