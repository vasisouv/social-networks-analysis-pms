import connectivity as cn
import visualize as vis
import graphLoad as gl

if __name__ == "__main__":
    G=gl.load_karate_club()
    cn.find_periphery(G)

    # clus_coef_v1(G)
    # clus_coef_v1(G2,False)
    # clus_coef_v2(G2)
    # create_tree(G)
    # find_shortest_path(G)
    # find_avg_distance(G)
    # find_avg_distance(J)
    # find_diameter(G)
    # find_diameter(J)
    # find_eccentricity(G)
    # find_eccentricity(J)
    # find_radius(G)
    # find_radius(J)
    # find_periphery(G)
    # find_central(graphLoad.load_karate_club())