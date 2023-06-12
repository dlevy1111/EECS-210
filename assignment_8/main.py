import networkx as nx # using a library because it makes things very easy
from nim import Board, isValid # https://github.com/kevinyang372/Nim
import random

'''
Name of program: Assignment 8
Description: This program shows my understanding of graphs
Inputs: None
Outputs: Text
Author's name: David Levy
Creation date: Apr. 29
'''

def euler_circuit(graph): # euler graph stuff
    G = nx.Graph()
    G.add_edges_from(graph)
    if nx.is_eulerian(G): # if our graph is eulerian, then we find an euler circuit
        print("This graph is eulerian")
        path = list(nx.eulerian_circuit(G, 1))
        circuit = ""
        for vertex in path: # formatting the circuit
            circuit = circuit + "-" + str(vertex[0])
        circuit = circuit + "-" + str(path[0][0])
        print(circuit[1:]) # printing the circuit
    else:
        odd_vertices = [] # the graph is not eulerian
        for vertex in G.degree():
            if vertex[1] % 2 == 1:
                odd_vertices.append(vertex[0]) # adding vertices with odd degrees to a list
        print("This graph is not eulerian")
        print("This graph has odd nodes:", odd_vertices) # printing that list

def euler_circuit2(graph):
    degrees_of_nodes = {}
    for item in graph:
        for node in item:
            if node not in degrees_of_nodes.keys():
                degrees_of_nodes[node] = 1
            else:
                degrees_of_nodes[node] += 1
    odd_degrees = []
    for node in degrees_of_nodes.keys():
        if degrees_of_nodes[node] % 2 == 1:
            odd_degrees.append(node)
    if len(odd_degrees) > 0:
        print("There is no eulerian circuit")
    else:
        print("There is an eulerian circuit:")
        print(find_eulerian_circuit(graph, (str(graph[0][0])+str(graph[0][1]))))
    

def find_eulerian_circuit(graph: list, circuit: str):

    if len(graph) == 1:
        circuit = str(graph[0][0])+str(graph[0][1])
        return circuit
    else:
        for i in range(0,len(graph)-1):
            print(circuit[len(circuit)-1] == str(graph[i][0]))
            if circuit[len(circuit)-1] == str(graph[i][0]):
                circuit = circuit + str(graph[i][1])
                graph.remove(graph[i])
                circuit = circuit + str(find_eulerian_circuit(graph, circuit))
                return circuit
            if circuit[len(circuit)-1] == graph[i][1]:
                try:
                    circuit = str(graph[i][0]) + str(find_eulerian_circuit(graph.remove(graph[i]), circuit))
                    return circuit
                except:
                    continue
        
    return

def dirac_theorem(graph): # dirac's theorem stuff
    G = nx.Graph()
    G.add_edges_from(graph) # making the graph into a graph object
    n = len(G.nodes())
    if n >= 3: # applying dirac's theorem
        hamilton = True
        for vertex in G.degree():
            if vertex[1] <= n/2: # more application of dirac's theorem
                hamilton = False
        if hamilton == True:
            print("This graph has a hamilton circuit")
        else:
            print("It is unclear whether this graph has a hamilton circuit")

def ore_theorem(graph): # ore's theorem stuff
    G = nx.Graph()
    G.add_edges_from(graph) # assembling graph

    n = len(G.nodes()) # number of nodes
    vertices = list(G.nodes()) # a list of all of the nodes
    degrees = dict(G.degree()) # a dictionary containing the degrees of all of the nodes
    deg_u_plus_deg_v = [] # an empty list for placing degrees
    non_adjacent_vertices = list(nx.non_neighbors(G, vertices[0]))

    for vertex in non_adjacent_vertices:
        deg_u_plus_deg_v.append(degrees[vertices[0]] + degrees[vertex]) # calculating degrees of non adjacent vertices

    hamilton = True
    for degree in deg_u_plus_deg_v: 
        if degree < n: # working out whether or not our graph has a hamilton circuit
            hamilton = False
    if hamilton == True:
        print("This graph has a hamilton circuit") # telling the user
    else:
        print("It is unclear whether this graph has a hamilton circuit")

def nim(num_piles: int, sticks_per_pile: list, just_print_tree: bool, A_goes_first: bool): # this nim script has been adapted from kevinyang372's github. thank you kevin.
    # initializing size of the game board
    ele = num_piles
    lis = sticks_per_pile
    game = Board(lis)

    print("Start %s" % (game.board), )

    if just_print_tree == False:
        if A_goes_first: # game start stuff
            print("A goes first")
        else:
            print("B goes first")
        player_win = True
        while True:
            if A_goes_first == False:
                # player B's turn
                user = f"{random.randint(0,3)} {random.randint(0,3)}" # randomly picking B's moves
                player_remove = [int(i) for i in user.split(' ')]

                while not isValid(player_remove, game.board): # changing B's move in case it doesn't work
                    user = f"{random.randint(0,3)} {random.randint(0,3)}"
                    player_remove = [int(i) for i in user.split(' ')]
                game.update(player_remove[1], player_remove[0])
                print(f"B's turn,", game.board)
                if sum(game.board) == 0:
                    player_win = False # win conditions
                    break
                elif sum(game.board) == 1:
                    break

            game.computerUpdate(just_print_tree) # since A uses the minmax strategy, we can just send A's move to the built in function
            print("A's turn,", game.board)
            
            if A_goes_first == True: # the case that A goes first
                A_goes_first = False
                # player B's turn
                user = f"{random.randint(0,3)} {random.randint(0,3)}" # randomly picking B's moves
                player_remove = [int(i) for i in user.split(' ')]
                while not isValid(player_remove, game.board): # changing B's move in case it doesn't work
                    user = f"{random.randint(0,3)} {random.randint(0,3)}"
                    player_remove = [int(i) for i in user.split(' ')]
                game.update(player_remove[1], player_remove[0]) # update nim  by player B's moves
                print(f"B's turn,", game.board) # tell the user what B did

                if sum(game.board) == 0:
                    player_win = False # win conditions
                    break
                elif sum(game.board) == 1:
                    break
            else:
                A_goes_first == True
            if sum(game.board) == 0: # win conditions
                break
            elif sum(game.board) == 1:
                player_win = False
                break
        if player_win: # usage of the win conditions
            print(f"Because the board is now {game.board}, B won!")
            return "B"
        else:
            print(f"Because the board is now {game.board}, B lost!")
            return "A"

    else:
        game.computerUpdate(just_print_tree)


def main():
    for i in range(0,4):
        if i == 0:
            print("1)") # problem 1
            euler_circuit([("a","b"),("b","c"),("d","a"),("d","b"),("d","e"),("e","f"),("e","f"),("f","c"),("g","d"),("g","h"),("h","e"),("h","f"),("h","j"),("j","f")])
        if i == 1:
            print("2)") # problem 2
            dirac_theorem([("a","b"),("b","c"),("a","c"),("c","f"),("f","d"),("f","e"),("e","d")])
        if i == 2:
            print("3)") # problem 3
            ore_theorem([("a","b"),("b","c"),("a","c"),("c","f"),("f","d"),("f","e"),("e","d")])
        if i == 3:
            print("4a)") # problem 4a
            print_tree = True
            nim(3, [1, 2, 3], print_tree, True)
            print("4b)") # problem 4b
            print_tree = False
            wins = {"A": 0, "B": 0}
            for i in range(0, 100): # all 100 simulations
                A_starts = False
                if i % 2 == 0:
                    A_starts = True
                wins[nim(3, [1, 2, 3], print_tree, A_starts)]+=1
            print(wins)

# main()


euler_circuit2([(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),(1,9),(9,8),(1,4),(4,6),(6,8)])
