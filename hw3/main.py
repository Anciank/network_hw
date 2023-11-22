import networkx as nx
import itertools

def Girvan_Newman_communities(G):
    print("----GirvanNewman")
    commu = nx.community.girvan_newman(G)
    commu_G = tuple(sorted(c) for c in next(commu))
    print('There are ' + str(len(commu_G)) + ' communities in the network.')
    print(commu_G)
    print('The modularity score:' + str(nx.community.modularity(G,commu_G)))
    print('--------')

    # Export to Gephi-compatible format (gexf)
    export_filename = "girvan_newman_communities.gexf"
    export_community_structure(G, commu_G, export_filename)

def greedy_communities(G):
    print("----greedy")
    c = nx.community.greedy_modularity_communities(G)
    print('There are '+str(len(c))+' communities in the network.')
    for i, community in enumerate(c):
        print(f'community {i + 1}: {sorted(community)}')
    print('The modularity score:' + str(nx.community.modularity(G,c)))
    print('--------')

    # Export to Gephi-compatible format (gexf)
    export_filename = "greedy_communities.gexf"
    export_community_structure(G, c, export_filename)

def louvin_community(G):
    print("----louvin")
    commu_G = nx.community.louvain_communities(G, seed=123)
    print('There are '+str(len(commu_G))+' communities in the network.')
    print(commu_G)
    print('The modularity score:' + str(nx.community.modularity(G, commu_G)))
    print('--------')

    # Export to Gephi-compatible format (gexf)
    export_filename = "louvain_communities.gexf"
    export_community_structure(G, commu_G, export_filename)

def export_community_structure(G, communities, filename):
    mapping = {node: community_id for community_id, community in enumerate(communities) for node in community}
    nx.set_node_attributes(G, mapping, 'community')

    nx.write_gexf(G, filename)

if __name__ == '__main__':
    G = nx.Graph()
    for line in open('../hw1/HepTh.txt', 'r'):  #line :  3466 	937
        ids = line.split()   # ids = ['3466', '937']
        G.add_edge( int(ids[0]), int(ids[1]) )
        
    louvin_community(G)
    greedy_communities(G)
    Girvan_Newman_communities(G)
