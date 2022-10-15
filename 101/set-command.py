

str1 = input(str("Mesajinizi giriniz :")).lower()
unique = set(str1)
uniqueList = list(unique)

print(str1)
print(unique)
print(uniqueList)

freq = {}
for item in uniqueList:
    freq[item] = str1.count(item)

freqKeys = list(freq.keys())
freqValues = list(freq.values())
print(freq)
print(freqKeys)
print(freqValues)