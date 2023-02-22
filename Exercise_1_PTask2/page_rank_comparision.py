import networkx as nx
from matplotlib import pyplot as plt


er_graph = nx.erdos_renyi_graph(10, 0.3)
ba_graph = nx.barabasi_albert_graph(10, 2)

nx.draw(ba_graph)
plt.show()


er_rank = nx.pagerank(er_graph)
print(er_rank)

ba_rank = nx.pagerank(ba_graph)
print(ba_rank)