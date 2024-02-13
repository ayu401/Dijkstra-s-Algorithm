import networkx as nx #Networkx library is a python package for creation and manipulation of complex networks/graphs

G = nx.Graph() #Creating an empty graph (Unidirected Graph)
'''
Sample Input #1
G.add_edge('A', 'B', weight=8)
G.add_edge('A', 'C', weight=3)
G.add_edge('B', 'C', weight=4)
G.add_edge('B', 'D', weight=1)
G.add_edge('C', 'D', weight=5)
G.add_edge('C', 'E', weight=2)
G.add_edge('D', 'E', weight=9)'''

# Add edges with weights
# Sample input #2
G.add_edge('A', 'B', weight=2)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=6)
G.add_edge('C', 'D', weight=3)
G.add_edge('C', 'E', weight=5)
G.add_edge('D', 'E', weight=2)


'''Every line adds edges to the graph with a specfified weight, defining ths structure of the graph where 
nodes are connected by edges and each edge has a weight showing the
distance betweenn the nodes'''

shortest_path = nx.shortest_path(G, source='A', target='E', weight='weight') #find the shortest path

'''nx.shortest_path() function will find the shortest path between any two nodes in a graph, where
G is the empty graph that we created, A is the source node
E is the target node and weight holds the value of the edge weights
to do the computation'''

shortest_path_distance = nx.shortest_path_length(G, source='A', target='E', weight='weight')
#to find length of the shortest path

print("Shortest path:", shortest_path)
print("Total distance:", shortest_path_distance)



