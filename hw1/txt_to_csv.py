file_path ='/Users/anciank/Desktop/network_hw/hw1/HepTh.txt' 
target_path = '/Users/anciank/Desktop/network_hw/hw1/HepTh.csv'

source_file = open(file_path, 'r')
target_file = open(target_path, 'w')

edges = []
for line in source_file:
    edges.append(line.split('\t'))

for edge in edges:
    target_file.write(edge[0] + ',' + edge[1])