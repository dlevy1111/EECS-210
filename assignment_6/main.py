from sudokuer import Sudoker

'''
Name of Program: Assignment 6
Program Description: A recursion-with-backtracking solution to Sudoku
Inputs: Sudoku problems
Outputs: Text
Author's Name: David Levy
Creation Date: March 21
'''


def main():
    grids = [] # a 3d list! one dimension for each puzzle, 2 dimensions for the puzzle itself

    for q in range(1,6): # there are 5 puzzles, so we loop through [1,6)
        puzzle = []
        with open(f"puzzles/puzzle{q}.txt", "r") as textfile: # reading in each puzzle file, as well as removing spaces and new lines
            for line in textfile:
                temp_list = []
                for item in line:
                    if " " in item or "\n" in item: # as stated, removing
                        continue
                    else:
                        temp_list.append(item)
                puzzle.append(temp_list)
        grids.append(puzzle)
    
    for k in range(0, len(grids)): # triple loop!
        for i in range(0, len(grids[0])):
            for j in range(0, len(grids[0][0])): # turning all "_" into "0"
                if grids[k][i][j] == "_":
                    grids[k][i][j] = str(0)
    # print(grids)
    # print()
    

    a = Sudoker(grids[0]) # making Sudoker solver objects
    # b = Sudoker(grids[1])
    # c = Sudoker(grids[2])
    # d = Sudoker(grids[3])
    # e = Sudoker(grids[4])

    print("1)") # the output
    if a.solve() == False: # taking care of no solution cases. There will be nothing printed (None) if the solver doesn't yield anything
        print("No Solution")
    # print("2)")
    # if b.solve() == False:
    #     print("No Solution")
    # print("3)")
    # if c.solve() == False:
    #     print("No Solution")
    # print("4)")
    # if d.solve() == False:
    #     print("No Solution")
    # print("5)")
    # if e.solve() == False:
    #     print("No Solution")

main()