# Find the smallest number form the list.


# a = [2, 4, 6, 8, 3, 5, 7, 9, 1]


def smallest_number(my_list):

    """ Assuming that first element is always smallest number from the list and traverse each number from a list,
    and checking the weightage of the number then changing the position of the s_num.
    """

    s_num = my_list[0] # assume smallest number is first number from the list.

    for i in my_list:
        if s_num == i:
            s_num = i
        elif s_num < i:
            pass
        else:
            s_num = i
        # print(f"Each Smallest number: {s_num}")
    return s_num


# print(f"Smallest number from the list is : {smallest_number(a)}")
