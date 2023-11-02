import networkx as nx
import string
import matplotlib.pyplot as plt
import pandas as pd

G = nx.Graph()

hw_path =r'C:\Users\17311\Desktop\homework\net_homework\lastfm_asia_edges.txt' 
f = open(hw_path, 'r')
for line in f:  #line :  3466 	937
    ids = line.split(',')   # ids = ['3466', '937']
    G.add_edge( int(ids[0]), int(ids[1]) )

#plt graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=False, node_size=1, node_color='b', alpha=0.6, width=0.1, arrows=False)
# plt.show()

#degree distribution
#degree_sequence = sorted([d for n, d in G.degree()], reverse=True)

# Calculate the degree of each node
#degrees = dict(G.degree())


# print(nx.pagerank(G))
pagerankValues = nx.pagerank(G)

# Get the unique values and their counts
pageRank_values = list(pagerankValues.values())
unique_values = list(set(pageRank_values))
values_counts = [pageRank_values.count(d) for d in unique_values]

#print(pageRank_values)

# Create a scatter plot
plt.scatter(unique_values, values_counts, s=10,marker='o', c='b', label='pageRank Graph')

# Set labels and title
plt.xlabel('pageRank_values')
plt.ylabel('Count')
plt.title('pageRank Plot')

# Show the plot
plt.show()

# Show the legend
# plt.legend()

# plt.scatter()
# plt.xlabel("Degree (k)")
# plt.ylabel("Probability (p(k))")
# plt.title("Degree Distribution")
# plt.show()


#number of nodes
#print(len(G.nodes))

#number of edges
#print(len(G.edges))

#diameter
# connected_components = list(nx.connected_components(G))

# max_diameter = 0

# for component in connected_components:
#     subgraph = G.subgraph(component)
#     diameter = nx.diameter(subgraph)
#     if diameter > max_diameter:
#         max_diameter = diameter

# print("Diameter of the graph:", max_diameter)