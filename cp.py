import math
import os
import random
import re
import sys
import time

# Complete the staircase function below.
def staircase(n):
    stair = ''
    for i in range (n):
        stair += (' '*(n-i-1))  
        stair += ('#'*(i+1))
        print(stair)
        stair = ''

def miniMaxSum(arr):
    arr.sort()
    length = len(arr)
    max_sum = 0
    min_sum = 0
    for i in range (0, 4):
        min_sum += arr[i]
        max_sum += arr[length-i-1]
    print(min_sum, max_sum)


def birthdayCakeCandles(ar):
    tall = -1
    count = 0
    for i in ar:
        if i == tall:
            count += 1
        if i > tall:
            tall = i
            count = 1
        
    return count


def timeConversion(s):
    time = list(map(str, s.strip().split(':')))
    noon = (time[len(time)-1])[-2:]
    
    if noon == "AM":
        if int(time[0]) == 12:
            return '00' + s[2:-2]
        return s[:-2]
    else:
        if int(time[0]) == 12:
            return s[:-2]
        return str(int(time[0]) + 12) + s[2:-2]
    return noon


def realEstateBroker(clients, houses):
    interest = [[0]*(len(clients)) for j in range(len(houses))] # construct 2D array
    
    # fill 2D array
    for i in range (len(houses)):
        for j in range (len(clients)):
            if houses[i][0] >= clients[j][0] and houses[i][1] <= clients[j][1]: 
                # if area of house >= client area AND price of house <= client price
                interest[i][j] = 1
              
    interest.sort(key = sum) # house with least potential clients comes first

    #for i in range (len(interest)):
        #print(sum(interest[i]), end = " ")

    # traversal to find maximum
    sold = 0
    for i in range (len(houses)):
        if sum(houses[i]) == 0:     # if no one wants the houses (e.g. all potential buyers took other houses), just skip it
            continue
        for j in range (len(clients)):
            if interest[i][j] == 1:
                sold += 1
                # clean up option for all others
                for k in range (len(houses)):
                    if k == i:
                        continue
                    interest[k][j] = 0
                # clean up self
                for m in range (len(clients)):
                    if j == m:
                        continue
                    interest[i][m] = 0
                #print(i, end = " ")
                break    # stop searching 

    #print(interest)
    return sold



if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    clients = []

    for _ in range(n):
        clients.append(list(map(int, input().rstrip().split())))

    houses = []

    for _ in range(m):
        houses.append(list(map(int, input().rstrip().split())))

    result = realEstateBroker(clients, houses)

    print(result)




    # n = int(input())
    ## arr = list(map(int, input().rstrip().split()))

    #start = time.perf_counter() # start time
    #stop = time.perf_counter() # stop time

    #print("Time: " + str(stop-start))