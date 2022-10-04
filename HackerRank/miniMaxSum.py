#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

'''
Mission
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input
1 2 3 4 5

Sample Output
10 14
'''

def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    
    maxSum = 0
    for item in arr[1:]:
        maxSum += item

    minSum = maxSum - arr[len(arr) - 1] + arr[0]
    
    print(str(minSum) + " " + str(maxSum))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
