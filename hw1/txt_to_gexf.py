import networkx as nx
import xml.etree.ElementTree as ET

# Step 1: Read the TXT File (Assuming a simple format: "node1 node2")
def read_txt_file(txt_file):
    with open(txt_file, 'r') as file:
        lines = file.readlines()
    return [line.strip().split() for line in lines]

# Step 2: Parse the Data
txt_file = '/Users/anciank/Desktop/network_hw/hw1/ca-GrQc.txt'  # Replace with the path to your TXT file
edge_data = read_txt_file(txt_file)

# Step 3: Create a Graph Data Structure
G = nx.Graph()

# Step 4: Add Nodes and Edges
for edge in edge_data:
    G.add_edge(edge[0], edge[1])

# Step 5: Generate GEXF File
root = ET.Element("gexf")
graph = ET.SubElement(root, "graph", mode="static", defaultedgetype="undirected")
nodes = ET.SubElement(graph, "nodes")
edges = ET.SubElement(graph, "edges")

for node_id in G.nodes(data=True):
    ET.SubElement(nodes, "node", id=node_id, label=str(node_id))

for source, target in G.edges():
    ET.SubElement(edges, "edge", source=source, target=target)

# Step 6: Write GEXF File
tree = ET.ElementTree(root)
gexf_file = 'output.gexf'  # Replace with the desired output file path
tree.write(gexf_file, encoding='utf-8', xml_declaration=True)

print(f"GEXF file '{gexf_file}' has been created.")
