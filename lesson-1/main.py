import connectivity as cn
import visualize as vis
import graphLoad as gl

if __name__ == "__main__":
    G=gl.load_karate_club()
    cn.find_periphery(G)
