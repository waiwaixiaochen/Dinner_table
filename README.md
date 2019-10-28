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

## Strategy used 

Local search algorithm was used in this program. The people's seat were swapped with its left or opposite seat. Compare the scores after each swap and record the higher one.



