import networkx as nx

def custom_pagerank(graph, num_iterations=100, damping_factor=0.85):
    # Initialize PageRank scores for all nodes to 1/N, where N is the number of nodes in the graph
    N = len(graph)
    pagerank = {node: 1 / N for node in graph.nodes()}

    for _ in range(num_iterations):
        new_pagerank = {}
        total_pagerank = 0
        for node in graph.nodes():
            rank = (1 - damping_factor) / N
            for neighbor in graph.neighbors(node):
                rank += damping_factor * pagerank[neighbor] / len(list(graph.neighbors(neighbor)))
            new_pagerank[node] = rank
            total_pagerank += rank

        # Normalize the PageRank scores
        for node in graph.nodes():
            new_pagerank[node] /= total_pagerank

        pagerank = new_pagerank

    return pagerank

# Create a sample graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 2), (4, 2)])

# Calculate custom PageRank
custom_pagerank_scores = custom_pagerank(G)

# Print custom PageRank scores for each node
for node, score in custom_pagerank_scores.items():
    print(f"Node {node}: PageRank = {score:.4f}")
