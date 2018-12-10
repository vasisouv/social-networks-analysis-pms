import networkx as nx
import matplotlib.pyplot as plt
from parallel_between import plotBetweeness
from community_detect import detectCommunities


def main():
	G_fb = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype = int)
	print (nx.info(G_fb))

	#Creates the snapshot of the network
	spring_pos = nx.spring_layout(G_fb)
	plt.axis("off")
	nx.draw_networkx(G_fb, pos = spring_pos, with_labels = False, node_size = 35)
	plt.savefig("fbnetwork.png", format = "PNG")
	plt.show()
	plt.clf()

	plotBetweeness(G_fb, spring_pos)
	plt.clf()
	detectCommunities(G_fb, spring_pos)
	plt.clf()
	plt.close()

if __name__ == '__main__':
	main()