import networkx as nx
import matplotlib.pyplot as plt
import graphLoad


# G=graphLoad.load_karate_club()

def draw_graph(G):
    plt.figure(figsize=(10,9))
    node_color = [G.degree(v) for v in G]
    node_size= [G.degree(v)*100 for v in G]
    pos1 = nx.circular_layout(G)
    pos2 = nx.fruchterman_reingold_layout(G)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,pos,alpha=0.7,with_labels=True,edge_color='.5',node_size=node_size,node_color=node_color,cmap=plt.cm.Blues)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# draw_graph(G)
