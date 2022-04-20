#create a list
a_list = [1,3,5,7,9]

sum_of_list = a_list[0] + a_list[1] + a_list[2] + a_list[3] + a_list[4]

print(sum_of_list)
print(sum_of_list / 5)

sum_of_b = 0
b_list = [1, 3, 5, 7, 9,11]
for numba in b_list:
    sum_of_b = sum_of_b + numba

print(sum_of_b)
print(sum_of_b / len(b_list))
b_list.append(13)
for numba in b_list:
    sum_of_b = sum_of_b + numba

print(sum_of_b)
print(sum_of_b / len(b_list))

print(b_list[len(b_list)-1])

print(b_list[-1])
