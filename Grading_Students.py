#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    
    gradeOutput=[]

    for i in grades:
        if i < 38:
            gradeOutput.append(i)
        else:
            GradeDifference=5-(i%5)
            if GradeDifference >=0 and GradeDifference <3:
                gradeOutput.append(i+GradeDifference)
            else:
                gradeOutput.append(i)
    return gradeOutput


    
      
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
