#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

'''
Mission
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Input Format

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .

Output Format

Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros

Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Sample Output

0.500000
0.333333
0.166667
'''

def plusMinus(arr):
    # Write your code here
    negNum = 0
    posNum = 0
    zeroNum = 0
    
    for item in arr:
        if item > 0:
            posNum += 1
        elif item < 0:
            negNum += 1
        else:
            zeroNum += 1
        
    lengthArr = len(arr)
    print(posNum / lengthArr)    
    print(negNum / lengthArr)
    print(zeroNum / lengthArr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
