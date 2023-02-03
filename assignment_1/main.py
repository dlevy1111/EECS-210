'''
Name: EECS 210 Assignment 1
Description: Shows understanding of programming and propositional logic
Inputs: none
Outputs: text
My name: David Levy
Creation date: Jan 15
'''

def main():
    p = [True, True, True, True, False, False, False, False] # setup 
    q = [True, True, False, False, True, True, False, False]
    r = [True, False, True, False, True, False, True, False]
    # negation = NOT p, NOT q = not p, not q
    # conjunction = p AND q = p and q
    # disjunction = p OR q = p or q
    # implication = NOT p OR q = (not p) or q = imp(p, q)
    # bicondition = NOT p XOR q = (p and q) or ((not p) and (not q)) = not (p ^ q)

    looping = True
    choice = 1
    while looping: # in this section we print the tables
        a = [] # output 1
        b = [] # output 2
        # we're always checking whether a = b, so we need to calculate both for each case
        
        # print("1) DeMorgan's first law\n2) DeMorgan's second law\n3) First associative law\n4) Second associative law\n5) [(p + q) * (p -> r) * (q -> r)] -> r ≡ T\n6) p <-> q ≡ (p -> q) * (q -> p)\n7) Stop\n")
        # choice = int(input("What would you like to do? "))
        print()

        printing_object = [["p", "q", "r"]]

        if choice == 1: # logic for DeMorgan's first law
            for i in range(0,len(p)): # i = index
                a.append( not ( q[i] and r[i] ) ) # using q and r here because lists p and q are incorrectly similar and q and r are the correct lists to be used here.
                b.append( ( not q[i] ) or ( not r[i] ) )
            printing_object[0].append("!(q * r)")
            printing_object[0].append("!q + !r")
        
        if choice == 2: # logic for DeMorgan's second law
            for i in range(0,len(p)):
                a.append( not ( q[i] or r[i] ) ) # same note as choice 1 about q and r
                b.append( ( not q[i] ) and ( not r[i] ) )
            printing_object[0].append("!(q + r)")
            printing_object[0].append("!q * !r")
        
        if choice == 3: # logic for first associative law
            for i in range(0,len(p)):
                a.append( ( p[i] and q[i] ) and r[i] )
                b.append( p[i] and ( q[i] and r[i] ) )
            printing_object[0].append("(p * q) * r")
            printing_object[0].append("p * (q * r")
        
        if choice == 4: # logic for second associative law
            for i in range(0,len(p)):
                a.append( ( p[i] or q[i] ) or r[i] )
                b.append( p[i] or ( q[i] or r[i] ) )
            printing_object[0].append("(p + q) + r")
            printing_object[0].append("p + (q + r)")
        
        if choice == 5: # logic for [(p + q) * (p -> r) * (q -> r)] -> r ≡ T
            for i in range(0,len(p)):
                a.append( imp( ( ( p[i] or q[i] ) and imp( p[i], r[i] ) and ( imp( q[i], r[i] ) ) ), r[i] ) )
                b.append( True )
            printing_object[0].append("[(p + q) * (p -> r) * (q -> r)] -> r")
            printing_object[0].append("T")
        
        if choice == 6: # logic for q <-> r ≡ (q -> r) * (r -> q)
            for i in range(0,len(p)):
                a.append( bic( q[i], r[i] ) ) # same note as choice 1
                b.append( ( imp( q[i] , r[i] ) and imp( r[i], q[i]) ) )
            printing_object[0].append("q <-> r")
            printing_object[0].append("(q -> r) * (r -> q)")
        
        if choice == 7: # exit case
            print("Goodbye")
            looping = False
            break
        
        print(choice)
        for i in range(0, 8): # rows of printing_object (starts at 1 since we have the first row of stuff)
            printing_object.append([p[i], q[i], r[i], a[i], b[i]])
        
        for row in range(0, len(printing_object)):
            for col in range(0, len(printing_object[0])):
                print(printing_object[row][col], end="\t")
            print()
        print()

        choice = choice + 1


def imp(p, q):
    return ((not p) or q)

def bic(p, q):
    return not (p ^ q)

main()
