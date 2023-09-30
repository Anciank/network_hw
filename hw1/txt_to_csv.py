file_path ='/Users/anciank/Desktop/network_hw/hw1/HepTh.txt' 
target_path = '/Users/anciank/Desktop/network_hw/hw1/HepTh.csv'

with open(file_path, 'r') as f:
    row = []
    for line in f:
        row.append(line.split('\t'))
    with open(target_path, 'w') as t:
        for r in row:
            t.write(r[0] + ',' + r[1])