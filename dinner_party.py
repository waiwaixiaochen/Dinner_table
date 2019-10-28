import argparse
import functools
import heapq
import random
import numpy as np

from collections import deque
from copy import copy, deepcopy
import time 


# Create table seats
def create(n):
    # Arrange people for the table
    people_list = [i for i in range(1,n+1)]
    return people_list

# State list
def state(people_list, n):
    state_list = []
    for j in range (0,n):
        if people_list[j] < ((n/2)+1):
            state_list.append(0) # host
        else:
            state_list.append(1) # guest
    return state_list
         

def total_score(people_list, state_list, n, preferences):
    score = 0
    for i in range (0,n):
        if state_list[i] == 0:
            #if (i != ((n/2)-1)) and ((i+1) != (n/2)) and ((i+1)<n) and state_list[i+1] == 0:
            #    adjacent_score = 0
            if (i != ((n/2)-1)) and (i != n-1) and state_list[i+1] == 1:
                adjacent_score = 1
            else:
                adjacent_score = 0
            score += adjacent_score

            
            #if (n/2)+i < n and state_list[int((n/2)+i)] == 0:
            #    opposite_score = 0
            if (n/2)+i < n and state_list[int((n/2)+i)] == 1:
                opposite_score = 2
            else:
                opposite_score = 0
            score += opposite_score
        
        if state_list[i] == 1:
            #if (i != ((n/2)-1)) and ((i+1) != (n/2)-1) and ((i+1)<n) and state_list[i+1] == 1:
            #    adjacent_score = 0
            if (i != ((n/2)-1)) and (i != n-1) and state_list[i+1] == 0:
                adjacent_score = 1
            else:
                adjacent_score = 0
            score += adjacent_score

            #if (n/2)+i < n and state_list[int((n/2)+i)] == 1:
            #    opposite_score = 0
            if (n/2)+i < n and state_list[int((n/2)+i)] == 0:
                opposite_score = 2
            else:
                opposite_score = 0
            score += opposite_score

    for j in range(0,n):
        preference_index_a = people_list[j] - 1
        if n == 2:
            preference_score = preferences[0][1]+preferences[1][0]
        elif j-1 < 0 and j+1 < n/2:
            preference_index_b1 = people_list[j+1] - 1
            preference_index_b2 = people_list[int(n/2 + j)] - 1
            preference_score = preferences[preference_index_a][preference_index_b1] + preferences[preference_index_a][preference_index_b2]
        elif j-1 >= 0 and j+1 < n/2:
            preference_index_b1 = people_list[j+1] - 1
            preference_index_b2 = people_list[int(n/2 + j)] - 1
            preference_index_b3 = people_list[j-1] - 1
            preference_score = preferences[preference_index_a][preference_index_b1] + preferences[preference_index_a][preference_index_b2] + preferences[preference_index_a][preference_index_b3]
        elif j-1 >= 0 and j+1 == n/2:
            preference_index_b2 = people_list[int(n/2 + j)] - 1
            preference_index_b3 = people_list[j-1] - 1
            preference_score = preferences[preference_index_a][preference_index_b2] + preferences[preference_index_a][preference_index_b3]
        elif j == n/2:
            preference_index_b1 = people_list[j+1] - 1
            preference_index_b2 = people_list[int(j-n/2)] - 1
            preference_score = preferences[preference_index_a][preference_index_b1] + preferences[preference_index_a][preference_index_b2]
        elif j > n/2 and j+1 < n:
            preference_index_b1 = people_list[j+1] - 1
            preference_index_b2 = people_list[int(j-n/2)] - 1
            preference_index_b3 = people_list[j-1] - 1
            preference_score = preferences[preference_index_a][preference_index_b1] + preferences[preference_index_a][preference_index_b2] + preferences[preference_index_a][preference_index_b3]
        elif j == n-1:
            preference_index_b2 = people_list[int(j-n/2)] - 1
            preference_index_b3 = people_list[j-1] - 1
            preference_score = preferences[preference_index_a][preference_index_b1] + preferences[preference_index_a][preference_index_b2] + preferences[preference_index_a][preference_index_b3]
        score += preference_score

    return score


# Swap function
def swapPos(p_list, ind1, ind2): 
    p_list[ind1], p_list[ind2] = p_list[ind2], p_list[ind1] 
    return p_list

# Arrange table to get a better score
def swaps(people_list, state_list, n, preferences):
    record = people_list.copy()
    score = total_score(people_list, state_list, n, preferences)
    
    for i in range (0, n):
        for j in range (i+1,n):
            temp_list = people_list.copy()
            temp_list = swapPos(temp_list, i, j)
            temp_state_list = state(temp_list, n)
            #print(temp_list)
            new_score = total_score(temp_list, temp_state_list, n, preferences )
            #print(new_score)
            if new_score > score:
                better_list = temp_list
                score = new_score
                record = better_list
            else: 
                better_list = record
    state_list = state(better_list, n)
            
    return score, better_list, state_list
        
# Arrange table to get a better score-method2
def swaps2(people_list, state_list, n, preferences):
    record = people_list.copy()
    score = total_score(people_list, state_list, n, preferences)
    x  = int(n/2)
    for i in range (0, x):
        for j in range(x, n):
            temp_list = people_list.copy()
            temp_list = swapPos(temp_list, i, j)
            temp_state_list = state(temp_list, n)
            #print(temp_list)
            new_score = total_score(temp_list, temp_state_list, n, preferences )
            #print(new_score)
            if new_score > score:
                better_list = temp_list
                score = new_score
                record = better_list
            else: 
                better_list = record
    state_list = state(better_list, n)
    return score, better_list, state_list



#Create a list to store preference matrix
n = 0
preferences = list()
matrix_row = 0

#Read the file 
file_name = "hw1-inst3.txt"
file = open(file_name, 'r')
n = file.readline()
n = int(n)
#print(n)
preferences = np.loadtxt(file)
preferences = preferences.astype(int)
#print(preferences[0][1])


#Initialize a dinner table with people seating in order
people_list = create(n)
state_list = state(people_list, n)

#Get a better score along with the table arrangement
timeout = 60   # seconds
timeout_start = time.time()
while time.time() < timeout_start + timeout:
    score, people_list, state_list = swaps(people_list, state_list, n, preferences)
    #score, people_list, state_list = swaps2(people_list, state_list, n, preferences)
print(score)
print(people_list)






