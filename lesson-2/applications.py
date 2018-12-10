import networkx as nx
import graphLoad as gl
import collections
import matplotlib.pyplot as plt

G = gl.load_karate_club()

def plot_deg_distribution(G,loglog):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    if loglog==False:
        plt.plot(deg,cnt,label='PDF',color='orange')
        plt.ylabel('Count')
        plt.xlabel('Degree')
        plt.title('Degree Distribution')
        plt.legend()
        plt.show()
    else:
        # new_cnt = tuple(x + 1 for x in cnt)
        plt.plot(deg, cnt, label='PDF', color='orange')
        plt.ylabel('Count')
        plt.xlabel('Degree')
        plt.title('Degree Distribution')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend()
        plt.show()


def plot_deg_histogram(G):
    plt.hist(list(dict(nx.degree(G)).values()))
    plt.ylabel('Probability')
    plt.xlabel('Degree')
    plt.title('Degree Histogram')
    plt.show()

#If we want to plot the in or out degreee distribution we only need to change the G.degree to G.in_degree or G.out_degree

def get_barabasi_albert(num_of_nodes,attach_to_nodes):
    G = nx.barabasi_albert_graph(num_of_nodes,attach_to_nodes)
    return G

# plot_deg_distribution(get_barabasi_albert(100000,1),False)
