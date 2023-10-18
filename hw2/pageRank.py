import networkx as nx

# Create a graph
G = nx.DiGraph()  # You can use DiGraph for directed graphs or Graph for undirected graphs

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")

# Add edges
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")
G.add_edge("D", "C")

# Compute PageRank
pagerank = nx.pagerank(G)

# Print PageRank scores
for node, score in pagerank.items():
    print(f"Node: {node}, PageRank Score: {score}")
