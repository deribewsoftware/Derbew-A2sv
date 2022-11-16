#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
def countSwaps(a):
  num=len(a)
  swaps=0
  for i in range(num):
    for j in range(num-1):
      if a[j+1]<=a[j]:
        a[j],a[j+1]=a[j+1],a[j]
        swaps += 1
  #return "Array is sorted in " +swaps+" swaps.\nFirst Element: "
  for i in range(num):
    if i==0:
      b=i
  return  "Array is sorted in " +str(swaps)+" swaps.\nFirst Element: "+str(a[b])+"\nLast Element: "+str(a[num-1])




 
    

                
if __name__ == '__main__':
    n=int(input().strip())
    a=list(map(int,input().rstrip().split()))
    print(countSwaps([4, 2, 1, 3]))


   


         
    # Write your code here

