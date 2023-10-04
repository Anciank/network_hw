import networkx as nx
import string
import matplotlib.pyplot as plt
import pandas as pd

G = nx.Graph()

hw_path ='/Users/anciank/Desktop/network_hw/hw1/HepTh.txt' 
f = open(hw_path, 'r')
for line in f:  #line :  3466 	937
    ids = line.split()   # ids = ['3466', '937']
    G.add_edge( int(ids[0]), int(ids[1]) )

#plt graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=False, node_size=1, node_color='b', alpha=0.6, width=0.1, arrows=False)
# plt.show()

#degree distribution
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)

plt.hist(degree_sequence, bins=range(min(degree_sequence), max(degree_sequence) + 1), density=True, alpha=0.75)
plt.xlabel("Degree (k)")
plt.ylabel("Probability (p(k))")
plt.title("Degree Distribution")
plt.show()


#number of nodes
print(len(G.nodes))

#number of edges
print(len(G.edges))

#diameter
connected_components = list(nx.connected_components(G))

max_diameter = 0

for component in connected_components:
    subgraph = G.subgraph(component)
    diameter = nx.diameter(subgraph)
    if diameter > max_diameter:
        max_diameter = diameter

print("Diameter of the graph:", max_diameter)