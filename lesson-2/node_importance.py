import networkx as nx
import graphLoad as gl
import operator


G = gl.load_karate_club()

def get_centrality_of_node(G,node):
    degCen = nx.degree_centrality(G)
    return degCen,degCen[node]

def get_centrality_of_directed(G):
    degOut = nx.out_degree_centrality(G)
    degIn = nx.in_degree_centrality(G)
    return degOut,degIn

def get_closeness_centrality(G,norm):
    return nx.closeness_centrality(G,wf_improved = True)

##if we want to find the centrality of a node which is somehow disconnected - problem
#in this case we use normalized = True

def get_bet_centrality(G,i):
    betCen = nx.betweenness_centrality(G,normalized=True,endpoints=False,k=i)
    return betCen

def get_n_highest_bet_Cen(G,n):
    betCen = get_bet_centrality(G,34)
    return (sorted(betCen.items(), key=operator.itemgetter(1),reverse=True))[:n]

def get_subset_centrality(G,s1,s2):
    subBetCen = nx.betweenness_centrality_subset(G,normalized=True)
    return subBetCen

def get_pagerank(G,dampingFactor):
    pRank = nx.pagerank(G,alpha=dampingFactor)
    return pRank

def get_hubs_authorities(G):
    h,a = nx.hits(G)
    return h,a