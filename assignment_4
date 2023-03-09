def is_reflexive(set, relation): # is the relation reflexive?
    # print(f"R = {relation}, S = {set}")
    for i in set:
        if (i,i) in relation:
            continue # do we have (i,i) for all items in the relation?
        else: # no? R's not reflexive 
            # print("R is not reflexive") 
            return False
    return True

def make_reflexive(set, relation): # make the relation reflexive
    for i in set:
        relation.add((i,i)) # making R reflexive
    print(f"R* would be {relation}")

def is_symmetric(set, relation): # is the relation symmetric?
   # print(f"R = {relation}, S = {set}")
    for i in relation:
        symmetric = False # pretend we know it's not symmetric for now
        for j in relation:
            if (i[0],i[1]) == (j[1],j[0]):
                symmetric = True # if there ever exists a pair (a,b) (b,a) in the list, we're good. no need to break
                break
        if symmetric == False: # the relation is not symmetric
            # print("R is not symmetric")
            return False
    # print("R is symmetric")
    return True

def is_antisymmetric(set, relation): # is the relation antisymmetric?
    # print(f"R = {relation}, S = {set}")
    for i in relation:
        antisymmetric = True # pretend we know it's not symmetric for now
        for j in relation:
            if i == j:
                antisymmetric = False
            if (i[0],i[1]) == (j[1],j[0]):
                antisymmetric = False # if there ever exists a pair (a,b) (b,a) in the list, we're good. no need to break
        if antisymmetric == False: # the relation is not symmetric
            # print("R is not symmetric")
            return False
    # print("R is symmetric")
    return True

def make_symmetric(set, relation): # make the relation symmetric
    new_relation = relation.copy() # make a copy of the relation
    for i in relation:
        i = (i[1], i[0]) # create R*
        new_relation.add(i)
    print(f"R* would be {new_relation}") # display R*

def is_transitive(set, relation): # is the relation transitive?
    set = list(set)
    set.sort()
    # print(f"R = {relation}, S = {set}")
    for a in set:
        for b in set:
            for c in set:
                if (a,b) in relation and (b,c) in relation and (a,c) not in relation:
                    # print("R is not transitive") # then our relation is not transitive!
                    return False
    return True

def make_transitive(set, relation): # make the relation transitive
    set = list(set)
    set.sort()
    new_relation = []
    row = []
    for i in set:
        for j in set: # making the relation into a matrix
            if (i,j) in relation:
                row.append(1)
            else:
                row.append(0)
        new_relation.append(row)
        row = []

    # warshall's algorithm
    for k in range(0, len(set)):
        for i in range(0, len(set)): # loop through 3 different variables in the relation
            for j in range(0, len(set)):
                    new_relation[i][j] = new_relation[i][j] or (new_relation[i][k] and new_relation[k][j]) # exactly warshall's equation
    closure = {0} # turning new_relation back into a set
    closure.remove(0)
    for i in range(0, len(set)):
        for j in range(0, len(set)):
            if new_relation[i][j] == 1:
                closure.add((set[i],set[j])) # return to set
    print(f"R* would be {closure}")

def is_equivalence_relation(set, relation): # is the relation an equivalence relation?
    # print(f"R = {relation}, S = {set}")
    if not is_reflexive(set, relation):
        return "reflexive"
    if not is_symmetric(set, relation):
        return "symmetric"
    if not is_transitive(set, relation):
        return "transitive"
    return True

def is_poset(set, relation): # are the relation and the set together a poset?
    # print(f"R = {relation}, S = {set}")
    if not is_reflexive(set, relation):
        return "reflexive"
    if not is_antisymmetric(set, relation):
        return "symmetric"
    if not is_transitive(set, relation):
        return "transitive"
    return True



def main(choice): # main
    if choice == 1: # reflexivity
        print("1)")
        print(f"R = {{(1,1), (4,4), (2,2), (3,3)}}, S = {{1,2,3,4}}")
        if is_reflexive({1,2,3,4}, {(1,1), (4,4), (2,2), (3,3)}):
            print("R is reflexive")
        else:
            print("R is not reflexive")
            make_reflexive({1,2,3,4}, {(1,1), (4,4), (2,2), (3,3)})
        print(f"R = {{('a','a'), ('c','c')}}, S = {{'a','b','c','d'}}")
        if is_reflexive({'a','b','c','d'}, {('a','a'), ('c','c')}):
            print("R is reflexive")
        else:
            print("R is not reflexive")
            make_reflexive({'a','b','c','d'}, {('a','a'), ('c','c')})
        print()

    if choice == 2: # symmetry
        print("2)")
        print(f"R = {{(1,2), (4,4), (2,1), (3,3)}}, S = {{1,2,3,4}}")
        if is_symmetric({1,2,3,4}, {(1,2), (4,4), (2,1), (3,3)}):
            print("R is symmetric")
        else:
            print("R is not symmetric")
            make_symmetric({1,2,3,4}, {(1,2), (4,4), (2,1), (3,3)})
        print(f"R = {{(1,2), (3,3)}}, S = {{1,2,3,4}}")
        if is_symmetric({1,2,3,4}, {(1,2), (3,3)}):
            print("R is symmetric")
        else:
            print("R is not symmetric")
            make_symmetric({1,2,3,4}, {(1,2), (3,3)})
        print()
    
    if choice == 3: # transitivity
        print("3)")
        print(f"R = {('a','b'), ('d','d'), ('b','c'), ('a','c')}, S = {{'a','b','c','d'}}")
        if is_transitive({'a','b','c','d'}, {('a','b'), ('d','d'), ('b','c'), ('a','c')}):
            print("R is transitive")
        else:
            print("Ris not transitive")
            is_transitive({'a','b','c','d'}, {('a','b'), ('d','d'), ('b','c'), ('a','c')})
        print(f"R = {{(1,1),(1,3),(2,2),(3,1),(3,2)}}, S = {{1,2,3,4}}")
        if is_transitive({1,2,3,4}, {(1,1),(1,3),(2,2),(3,1),(3,2)}):
            print("R is transitive")
        else:
            print("R is not transitive")
            make_transitive({1,2,3,4}, {(1,1),(1,3),(2,2),(3,1),(3,2)})
        print()
    
    if choice == 4: # equilvalence relation?
        print("4)")
        print(f"R = {{(1,1),(2,2),(2,3)}}, S = {{1,2,3}}")
        what_happened = is_equivalence_relation({1,2,3}, {(1,1),(2,2),(2,3)})
        if what_happened == True:
            print("R is an equivalence relation")
        else:
            print("R is not an equivalence relation because it is (at least) not "+ f"{what_happened}")
        print(f"R = {{('a','a'),('b','b'),('c','c'),('b','c'),('c','b')}}, S = {{'a','b','c'}}")
        what_happened = is_equivalence_relation({'a','b','c'}, {('a','a'),('b','b'),('c','c'),('b','c'),('c','b')})
        if what_happened == True:
            print("R is an equivalence relation")
        else:
            print("R is not an equivalence relation because it is (at least) not "+ f"{what_happened}")
        print()
    
    if choice == 5: # poset?
        print("5)")
        print(f"R = {{(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)}}, S = {{1, 2, 3, 4}}")
        what_happened = is_equivalence_relation({1, 2, 3, 4}, {(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)})
        if what_happened == True:
            print("R is an equivalence relation")
        else:
            print("R is not an equivalence relation because it is (at least) not "+ f"{what_happened}")
        print(f"R = {{(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)}}, S = {{0, 1, 2, 3}}")
        what_happened = is_equivalence_relation({0, 1, 2, 3}, {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)})
        if what_happened == True:
            print("R is an equivalence relation")
        else:
            print("R is not an equivalence relation because it is (at least) not "+ f"{what_happened}")
        print()

for i in range(1,6):
    main(i)
