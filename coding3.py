# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 3

# YOUR NAME:
# YOUR UNI:

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


##### Part A (a) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
int: number  of vertices , int: number  of edges , list: sorted  list of  degrees in ascending order.
'''
def graph_properties(G):
    # WRITE  YOUR  CODE  HERE
    
    num_edges = G.number_of_edges()
    num_vert = G.number_of_nodes()
    nodes = [G.degree[i] for  i  in G.nodes]
    nodes.sort()
    return num_vert, num_edges, nodes #number  of vertices , number  of edges , sorted  list of  degrees in ascending order.

##### Part A (b) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
boolean: True if handshake theorem is true, False if handshake theorem is false
.
'''
def verify_handshake(G):
    # WRITE  YOUR  CODE  HERE
    num_edges, nodes = graph_properties(G)[1:]
    
    if 2*num_edges != sum(nodes):
        return False

    return True #True or  False

##### Part A (c) #####
'''
Parameters:
G: a graph object of the class networkx

Returns: no return
'''
def plot_graph(G):
    # WRITE  YOUR  CODE  HERE
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

    return # No return

##### Part B (a) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
boolean: True if G is a true, False if not.
'''
def is_tree(G):
    # WRITE  YOUR  CODE  HERE
    try:
        nx.find_cycle(G, orientation='original')
        pass
    except:
        if nx.is_connected(G):
            return True
    return False # return True #True or  False

##### Part B (b) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
boolean: True if e <= 3v - 6, False otherwise
'''
def verify_planar_necessary_condition(G):
    # WRITE  YOUR  CODE  HERE
    verts, edges = graph_properties(G)[:2]
    if edges > 3*verts - 6:
        return False
    return True # True or False


##### Part B (c) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
boolean: True if Eulerian, False otherwise.
'''
def is_Eulerian(G):
    # WRITE  YOUR  CODE  HERE
    nodes = graph_properties(G)[2]
    for node in nodes:
        if node%2 != 0:
            return False
    return True # your checker result (True or False)

##### Part C (a) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
int: the index of category that G1 and G2 fall into
'''
def are_isomorphic(G1, G2):
    # WRITE  YOUR  CODE  HERE 
    # 

    verts1, edges1, nodes1 = graph_properties(G1)
    verts2, edges2, nodes2 = graph_properties(G2)

    if verts1 != verts2:
        return 1
    if edges1 != edges2:
        return 2
    if nodes1 != nodes2:
        return 3

    nodes1 = [G1.degree[i] for  i  in G1.nodes]
    nodes2 = [G2.degree[i] for  i  in G2.nodes]
    if  nodes1 != nodes2:
        return 4

    try:
        nx.find_cycle(G1, orientation='original')
        try:
            nx.find_cycle(G2, orientation='original')
            pass
        except:
            return 5
    except:
        try:
            nx.find_cycle(G2, orientation='original')
            return 5
        except:
            pass
    

    if nx.is_connected(G1) != nx.is_connected(G2):
        return 6

    return 7 # Index of Category the input graphs fit into

##### Part C (b) #####
'''
Parameters:
G: a graph object of the class networkx

Returns:
list: edge lists of the non-isomorphic graphs with four vertices
'''
def all_non_isomorphic_four():

    Gs = [nx.Graph() for i in range(11)]
    for i in range(11):
        for j in range(1,5):
            Gs[i].add_node(j)

    for i in range(1,11):
        Gs[i].add_edge(1, 2)

    Gs[2].add_edge(3, 4)
    Gs[3].add_edge(2, 3)
    Gs[4].add_edge(2, 3)
    Gs[4].add_edge(3, 4)
    Gs[5].add_edge(2, 3)
    Gs[5].add_edge(3, 1)
    Gs[6].add_edge(2, 3)
    Gs[6].add_edge(2, 4)
    Gs[7].add_edge(2, 3)
    Gs[7].add_edge(3, 4)
    Gs[7].add_edge(4, 1)
    Gs[8].add_edge(2, 3)
    Gs[8].add_edge(3, 4)
    Gs[8].add_edge(4, 2)
    Gs[9].add_edge(4, 1)
    Gs[9].add_edge(2, 3)
    Gs[9].add_edge(3, 4)
    Gs[9].add_edge(4, 2)
    Gs[10].add_edge(4, 1)
    Gs[10].add_edge(2, 3)
    Gs[10].add_edge(3, 4)
    Gs[10].add_edge(4, 2)
    Gs[10].add_edge(1, 3)

    edges =[]
    for G in Gs:
        tmp = []
        for i in G:
            for node in list(G.edges(i)):
                if node:
                    tmp.append(node)
 
        if tmp :
            edges.append(tmp)

        
    # for i in range(11):
    #     plot_graph(Gs[i])


    return edges # edge lists of all non-isomorphic  graphs  with  four  vertices

##### Part D (a) #####
'''
Returns:
networkx.Graph object
'''
def form_G_code():
    # WRITE YOUR CODE HERE  
    G = nx.Graph()
    G.add_node("graph_properties(G)")
    G.add_node("verify_handshake(G)")
    G.add_node("plot_graph(G)")
    G.add_node("is_tree(G)")
    G.add_node("verify_planar_necessary_condition(G)")
    G.add_node("is_Eulerian(G)")
    G.add_node("are_isomorphic(G)")
    G.add_node("all_non_isomorphic_four(G)")

    G.add_edge("graph_properties(G)", "verify_handshake(G)")
    G.add_edge("graph_properties(G)", "verify_planar_necessary_condition(G)")
    G.add_edge("graph_properties(G)", "is_Eulerian(G)")
    G.add_edge("graph_properties(G)", "graph_properties(G)")

    return G


'''
G: a graph object of the class networkx

Returns:
list, boolean, boolean, boolean, boolean, boolean: a list of graph properties [vertices, edges, and degree list from part A(a)] and 5 more Boolean values
'''
def explore_graph(G):
    # WRITE YOUR CODE HERE
    one, two, three, four, five, six = list(graph_properties(G)), False, False, False, False, False

    if is_tree(G):
        two = True
    if is_Eulerian(G):
        three = True
    if nx.is_connected(G):
        four = True
    try:
        nx.find_cycle(G, orientation='original')
        five = True
    except:
        pass
    if verify_planar_necessary_condition(G):
        six = True

    return one, two, three, four, five, six 
 

### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
if __name__ == '__main__':
    G1 = nx.Graph()
    G1.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (2, 6)])
    G2 = nx.Graph()
    G2.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (3, 6)])
    K_5 = nx.complete_graph(5)
    K_3_5 = nx.complete_bipartite_graph(3, 5)
    planar_graph = nx.dodecahedral_graph()
    print("#######################################")
    print("Welcome to Coding 3: Graph Theory!")
    print("#######################################")
    print()
    
    print("---------------------------------------")
    print("PART A: Basics in Graph theory")
    print("---------------------------------------")
    print("Part (a)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = graph_properties(G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", (6, 5, [1, 1, 1, 2, 2, 3]))
    print()
    print("Test Case 2: ")
    student_ans_2 = graph_properties(K_5)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", (5, 10, [4, 4, 4, 4, 4]))
    print("---------------------------------------")

    print("Part (b)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = verify_handshake(G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", True)
    print()
    print("Test Case 2: ")
    student_ans_2 = verify_handshake(K_5)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", True)
    print("---------------------------------------")

    print("Part (c)")
    print("---------------------------------------")
    # print("Test Case 1: ")
    # plot_graph(G2)

    # print()
    # print("Test Case 2: ")
    # plot_graph(K_5)
    print("---------------------------------------")
    
    print("---------------------------------------")
    print("PART B: Cycle, Connectivity and Special graphs")
    print("---------------------------------------")
    print("Part (a)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = is_tree(G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", True)
    print()
    print("Test Case 2: ")
    student_ans_2 = is_tree(K_5)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", False)
    print("---------------------------------------")

    print("Part (b)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = verify_planar_necessary_condition(planar_graph)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", True)
    print()
    print("Test Case 2: ")
    student_ans_2 = verify_planar_necessary_condition(G1)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", True)
    print("---------------------------------------")

    print("Part (c)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = is_Eulerian(G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", False)
    print()
    print("Test Case 2: ")
    student_ans_2 = is_Eulerian(K_5)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", True)
    print("---------------------------------------")

    
    print("---------------------------------------")
    print("PART C: Isomorphism")
    print("---------------------------------------")
    print("Part (a)")
    print("---------------------------------------")
    print("Test Case 1: ")
    student_ans_1 = are_isomorphic(G1, G1)
    print("Test Case 1 (Your Answer):", student_ans_1)
    print("Test Case 1 (Correct Answer):", 7)
    print()
    print("Test Case 2: ")
    student_ans_2 = are_isomorphic(G1, G2)
    print("Test Case 2 (Your Answer):", student_ans_2)
    print("Test Case 2 (Correct Answer):", 4)
    print("---------------------------------------")

    print("Part (b)")
    print("---------------------------------------")
    print(all_non_isomorphic_four())
    print("---------------------------------------")
    
    print("---------------------------------------")
    print("PART D: Your code is a graph")
    print("---------------------------------------")
    print("Part (a)")
    G_code = form_G_code()
    print("---------------------------------------")
    print("Part (b)")
    print("---------------------------------------")
    print(explore_graph(G_code))