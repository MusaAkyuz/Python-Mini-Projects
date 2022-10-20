
# Just vovels
fileD = open("text.txt", encoding="utf8")
deleting = ["a", "e", "ı", "i", "o", "ö", "ü", "u", "?", "!", ".", ","]
my_alphabet = []

for line in fileD:
    line = list(line)
    for letter in line:
        if letter not in deleting:
            my_alphabet.append(letter)

print(my_alphabet)

    

