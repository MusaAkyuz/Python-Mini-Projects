
alphabet = ["bcdfghjklmnprstvyzx"]

str1 = input(str("Mesaj : ")).lower()
uniqueStr1 = set(str1)
dictionary = {}

for item in str1:
    dictionary[item] = str1.count(item)

print(dictionary)
print(uniqueStr1)