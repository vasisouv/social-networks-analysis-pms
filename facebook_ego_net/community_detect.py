import networkx as nx
import matplotlib.pyplot as plt
import community

def detectCommunities(G_fb, layout):

	parts = community.best_partition(G_fb)
	values = [parts.get(node) for node in G_fb.nodes()]

	plt.axis("off")
	nx.draw_networkx(G_fb, pos = layout, cmap = plt.get_cmap("jet"), node_color = values, node_size = 35, with_labels = False)
	plt.savefig("communities.png", format = "PNG")
	plt.show()




