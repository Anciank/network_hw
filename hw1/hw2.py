import networkx as nx
import string
import matplotlib.pyplot as plt
import pandas as pd
# pageRank algorithm

G = nx.Graph()

hw_path =r'C:\Users\17311\Desktop\homework\net_homework\p2p-Gnutella04.txt' 
f = open(hw_path, 'r')
for line in f:  #line :  3466 	937
    ids = line.split()   # ids = ['3466', '937']
    G.add_edge( int(ids[0]), int(ids[1]) )

pagerankValues = nx.pagerank(G)

pageRank_values = list(pagerankValues.values())
unique_values = list(set(pageRank_values))
values_counts = [pageRank_values.count(d) for d in unique_values]

#print(pageRank_values)

# Create a scatter plot
plt.scatter(unique_values, values_counts, s=10,marker='o', c='b', label='pageRank value')
plt.xlabel('pageRank_values')
plt.ylabel('Count')
plt.title('pageRank Plot')
# show the legend
plt.legend()
# Show the plot
plt.show()