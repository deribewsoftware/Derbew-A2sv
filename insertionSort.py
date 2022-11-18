#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort(arr):
 num=len(arr)
 for i in range(1,num):
   key=arr[num-1]
   j=num-2
   while j>=0 and key<arr[j]:
     arr[j+1] =arr[j]
     j-=1
     for i in range(len(arr)):
      print(arr[i],end=" ")
     
     
     print()
   else:
     arr[j+1]=key
     for i in range(len(arr)):
        print(arr[i],end=" ")
     break
     
     
insertionSort([2,4,6,8,3])
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    #insertionSort1(n, arr)
     
