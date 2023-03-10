#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(path,steps):
    
    # Write your code here
    
    
    alltitude=0
    valley=0
    step={"D":-1,"U":1}
    for i in steps:
        alltitude +=step[i]
        if alltitude==0 and i=="U":
            valley+=1
    return valley
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
