import connectivity as cn
import visualize as vis
import graphLoad as gl

if __name__ == "__main__":
    G = gl.load_karate_club()

    print (len(cn.find_periphery(G)))
    cn.clus_coef_v1(G, False)
    cn.clus_coef_v2(G)
    # cn.create_tree(G)
    # print (cn.find_shortest_path(G)[1])
    cn.find_avg_distance(G)
    cn.find_diameter(G)
    # cn.find_eccentricity(G)
    cn.find_radius(G)
    print (len(cn.find_central(G)))
    # vis.draw_graph(G)
