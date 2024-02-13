#Networkx library is a python package for creation and manipulation of complex networks/graphs
import networkx as nx 

#Creating an empty graph (Unidirected Graph)
G = nx.Graph() 

#Input the number of edges
num_edges = int(input("Enter the number of edges: "))

# Input the edges and their weights
for _ in range(num_edges): #The underscore _ is often used as a placeholder variable when you don't intend to use the value being assigned to it.
    start,end,weight = input("Enter edge(start, end, weight): ").split()
    weight = int(weight)
    G.add_edge(start, end, weight=weight)

# Input the start and end nodes for shortest path calculation
start_node = input("Enter a start node: ")
end_node = input("Enter the end node: ")

shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')

'''nx.shortest_path() function will find the shortest path between any two nodes in a graph, where
G is the empty graph that we created, source is the source node
target is the end node and weight holds the value of the edge weights
to do the computation'''

shortest_path_distance = nx.shortest_path_length(G, source=start_node, target=end_node, weight='weight')
#to find length of the shortest path

print("Shortest path:", shortest_path)
print("Total distance:", shortest_path_distance)



