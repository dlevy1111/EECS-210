'''
Name of Program: Assignment 7
Description: This program shows (and completes) my understanding of permutations and combinations
Inputs: None
Outputs: Text
Author: David Levy
Creation Date: Apr. 4, 2023
'''

def fac(num): # simple recursive factorial function
    if num == 1 or num == 0:
        return 1
    return num*fac(num-1) # pretty chill

def C(n, r): # combinations function
    return fac(n)/(fac(n-r)*fac(r)) # works just like the one from lecture

def stlng(n, j): # function for computing the stirling number of the second kind
    sum = 0
    for i in range(0,j+1): # looping = summation
        sum += ((pow((-1),i))*C(j,i)*(pow((j-i),n))) # operation just like in the slides
    return sum/(fac(j)) # return your sum/j!

def dist_obj_in_dist_boxes(n_objects, j_items_per_box, k_boxes): # distinguishable objects --> distinguishable boxes 
    prod = 1 # dummy variable for returning 
    for i in range(0, k_boxes): # loop through boxes
        prod = prod*C(n_objects-j_items_per_box*i, j_items_per_box) # multiply combinations along the way
    return prod # then return

def ind_obj_in_dis_boxes(n_objects, k_boxes): # indistinguishable objects --> distinguishable boxes
    return C(n_objects+k_boxes-1, n_objects)

def dist_obj_in_ind_boxes(n_items, k_boxes): # distinguishable objects --> indistinguishable boxes
    sum = 0
    for i in range(1, k_boxes+1):
        sum += stlng(n_items, i)
    return sum

def _rec_partition(n_objects, k_boxes):
    # since partition is recursive, we need to handle base cases:
    if k_boxes == 1 or n_objects == 0:
        return 1
    elif k_boxes > n_objects: # more base cases
        return _rec_partition(n_objects, n_objects)
    # using recurrence relation for partition function found on internet
    else:
        return _rec_partition(n_objects - k_boxes, k_boxes) + _rec_partition(n_objects, k_boxes - 1)

def ind_obj_in_ind_boxes(n_objects, k_boxes): # indistinguishable objects --> indistinguishable boxes
    # using a pre-defined recursive wrapping function
   return _rec_partition(n_objects, k_boxes)

def main(): # main function that actually deals with the output
    for i in range(0,4):
        print(f"{i+1})")
        if i == 0: # distinguishable items into distinguishable boxes
            print("a)")
            print("How many ways are there to deal 5-card poker hands from a 52-card deck to each of 4 players?")
            print(dist_obj_in_dist_boxes(52, 5, 4))
            print("b)")
            print("A professor packs her collection of 40 issues of a mathematics journal in four boxes with 10 issues per box. How many ways can she distribute the journals if each box is numbered, so that they are distinguishable?")
            print(dist_obj_in_dist_boxes(40, 10, 4))
        elif i == 1: # indistinguishable items into distinguishable boxes
            print("a)")
            print("How many ways are there to place 10 indistinguishable balls into 8 distinguishable bins?")
            print(ind_obj_in_dis_boxes(10, 8))
            print("b)")
            print("How many ways are there to distribute 12 indistinguishable balls into six distinguishable bins?")
            print(ind_obj_in_dis_boxes(12,6))
        elif i == 2: # distinguishable items into indistinguishable boxes
            print("a)")
            print("How many ways can Anna, Billy, Carson, and Danny be placed into 3 indistinguishable homerooms?")
            print(dist_obj_in_ind_boxes(4,3))
            print("b)")
            print("How many ways are there to put five temporary employees into four identical offices?")
            print(dist_obj_in_ind_boxes(5,4))
        elif i == 3: # indistinguishable items into indistinguishable boxes
            print("a)")
            print("There are 9 ways to pack six copies of the same book into four identical boxes")
            print(ind_obj_in_ind_boxes(6,4))
            print("b)")
            print("How many ways are there to distribute five indistinguishable objects into three indistinguishable boxes?")
            print(ind_obj_in_ind_boxes(5,3))

main()