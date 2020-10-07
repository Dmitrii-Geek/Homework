my_list = [1, 9, 1, 72, 3, 4, 5, 6, 3]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0]
print(new_list)