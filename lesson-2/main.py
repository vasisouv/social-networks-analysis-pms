import node_importance as ni
import graphLoad as gl
import createGraphs as cg
import applications as app

# G = gl.load_karate_club()
G1 = cg.create_directed_graph()

# if __name__ == "__main__":
    # degCen,dN =  (ni.get_centrality_of_node(G,34))
    # print (ni.get_centrality_of_directed(G1))
    # print (ni.get_closeness_centrality(G,True))
    # print(ni.get_bet_centrality(G))
    # print (ni.get_n_highest_bet_Cen(G,5))
    # s1=[34,33,21,30,16,27,15,23,10]
    # s2=[1,4,13,11,6,17,7]
    # pRank =  (ni.get_pagerank(G,0.8))
    # sortedpRank = sorted(pRank.items(), key=lambda x: x[1], reverse=True)
    # print (sortedpRank)
    # print (ni.get_hubs_authorities(G1)[0])
    # print(ni.get_hubs_authorities(G1)[1])
    # app.plot_deg_distribution(app.get_barabasi_albert(100000,1),False)
    # G = app.get_watts_strogatz()


