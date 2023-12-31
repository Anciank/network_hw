import networkx as nx

# Replace with the path to your TXT file
file_path = r'C:\Users\17311\Desktop\homework\net_homework\p2p-Gnutella04.txt'  
target_path = r'C:\Users\17311\Desktop\homework\net_homework\p2p-Gnutella04.gexf'

# Step 1: Read the TXT File (Assuming a simple format: "node1 node2")
def read_txt_file(txt_file):
    with open(txt_file, 'r') as file:
        lines = file.readlines()
    return [line.strip().split() for line in lines]

# Step 2: Create a Graph Data Structure
G = nx.Graph()

# Step 3: Add Nodes and Edges
for edge in read_txt_file(file_path):
    G.add_edge(edge[0], edge[1])

# Step 4: Write G into gexf file
nx.write_gexf(G, target_path)
