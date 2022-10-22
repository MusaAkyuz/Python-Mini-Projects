
# Just not vovels

# keeps all words from input like file or string
allWords = []
filteredAllWords = []

# for the filtering text
filtersWord = ["a", "e", "ı", "i", "u", "ü", "o", "ö", " ", "?", "!", ",", ".", "\"", "-", "“", "v", "\n"]

# alltext line by line
allText = []

# unique all wrods
unique = []
filteredUnique = []

with open("text.txt", encoding="utf-8") as file:
    allText = file.readlines()

with open("text.txt", encoding="utf-8") as file:
    while True:
        char = file.read(1)
        
        # checking the EOF (End Of File) to quit from loop
        if not char:
            break

        allWords.append(char.lower())
        # filtering words
        if char not in filtersWord:
            filteredAllWords.append(char.lower())


unique = set(allWords)
filteredUnique = set(filteredAllWords)
print(unique)
