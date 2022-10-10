
# Insertion Sort
# Algorith Analysis

unsorted = [3, 5, 7, 2, 1, 9]
print(unsorted)

for j in range(1, len(unsorted)):
    print(j)
    key = unsorted[j]
    i = j - 1
    while i >= 0 and unsorted[i] > key:
        unsorted[i + 1] = unsorted[i]
        i -= 1
    unsorted[i + 1] = key

print(unsorted)