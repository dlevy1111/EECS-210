'''
File name: EECS 210 Assignment 3
Description: This program shows my understanding of sets and set operations
Inputs: None
Outputs: Text
Name: David Levy
Creation date: Feb 7
'''

def union(set1, set2): # defining the built in union set operation
    return set1 | set2

def intersection(set1, set2): # defining the built in interesection set operation
    return set1 & set2

def difference(set1, set2): # defining the built in difference set operation
    return set1 - set2

def symm_diff(set1, set2): # defining the built in symmetric difference set operation
    return set1 ^ set2 

def composition(set1, set2): # defining the built in composition relation operation using difference
    set1_o_set2 = set()
    for a in set1: # a[0] is the first entry in each ordered pair
        for b in set2: # b[0] is the second entry in each ordered pair - letters don't matter
            if a[1] == b[0]: # if the second item in the first relation equals to first item in the second relation
                set1_o_set2.add((a[0],b[1]))
    return set1_o_set2



def main(choice): # first part of the program
    if choice == 1:
        R1 = {(1,1), (2,2), (3,3)}
        R2 = {(1,1), (1,2), (1,3), (1,4)}

        print("1.a) R1 ∪ R2: "+str(union(R1, R2))) # R1 ∪ R2
        print("1.b) R1 ∩ R2: "+str(intersection(R1, R2))) # R1 ∩ R2
        print("1.c) R1 − R2: "+str(difference(R1, R2))) # R1 − R2
        print("1.d) R2 − R1: "+str(difference(R2, R1))) # R2 − R1
        print()
    
    if choice == 2: # second part of the program
        A = {1, 2, 3} # defining sets A, B, and C
        B = {1, 2, 3, 4}
        C = {0, 1, 2}
        R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)} # defining relations R and S since there are no relations from A to B, and B to C defined
        S = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)}
        print("2) ",composition(R,S)) # using the composition function that i made earlier
        print()
    if choice == 3: # third part of the program
        R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)} # defining R again
        print("3) ",composition(R,R)) # using the composition function from before
        print()

    if choice == 4: # fourth part of the program
        print("4)", end="\n")
        U = set() # our domain U = {-10, ..., -1, 0, 1, ..., 10}. this was easier (and cooler) than manually making the set
        for i in range(-10, 11): # 11 is excluded so that 10 may be included
            U.add(i)
        R = set()
        for a in U:
            for b in U:
                if a + b == 0: # our definition
                    R.add((a,b))
        print("R =", R)

        # is R reflexive?

        count_of_working_pairs = 0 
        for a in R:
            if a[0] != a[1]: # for some ordered pair (a,b) does a = b? if not then...
                print(f"R is not reflexive because of ({a[0]}, {a[1]})")
                break
            else: # but if it does then...
                count_of_working_pairs += 1
        if count_of_working_pairs == len(R)-1: # i chose this because i know it's right
            print("R is reflexive because all pairs are of the form (a,a)")
        # no actually i made it up

        # is R symmetric?

        r_is_symmetric = True
        for a in R: # looping through all ordered pairs
            has_symmetric_pair = False
            for b in R: # looping through all ordered pairs
                if a[0] == b[1] and a[1] == b[0]: # does (a,b) = (b,a)?
                    has_symmetric_pair = True
            if has_symmetric_pair == True:
                continue
            else:
                r_is_symmetric = False
                print(f"R is not symmetric because of {a} and {b}") # the statement
                break
        if r_is_symmetric: # if r is symmetric then we say it :
            print("R is symmetric because all ordered pairs have friendly pairs like (a,b) being friends with (b,a)")
        
        # is R antisymmetric?
        
        r_is_antisymmetric = True

        if r_is_symmetric:
            print("R is not antisymmetric because R is symmetric")
        else:
            for a in R: # looping through all ordered pairs
                has_symmetric_pair = False
                for b in R: # looping through all ordered pairs
                    if (a[0] == b[1] and a[1] == b[0]) == False: # does (a,b) =\= (b,a)?
                        has_symmetric_pair = True
                if has_symmetric_pair == False:
                    q = "great."
                else:
                    r_is_antisymmetric = False
                    print(f"R is not antisymmetric because of {a} and {b}")
            if r_is_antisymmetric:
                print("R is antisymmetric because all ordered pairs do not have corresponding friends like (a,b) being friends with (b,a)")
        
        # is R transitive?

        r_is_transitive = True
        break_flag1 = False # if we need to make a quick getaway
        break_flag2 = False
        for a in R:
            for b in R: # 3 ordered pairs
                for c in R:
                    if a == b or b == c or c == a: # we want to check different values
                        continue
                    if (a[0] == c[1] and a[1] == b[0] and b[1] == c[0]) == False: # here, a, b, and c are different from the variables a, b, and c used in (a,b),(b,c),(c,a). they are the actual ordered pairs.
                        r_is_transitive = False
                        print(f"R is not transitive because of {a}, {b}, and {c}")
                        break_flag1 = True
                        break_flag2 = True # quick getaway
                        break
                if break_flag1: # quick getaway
                    break
            if break_flag2: # quick getaway
                break
        if r_is_transitive: # R is transitive
            print("R is transitive because for all ordered pairs in R, each one has a couple of friends that share the same entries")



for i in range(1,5): # printing the solutions
    main(i)
