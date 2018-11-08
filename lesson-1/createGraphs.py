import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite


# UNDIRECTED NETWORK
def create_undirected_graph():
    G = nx.Graph()
    G.add_node("a")
    G.add_nodes_from(["b", "c"])
    G.add_edge(1, 2)
    edge = ("d", "e")
    G.add_edge(*edge)
    edge = ("a", "b")
    G.add_edge(*edge)
    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())
    # adding a list of edges:
    G.add_edges_from([("a", "c"), ("c", "d"), ("a", 1), (1, "d"), ("a", 2)])
    print(G.edges())
    nx.draw(G, with_labels=True, pos=nx.spring_layout(G))
    plt.savefig("simple_undirected.png")  # save as png
    plt.show()  # display
    return G


# DIRECTED GRAPH
def create_directed_graph():
    D = nx.DiGraph()
    D.add_edge('B', 'A')
    D.add_edge('B', 'C')
    D.add_edges_from([('L', 'B'), ('A', 'L'), ('A', 'K'), ('K', 'L')])
    print("Nodes of graph: ")
    print(D.nodes())
    print("Edges of graph: ")
    print(D.edges())
    nx.draw(D, with_labels=True, pos=nx.spring_layout(D))
    plt.savefig("simple_directed.png")  # save as png
    plt.show()  # display
    return D


# WEIGHTED NETWORK
def created_weighted_graph():
    W = nx.Graph()
    W.add_edge('x', 'z', weight=6)
    W.add_edge('y', 'z', weight=3)
    W.add_edge('x', 'a', weight=4)
    W.add_edge('c', 'x', weight=2)
    print(W.edges())
    edgewidth = [d['weight'] for (u, v, d) in W.edges(data=True)]
    print(edgewidth)
    nx.draw(W, with_labels=True, pos=nx.spring_layout(W), width=edgewidth)
    plt.savefig("simple_weighted.png")  # save as png
    plt.show()  # display
    return W


# GRAPH WITH EDGE ATTRIBUTES
def create_graph_with_edge_attributes():
    R = nx.Graph()
    R.add_node('Ilias', role='male')
    R.add_node('George', role='male')
    R.add_node('Nick', role='male')
    R.add_node('Lisa', role='female')
    R.add_node('Rachel', role='female')
    R.add_node('Mary', role='female')
    R.add_edge('George', 'Lisa', relation='friend')
    R.add_edge('Ilias', 'Lisa', relation='friend')
    R.add_edge('Nick', 'Lisa', relation='couple')
    R.add_edge('Ilias', 'Rachel', relation='couple')
    R.add_edge('Lisa', 'Rachel', relation='family')
    R.add_edge('George', 'Ilias', relation='friend')
    R.add_edge('Ilias', 'Mary', relation='friend')
    colors = {'friend': 'g', 'couple': 'r', 'family': 'b'}
    edgewidth = [colors[d['relation']] for (u, v, d) in R.edges(data=True)]
    print(edgewidth)
    print(type(edgewidth))
    print(R.edges())
    nx.draw(R, with_labels=True, pos=nx.spring_layout(R), edge_color=edgewidth)
    plt.savefig("simple_attributed.png")  # save as png
    plt.show()  # display
    return R


# MULTIGRAPH
def create_multigraph():
    M = nx.MultiGraph()
    M.add_edge('George', 'Lisa', relation='friend')
    M.add_edge('George', 'Lisa', relation='family')
    M.add_edge('Nick', 'Lisa', relation='couple')
    M.add_edge('Ilias', 'Rachel', relation='couple')
    M.add_edge('Nick', 'Rachel', relation='friend')
    M.add_edge('Lisa', 'Rachel', relation='family')
    M.add_edge('George', 'Ilias', relation='friend')
    M.add_edge('Ilias', 'Mary', relation='friend')
    M.add_edge('George', 'Mary', relation='family')
    M.add_edge('George', 'Mary', relation='friend')
    colors = {'friend': 'g', 'couple': 'r', 'family': 'b'}
    edgewidth = [colors[d['relation']] for (u, v, d) in M.edges(data=True)]
    print(edgewidth)
    print(type(edgewidth))
    print(M.edges())
    nx.draw(M, with_labels=True, pos=nx.spring_layout(M), edge_color=edgewidth)
    # plt.savefig("multi_attributed.png") # save as png
    plt.show()  # display
    return M


####EDGE ATTRIBUTES###
def edge_node_attributes(R):
    # list all edges
    print(R.edges())
    # list all edges with attributes
    print(R.edges(data=True))
    # print the attributes of a specific edge
    print(R['Ilias']['Rachel'])
    # list all nodes
    print(R.nodes())
    # print all nodes with attributes
    print(R.nodes(data=True))
    # print node attribute
    print(R.node['Ilias']['role'])


# BIPARTITE GRAPHS### a graph whose nodes can be split into two sets L and R and every edge connects a node in L with
#  a node in R
def create_bipartite_graph():
    B = nx.Graph()
    B.add_nodes_from(['A', 'B', 'C', 'D', 'E'], bipartite=0)  # label one set of nodes 0
    B.add_nodes_from([1, 2, 3, 4], bipartite=1)  # label other set of nodes 1

    B.add_edges_from([('A', 1), ('B', 1), ('C', 1), ('D', 2), ('E', 3), ('E', 4)])  # adding edges

    # check if a graph is bipartite!!!

    print(bipartite.is_bipartite(B))
    # let's change something
    B.add_edge('A', 'B')
    print(bipartite.is_bipartite(B))
    B.remove_edge('A', 'B')

    # check if a set of nodes is part of bipartition -
    X = set([1, 2, 3, 4])
    print(bipartite.is_bipartite_node_set(B, X))
    return B


# PROJECTED GRAPHS
def create_projection(B):
    B.add_edges_from(
        [('D', 1), ('H', 1), ('B', 2), ('C', 2), ('D', 2), ('E', 2), ('G', 2), ('E', 3), ('F', 3), ('H', 3), ('J', 3),
         ('E', 4), ('I', 4), ('J', 4)])
    X = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    N = set([1, 2, 3, 4])
    P = bipartite.projected_graph(B, X)
    print(nx.info(P))
    P2 = bipartite.projected_graph(B, N)
    print(nx.info(P2))

    # if we want weights:
    P3 = bipartite.weighted_projected_graph(B, N)
    print(P3.edges(data=True))
    return P, P2, P3
