import networkx as nx
import pandas as pd
import pickle



#LOAD GRAPHS IN NETWORKX
#using an adjacency list
def load_from_adjlist(file):
    G1 = nx.read_adjlist('graphs/'+file)
    # print (nx.info(G1))
    return G1

#using an edgelist with weights
def load_from_edgelist(file):
    G2 = nx.read_edgelist('graphs/'+file, data=[('Weight', int)])
    print (nx.info(G2))
    print (G2.edges(data=True))
    return G2

#using a pandas dataframe
def load_from_pandas(file):
    df=pd.read_csv('graphs/'+file,delim_whitespace=True,header=None,names=['n1','n2','weight'])
    print (df.head(3))
    G3 = nx.from_pandas_edgelist(df,'n1','n2',edge_attr='weight')
    print (nx.info(G3))
    return G3

#using already available graphs
def load_karate_club():
    G=nx.karate_club_graph()
    G = nx.convert_node_labels_to_integers(G,first_label=1)
    return G

def load_from_pickle(picklefile):
    G = pickle.load(open('graphs/'+picklefile,'rb'))
    print (nx.info(G))
    return G