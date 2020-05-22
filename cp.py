import math
import os
import random
import re
import sys
import copy
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
        if sum(interest[i]) == 0:     # if no one wants the houses (e.g. all potential buyers took other houses), just skip it
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


# recursive solution
def realEstateBroker2(clients, houses):
    interest = [[0]*(len(clients)) for j in range(len(houses))] # construct 2D array
    
    # fill 2D array
    for i in range (len(houses)):
        for j in range (len(clients)):
            if houses[i][0] >= clients[j][0] and houses[i][1] <= clients[j][1]: 
                # if area of house >= client area AND price of house <= client price
                interest[i][j] = 1
              
    interest.sort(key = sum) # house with least potential clients comes first

    # recursive helper function
    def recurse(interest, house_num, max_depth):
        print("depth:", house_num)
        #print("reached at:", house_num)
        # base case
        if house_num >= max_depth:
            return 0

        max_sold = 0
        cur_sold = 0
        # if no one wants the houses (e.g. all potential buyers took other houses), just skip it
        if (sum(interest[house_num]) == 0):
            return recurse(interest, house_num+1, max_depth)    # move on to next house

        for num_client in range (len(clients)):
            if interest[house_num][num_client] == 1:
                # detach edge from all other houses that this client could buy
                new_interest = copy.deepcopy(interest)  # copies inner objects as well
                for other_house in range (len(houses)):
                    if other_house == house_num:
                        continue
                    new_interest[other_house][num_client] = 0
                # now recurse with updated interest adjacency matrix
                cur_sold = recurse(new_interest, house_num+1, max_depth) + 1
                max_sold = cur_sold if cur_sold > max_sold else max_sold    # update sold to largest

        return max_sold

    for i in range (len(interest)):
        print(sum(interest[i]), end = " ")

    # recursive search
    sold = recurse(interest, 0, len(houses)) # start with house 0 (the house with least potential clients)
        
    # if houses > clients and somehow we sold more than we have houses
    sold = len(houses) if sold > len(houses) else sold
    
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

    start = time.perf_counter() # start time
    result = realEstateBroker2(clients, houses)
    stop = time.perf_counter() # stop time

    print(result)

    print("Time: " + str(stop-start))



    # n = int(input())
    ## arr = list(map(int, input().rstrip().split()))

    

    