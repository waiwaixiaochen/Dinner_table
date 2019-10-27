# Dinner_table

Suppose you are given a set of n people (with n even) to be seated at a dinner party. The people will be 
seated along the two sides of a long table. Half are "hosts", half are "guests". The given function r(p) 
identifies the role of a given person. As the host, you also know an integer-valued "preference function" 
h(p1, p2) for a pair of people p1, p2. The preference function indicates how much the first person likes 
the second; it may be negative. 

The "score" of a table is determined by the following criteria:
- 1 point for every adjacent pair (seated next to each other) of people with one a host and the other a guest.
- 2 points for every opposite pair (seated across from each other) of people with one a host and the other a guest.
- h(p1, p2) + h(p2, p1) points for every adjacent or opposite pair of people p1, p2.

As an event organizer is to write a search that will find a "good" table score for a given set of people and preference function.


## Pre-reqs, Setup, and Build

Get prerequisites
- Install Python

Git clone
```shell
$ git clone https://github.com/waiwaixiaochen/Dinner_table.git
```

Run the program
```shell
$ python dinner_party.py
```

## Strategies used

- Step 1: Set the initial seats to be seated according to the people's order, that is, 
          if the seat number is i, then the people is the ith people in the seat
- Step 2: Calculate the score for the table
- Step 3: Swap the people for the first seat with its left seat, or with the opposite seat
- Step 4: Repeat Step 2, compare the scores, keep the record of the seats state with the higher score. 
          Repeat Step 3, move to the next seat
- Step 5: Repeat Step 4, until time(60 seconds) is over, return the highest score along with the seats information

