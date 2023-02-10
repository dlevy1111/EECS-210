'''
Name: EECS 210 Assignment 2
Description: Shows understanding of predicate logic and (nested) quantifiers
Inputs: none
Outputs: text
My name: David Levy
Creation date: Jan 22
'''


def main(): # simple main function, loops through all possible options in both part one and two.
    options = "abcdef"
    for letter in options:
        part_one(letter)
        print()
    for letter in options:
        part_two(letter)
        print()


def part_one(letter):
    domain = [0,1,2,3,4,5,6,7,8,9,10]
    if letter == "a":# a) ∃x P(x), P(x) = “x<2”
        exp_xa = False # exp_x is ∃x P(x) for c
        for x in domain:
            if x > 2:
                exp_xa = True
                print(f"For 1a: ∃x(x>2) = {exp_xa}, due to {x}")
                break
    if letter == "b":# b) ∀x P(x), P(x) = “x<2” 
        axp_xb = True # axp_x is ∀x P(x) for b
        for x in domain:
            if not (x > 2):
                axp_xb = False
                print(f"For 1b: ∀x(x>2) = {axp_xb}, due to {x}")
                break
    if letter == "c": # c) ∃x (P(x) ∨ Q(x)), P(x) = “x<2”, Q(x) = “x>7”  
        exp_xc = False # same as the other two except for c
        for x in domain:
            if x < 2 or x > 7:
                exp_xc = True
                print(f"For 1c: ∃x(x<2 ∨ x>7) = {exp_xc}, due to {x}")
                break
    if letter == "d": # d) ∀x (P(x) ∨ Q(x)), P(x) = “x<2”, Q(x) = “x>7”  
        axp_xd = True # same as other stuff yeah
        for x in domain:
            if not (x < 2 or x > 7):
                axp_xd = False
                print(f"For 1d: ∀x(x<2 ∨ x>7) = {axp_xd}, due to {x}")
                break
    if letter == "e": # e) Prove De Morgan’s Law for ∃, P(x) = “x<5” 
        print("For 1e, ¬∃x(x<5)=∀x¬(x<5)=∀x(x>=5):")
        e1 = [] # ¬∃x(x<5)
        e2 = [] # ∀x(x>=5)
        for x in domain: # demorgan pt 1
            exp_xe1 = False
            if x < 5:
                exp_xe1 = True
            e1.append(not exp_xe1)
        for x in domain: # demorgan pt 2
            exp_xe2 = False
            if x >= 5:
                exp_xe2 = True
            e2.append(exp_xe2)
        print("¬∃x(x<5): ", e1)
        print("∀x(x>=5): ", e2)
    if letter == "f": # f) Prove De Morgan’s Law for ∀, P(x) = “x<5”  
        print("For 1f, ¬∀x(x<5)=∃x¬(x<5)=∃x(x>=5):")
        f1 = [] # ¬∀x(x<5)
        f2 = [] # ∃x(x>=5) 
        for x in domain: # demorgan pt 1
            exp_xf1 = True
            if x < 5:
                exp_xf1 = False
            f1.append(not exp_xf1)
        for x in domain: # demorgan pt 2
            exp_xf2 = True
            if x >= 5:
                exp_xf2 = False
            f2.append(exp_xf2)
        print("¬∃x(x<5): ", f1)
        print("∀x(x>=5): ", f2)


def part_two(letter):
    domain = [1,2,4,5,10,0.5,0.25,0.2,0.1] # x, y ∈ [1,2,4,5,10,0.5,0.25,0.2,0.1]
    output = []
    if letter == "a": # a) ∀x∀yP(x,y)
        for x in domain:
            for y in domain:
                if P(x,y) == False:
                    output.append((x,y))
        print(f"For 2a: ∀x∀yP(x,y) does not hold for these values of (x, y): {output}")
    if letter == "b": # b) ∀x∃yP(x,y)
        for x in domain:
            for y in domain: # lots of removal of unnecessary commands has led to this simple code
                if P(x,y):
                    output.append((x,y))
                    break
        print(f"For 2b: ∀x∃yP(x,y) holds for these values of (x, y): {output}")
    if letter == "c": # c) ∀y∃xP(x,y)
        for x in domain:
            for y in domain: # lots of removal of unnecessary commands has led to this simple code
                if P(x,y):
                    output.append((x,y))
                    break
        print(f"For 2c: ∀y∃xP(x,y) holds for these values of (y, x): {output}")
    if letter == "d": # d) ∃x∀yP(x,y)
        flag = False # if there does in fact exist an X that works, we raise this flag
        for x in domain:
            ay = True
            for y in domain:
                if not P(x,y):
                    ay = False
                    break
            if ay == False and flag == False: # if this value of x didn't work and the flag isn't raised, add back all the values in this iteration of x
                for y in domain:
                    output.append((x,y))
            else:
                print(f"For 2d: ∃x∀yP(x,y) is made true by x = {x}")
                flag = True
        if flag == False:
            print(f"For 2d: ∃x∀yP(x,y) does not hold for these values of (x,y): {output}")
    if letter == "e": # e) ∃y∀xP(x,y)
        flag = False # if there does in fact exist an X that works, we raise this flag
        for y in domain:
            ay = True
            for x in domain:
                if not P(x,y):
                    ay = False
                    break
            if ay == False and flag == False: # was there an x for all y? works like the flag above in "d"
                for y in domain:
                    output.append((x,y))
            else:
                print(f"For 2e: ∃y∀xP(x,y) is made true by x = {x}")
                flag = True
        if flag == False:
            print(f"For 2e: ∃y∀xP(x,y) does not hold for these values of (x,y): {output}")
    if letter == "f": # f) ∃x∃yP(x,y)
        for x in domain:
            for y in domain:
                if P(x,y): # very simple. if ever, we're good.
                    output.append((x,y))
        print(f"For 2f: ∃x∃yP(x,y) holds for these values of (x,y): {output}")



def P(x, y): # P(x,y) = "x*y = 1"
    return (x*y==1) # our sentence

main()
