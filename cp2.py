import math
import os
import random
import re
import sys
import time

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    pos1 = x1 if v1 > v2 else x2
    pos2 = x2 if v1 > v2 else x1
    
    while pos1 <= pos2:
        if pos1 == pos2:
            return "YES"
        pos1 += v1 if v1 > v2 else v2
        pos2 += v2 if v1 > v2 else v1
    
    return "NO"

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print (result)

    # ------------------- test 1 -------------------
    #start = time.perf_counter() # start time
        
    #stop = time.perf_counter() # stop time


    #print("Time: " + str(stop-start))
    #print("Time: " + str(stop2-start2))

