s = "abcdefghjklmn"

print(s[1])  # b
print(s[1:5])  # bcde
print(len(s))  # 13

for item in s:
    print(item, end="")  # abcdefghjklmn

print("\n")

st = "somewordstocheck"
list_st = list(st)
list_st = list_st.sort()
print(list_st)
if "som" in st:
    print("\nYeah it is in the st")
