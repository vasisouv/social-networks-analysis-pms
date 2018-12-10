import networkx as nx
from multiprocessing import Pool
import itertools
import matplotlib.pyplot as plt


def partitions(nodes, n):
	"Partitions the nodes into n subsets"
	nodes_iter = iter(nodes)
	while True:
		partition = tuple(itertools.islice(nodes_iter,n))
		if not partition:
			return
		yield partition

def btwn_pool(G_tuple):
	return nx.betweenness_centrality_source(*G_tuple)


def between_parallel(G, processes = None):
	p = Pool(processes=processes)
	part_generator = 4*len(p._pool)
	node_partitions = list(partitions(G.nodes(), int(len(G)/part_generator)))
	num_partitions = len(node_partitions)

	bet_map = p.map(btwn_pool,
					zip([G]*num_partitions,
						[True]*num_partitions,
						[None]*num_partitions,
						node_partitions))

	bt_c = bet_map[0]
	for bt in bet_map[1:]:
		for n in bt:
			bt_c[n] += bt[n]
	return bt_c


#Runs the parallel betweenness algorithm on the network and plots the "top" vertices
def plotBetweeness(G_fb, layout, top = 10):

	bt = between_parallel(G_fb)

	max_nodes =  sorted(bt.items(), key = lambda v: -v[1])[:top]
	bt_values = [5]*len(G_fb.nodes())
	bt_colors = [0]*len(G_fb.nodes())
	for max_key, max_val in max_nodes:
		bt_values[max_key] = 150
		bt_colors[max_key] = 2

	plt.axis("off")
	nx.draw_networkx(G_fb, pos = layout, cmap = plt.get_cmap("rainbow"), node_color = bt_colors, node_size = bt_values, with_labels = False)
	plt.savefig("Between_network.png", format="PNG")
	plt.show()