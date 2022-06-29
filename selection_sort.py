# Selection sort works based on the finding the smallest number and adding into an new array.


from smallest_number import smallest_number


arr = [9, 6, 4, 10, 5, 3, 2, 1]

new_arr = []

for s in range(0, len(arr)):
    s_num = smallest_number(arr)
    new_arr.append(s_num)
    arr.pop(arr.index(s_num))

print(new_arr)

