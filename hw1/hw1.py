import networkx as nx
import string
import matplotlib.pyplot as plt
import pandas as pd

G = nx.Graph()

for line in open('hw1/HepTh.txt', 'r'):  #line :  3466 	937
    ids = line.split()   # ids = ['3466', '937']
    G.add_edge( int(ids[0]), int(ids[1]) )

def plot_pk_k():
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)

    plt.hist(degree_sequence, bins=range(min(degree_sequence), max(degree_sequence) + 1), 
            density=True, alpha=0.75)
    plt.xlabel("Degree (k)")
    plt.ylabel("Probability (p(k))")
    plt.title("Degree Distribution")
    plt.show()

def plot_degree_distribution():
    # Get the degrees of the nodes in the filtered graph
    degrees = [G.degree(node) for node in G.nodes()]

    # Create a histogram of the degree distribution
    plt.figure(figsize=(8, 6))
    plt.hist(degrees, bins=20, color='skyblue', alpha=0.7)
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title('Degree Distribution of Filtered Graph')
    plt.grid(True)
    plt.show()

def plot_G(filter_to):
    filtered_G = G.subgraph([node for node in G.nodes() if G.degree(node) > filter_to])
    pos = nx.spring_layout(filtered_G)
    plt.figure(figsize=(10, 6))
    nx.draw(filtered_G, pos, node_size=20,node_color='green')
    plt.title("Filtered Graph (Degree > 15) using Fruchterman-Reingold Layout")
    plt.show()

def print_node_num():
    #number of nodes
    print('number of nodes: ', len(G.nodes))

def print_edeg_num():
    #number of edges
    print('Number of edges: ', len(G.edges))

def print_diameter():
    #diameter
    print("Diameter of the graph:", 
        max([nx.diameter(G.subgraph(subGraph)) 
            for subGraph in list(nx.connected_components(G))]))