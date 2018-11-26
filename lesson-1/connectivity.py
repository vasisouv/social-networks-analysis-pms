import networkx as nx
import graphLoad



'''CLUSTERING COEFFICIENT - tendency of nodes to create clusters'''

def clus_coef_v1(G,each_node): #Fraction of pairs of the node's friends that are friends with each other
    if each_node==True:
        for node in G.nodes():
            print (nx.clustering(G,node))
    print ('Average with v1:',nx.average_clustering(G))

def clus_coef_v2(G): #Ratio of numbers of triangles and number of "open triads"
    print ('Average with v2: ',nx.transitivity(G))

#Why do we have different values???
# ->transitivity: puts larger weight on higher degree nodes

'''DISTANCE - how far is node X from node Y'''
#path: sequence of nodes connected by an edge - number of steps it contains from beginning to the end
#breadth-first search - create a tree
def create_tree(G):
    nodes=list(G.nodes())
    print (type(G.nodes()))
    T=nx.bfs_tree(G,nodes[0])
    print (T.edges())
    return T

def find_shortest_path(G):
    nodes=list(G.nodes())
    print (nodes[0])
    sp = nx.shortest_path(G,nodes[0])
    sp_length=nx.shortest_path_length(G,nodes[0])
    # print (sp)
    # print (sp_length)
    return sp,sp_length

def find_avg_distance(G):
    try:
        avg = nx.average_shortest_path_length(G)
    except nx.NetworkXError:
        print ('Graph is not connected')
        avg=0
    print ('Average sp length:',avg)
    return avg

def find_diameter(G): #diameter: maximum distance between any pair of nodes
    try:
        d = nx.diameter(G)
    except nx.exception.NetworkXError:
        print ('Found infinite path length because the graph is not connected')
        d=0
    print ('diameter:',d)
    return (d)

def find_eccentricity(G): #eccentricity: the largest distance between n and all other nodes
    try:
        ecc = nx.eccentricity(G)
    except nx.exception.NetworkXError:
        print('Graph is not connected')
        ecc = 0
    print ('Eccentricity: ',ecc)
    return ecc

def find_radius(G):
    try:
        rad = nx.radius(G)
    except nx.exception.NetworkXError:
        print('Graph is not connected')
        rad = 0
    print ('Radius: ',rad)
    return rad

def find_periphery(G): #set of nodes that have the eccentricity equal to the diameter
    try:
        per = nx.periphery(G)
    except nx.exception.NetworkXError:
        print('Graph is not connected')
        per = {}
    print ('Periphery: ',per)
    return per

def find_central(G):
    try:
        cen = nx.center(G)
    except nx.exception.NetworkXError:
        print('Graph is not connected')
        cen = {}
    print ('Central: ',cen)
    return cen


'''CONNECTED GRAPHS
    Connected component:
    (i)Every node in the subset has a path to every other node
    (ii)No other node has a path to any node in the subset
'''
#check if a network is connected:
def is_connected(G):
    iscon = nx.is_connected(G)
    print (iscon)
    return iscon

def get_num_of_cc(G):
    print (nx.number_connected_components(G))
    return nx.number_connected_components(G)

def get_the_comps(G):
    print (sorted(nx.connected_components(G)))
    return (sorted(nx.connected_components(G)))

def get_nodes_cc(G,n):
    print (nx.node_connected_component(G,n))
    return (nx.node_connected_component(G,n))

'''for directed graphs - when are they connected?
A directed graph is strongly connected if for every pair of nodes u and v there is a directed path from u to v and 
a directed path from v to u
weakly connected: if replacing all directed edges to undirected produces a connected graph'''''

def is_strongly_connected(G):
    isStrongly = nx.is_strongly_connected(G)
    print (isStrongly)
    return isStrongly

def get_strong_con_comps(G):
    print (sorted(nx.strongly_connected_components(G)))
    return (sorted(nx.strongly_connected_components(G)))

def is_weakly_con(G):
    isWeak = nx.is_weakly_connected(G)
    print (isWeak)
    return isWeak

def get_weakly_con_comps(G):
    print (sorted(nx.weakly_connected_components(G)))
    return (sorted(nx.weakly_connected_components(G)))

'''NETWORK ROBUSTNESS - the ability of a network to maintain its general structural properties when it faces failures'''
def get_smallest_number_of_nodes_to_disconnect(G_un):
    print (nx.node_connectivity(G_un),nx.minimum_node_cut(G_un))
    return nx.node_connectivity(G_un), nx.minimum_node_cut(G_un)

def get_edges_to_remove_to_disconnect(G_un):
    print(nx.edge_connectivity(G_un), nx.minimum_edge_cut(G_un))
    return nx.edge_connectivity(G_un), nx.minimum_edge_cut(G_un)

#Robust networks have large minimum node and edge cuts

def find_simple_paths(G,n1,n2):
    print (sorted(nx.all_simple_paths(G,n1,n2)))
    return sorted(nx.all_simple_paths(G,n1,n2))

def find_which_nodes_and_edges_to_remove(G,n1,n2):
    a= nx.node_connectivity(G,n1,n2)
    b= nx.minimum_node_cut(G,n1,n2)
    c = nx.edge_connectivity(G,n1,n2)
    d = nx.minimum_edge_cut(G,n1,n2)
    print (a,b,c,d)
    return (a,b,c,d)