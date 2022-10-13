# learning list in list

lis = [[1,2,3],[4,5,6],[7,8,9]]

print(lis[0])
print(lis[0][0])

# OUTPUT
#--------
#[1, 2, 3]
#1

print(len(lis))
print(len(lis[0]))

# OUTPUT
#--------
#3
#3

# Appending list in list
list1 = [1, 2, 3]
list2 = [4, 5 ,6]

list1.extend(list2)
print(list1)

# OUTPUT
#--------
#[1, 2, 3, 4, 5, 6]

list3 = [7, 8, 9]
list3.append(list2)
print(list3)

# OUTPUT
#--------
#[7, 8, 9, [4, 5, 6]]

