# applies the Minimax and Alpha-beta pruning to find the best strategy

# decide based on the current state
def decide(state, alpha, beta, maxTurn, print_tree):
    # determining final state
    if (sum(state) == 1 and maxTurn) or (sum(state) == 0 and not maxTurn): return (-1, [state]) # base cases
    if (sum(state) == 1 and not maxTurn) or (sum(state) == 0 and maxTurn): return (1, [state])
    
    if maxTurn:
        res_max = -float('inf')
        res = None
        for i in find_next(state, maxTurn, print_tree):
            # recursively search for the next possible move
            val, temp = decide(i, alpha, beta, not maxTurn, print_tree)
            if val > res_max:
                res_max = val
                res = temp
            # update the upper bound
            alpha = max(alpha, val)
            # pruning
            if alpha >= beta:
                break
        # if print_tree == False:
        #     print(print(f"{[state]+res}"))
        return res_max, [state] + res
    else:
        res_min = float('inf')
        res = None
        for i in find_next(state, maxTurn, print_tree):
            val, temp = decide(i, alpha, beta, not maxTurn, print_tree)
            if val < res_min:
                res_min = val
                res = temp
            beta = min(beta, val)
            if alpha >= beta:
                break
        # if print_tree == False:
        #     print(print(f"removing {res_min} rocks from pile {state}, yielding {[state]+res}"))
        return res_min, [state] + res
    
# find all possible next moves
def find_next(state, maxTurn, print_tree):
    visited = set()
    res = []

    for i in range(len(state)):
        # print(f"{i}:")
        for m in range(1, state[i] + 1):
            # print(f"{m}:", end="")
            temp = list(state[:])
            temp[i] -= m
            
            # check if the stage already exists
            rearranged = tuple(sorted(temp))
            if rearranged not in visited:
                res.append(temp)
                visited.add(rearranged)
    if print_tree:
        turn = "max"
        if maxTurn == False:
            turn = "min"
        print(f"from state {state}, we get the following options in a {turn} branch:", res)
    return res
