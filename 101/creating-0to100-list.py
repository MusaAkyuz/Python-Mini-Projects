import time
liste = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
print(1//2)
s = 0
e = len(liste) - 1
m = ((e - s) // 2) - 1

while True:
    print(liste[m], liste[m - 1])
    m = ((e - s) // 2)

    if liste[m] == True:
        if liste[m - 1] == False:
            print(m)

        e = m

    if liste[m] == False:
        if liste[m + 1] == True:
            print(m + 1)

        s = m

    print(f"middle : {m}, startOfset : {s}, endOfset : {e}")
    time.sleep(1)
            
