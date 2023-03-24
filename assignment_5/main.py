'''
Program name: EECS 210 Assignment 5
Description: Demonstrates my understanding of Functions and how they can be described
Inputs: Sets and Functions
Outputs: Text
My Name: David Levy
Creation Date: Mar. 9
'''

# simple function for printing a function and associated sets
def print_functions(A, B, f): 
    print(f"A = {A}") # literally just prints the items out
    print(f"B = {B}")
    print(f"f = {f}")

# Determine if a relation on A and B is a function
def is_function(A, B, f):
    is_function = True
    little_a = [] # all items in f that are also in a
    for item in f:
        little_a.append(item[0]) # organizing all items from a that are in f
    for item in little_a:
        if little_a.count(item) != 1: # each item should only match once
            is_function = False
            break
    if is_function:
        return True
    else:
        return False

# If a relation is a function, then figure out whether it is surjective or injective
# do all items in A correspond to an item in B (through f)?
def is_injective(A, B, f):
    is_injective = True
    lil_a = [] # splitting f into A and B
    lil_b = [] # a list of little a is the same as A (one big a)
    for item in f:
        lil_a.append(item[0])
        lil_b.append(item[1])
    for item in A: # do all items in set A get mapped onto B?
        if item not in lil_a:
            is_injective = False
    for i in B: # are there any duplicate mappings from two items in A onto B?
        if lil_b.count(i) >= 2:
            is_injective = False
    if is_injective: # so? is f injective or what
        return True
    else:
        return False
            
# do all items in B have corresponding items in A and also
# do all items in A get (potentially doubley) mapped to value in b?
def is_surjective(A, B, f):
    is_surjective = True
    lil_b = [] # once again we pull all b values from f
    for item in f:
        lil_b.append(item[1])
    for item in B: # are all items in B present in f?
        if item not in lil_b:
            is_surjective = False
    if is_surjective: # so??? is f surjective???
        return True
    else:
        return False

# Requires that f be bijective (surjective and injective)
def calculate_inverse(A, B, f): # a function for calculating the inverse of a function
    output = {0}
    output.remove(0)
    for item in f:
        output.add((item[1],item[0])) # inverting a function makes it map items from B to A
    return output
    


# If it's both injective and surjective (bijective), find its inverse
def everything(A, B, f): # just one function to take care of everything
    print_functions(A, B, f) # first we print the stuff we have
    if is_function(A, B, f): # first, f needs to be a function
        print("f is a function from A to B")
        if is_injective(A, B, f): # then, we check injectivity
            print("f is injective")
        else:
            print("f is not injective")
        if is_surjective(A, B, f): # after that we check surjectivity
            print("f is surjective") 
        else:
            print("f is not surjective")
        if is_surjective(A, B, f) and is_injective(A, B, f): # if f is both injective and surjective, f is bijective.
            print("f is bijective on A and B")
            print("f has inverse:", calculate_inverse(A, B, f)) # returning the inverse
        else:
            print("f is thus not bijective as well")
    else:
        print("f is not a function from A to B")


def main():
    all_inputs = [ # all inputs from the prompt
        ({'a','b','c','d'}, {'v','w','x','y','z'}, {('a','z'),('b','y'),('c','x'),('d','w')}),
        ({'a','b','c','d'}, {'x','y','z'}, {('a','z'),('b','y'),('c','x'),('d','z')}),
        ({'a','b','c','d'}, {'w','x','y','z'}, {('a','z'),('b','y'),('c','x'),('d','w')}),
        ({'a','b','c','d'}, {1,2,3,4,5}, {('a',4),('b',5),('c',1),('d',3)}),
        ({'a','b','c'}, {1,2,3,4}, {('a',3),('b',4),('c',1)}),
        ({'a','b','c','d'}, {1,2,3}, {('a',2),('b',1),('c',3),('d',2)}),
        ({'a','b','c','d'}, {1,2,3,4}, {('a',4),('b',1),('c',3),('d',2)}),
        ({'a','b','c','d'}, {1,2,3,4}, {('a',2),('b',1),('c',2),('d',3)}),
        ({'a','b','c'}, {1,2,3,4}, {('a',2),('b',1),('a',4),('c',3)})
    ]
    for i in range(0,len(all_inputs)):
        print(str(i+1)+")")
        input_ = all_inputs[i]
        everything(input_[0], input_[1], input_[2])

main()
