import time
import numpy as np

def main():
    noofterms = 10000000
    den = np.linspace(1, noofterms*2, noofterms)
    num = np.ones(noofterms)

    for i in range(1, noofterms):
        num[i] = pow(-1, i)

    counter = 0
    sumValue = 0

    t1 = time.process_time()
    while counter < noofterms:
        sumValue += (num[counter] / den[counter])
        counter += 1

    piValue = sumValue * 4.0
    print("pi value is : %f" % piValue)

    t2 = time.process_time()
    timeTaken = t2 - t1
    print("Time take is : %f seconds" % timeTaken)



if __name__ == '__main__':
    main()
