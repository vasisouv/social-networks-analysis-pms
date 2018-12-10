import networkx as nx
import graphLoad as gl
import collections
import matplotlib.pyplot as plt
import operator
import community

# G = gl.load_karate_club()

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


def get_watts_strogatz(n,k,p):
    G = nx.watts_strogatz_graph(n,k,p)

def get_common_neighbors(G,node1,node2):
    cn = sorted(nx.common_neighbors(G,node1,node2))
    return cn

def get_jac_coef(G):
    jc = list(nx.jaccard_coefficient(G))
    jc.sort(key=operator.itemgetter(2),reverse=True)
    return jc

def get_resource_allocation(G):
    ra = list(nx.resource_allocation_index(G))
    ra.sort(key=operator.itemgetter(2),reverse=True)
    return ra

def get_adamic_adar(G):
    aa = list(nx.adamic_adar_index(G))
    aa.sort(key=operator.itemgetter(2),reverse=True)
    return aa

def get_prefer_att(G):
    pa = list(nx.preferential_attachment(G))
    pa.sort(key=operator.itemgetter(2),reverse=True)
    return pa

def get_communit_common(G):
    cc = list(nx.cn_soundarajan_hopcroft(G))
    cc.sort(key=operator.itemgetter(2),reverse=True)
    return cc

def get_community_resource_allocation(G):
    cra = list(nx.ra_index_soundarajan_hopcroft(G))
    cra.sort(key=operator.itemgetter(2), reverse=True)
    return cra

def get_communities(G):
    communities = community.best_partition(G)
    print (communities)

