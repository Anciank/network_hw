import networkx as nx
import string
import matplotlib.pyplot as plt
import pandas as pd

G = nx.Graph()

#create a graph
hw_path =r'C:\Users\17311\Desktop\homework\net_homework\p2p-Gnutella04.txt' 
f = open(hw_path, 'r')
for line in f:  #line :  3466 	937
    ids = line.split()   # ids = ['3466', '937']
    G.add_edge( int(ids[0]), int(ids[1]) )

dc = nx.algorithms.centrality.degree_centrality(G)

# Get the unique degrees and their counts
degree_values = list(dc.values())
unique_degrees = list(set(degree_values))
degree_counts = [degree_values.count(d) for d in unique_degrees]

# Create a scatter plot
plt.scatter(unique_degrees, degree_counts, s=10,marker='o', c='b', label='Degree Centrality')

# Set labels and title
plt.xlabel('Value')
plt.ylabel('Count')
plt.title('Degree Centrality Scatter Plot')

# Show the legend 图例
plt.legend()

# Show the plot
plt.show()