import argparse
import functools
import heapq
import random
import numpy as np

from collections import deque
from copy import copy, deepcopy

class tableSeats(object):

    # Create table seats
    def __init__(self, n, people_list):
        # Arrange people for the table
        people_list = [i for i in range(1, n+1)]
        random.shuffle(people)

    # Return a list of seats-swapping in the current position
    # The swaps could be: swap with the left side people or the opposite people
    def swaps(self):
        n = self.n
        b = self.people_list[x]
        (i, j) = b
        ms = []
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xi = i + d[0]
            xj = j + d[1]
            if xi >= 0 and xi < n and xj >= 0 and xj < n:
                ms.append(((xi, xj), b))
        return ms

    

#Create a list to store preference matrix
n = 0
preferences = list()
matrix_row = 0

#Read the file 
file_name = "hw1-sample1.txt"
file = open(file_name, 'r')
n = file.readline()
#print(n)
preferences = np.loadtxt(file)
preferences = preferences.astype(int)
#print(preferences[0][1])






