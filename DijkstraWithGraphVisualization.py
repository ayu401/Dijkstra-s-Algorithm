#Networkx library is a python package for creation and manipulation of complex networks/graphs
import networkx as nx 

# matplotlib.pyplot is a module within the Matplotlib library that provides a MATLAB-like plotting interface.
import matplotlib.pyplot as plt

#Creating an empty graph (Unidirected Graph)
G = nx.Graph() 

#Input the number of edges
num_edges = int(input("Enter the number of edges: "))

# Input the edges and their weights
for _ in range(num_edges): #The underscore _ is used as a placeholder variable when we don't intend to use the value being assigned to it.
    start,end,weight = input("Enter edge(start, end, weight): ").split()
    weight = int(weight)
    G.add_edge(start, end, weight=weight)

pos = nx.spring_layout(G) # spring_layout() Function to compute the positions of the nodes in the graph.
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=20, font_weight='bold') # draw() function to visualize the graph.

'''
with_labels=True: Indicates that we want to label the nodes in the graph.
node_size=700: Sets the size of the nodes in the graph.
node_color='skyblue': Sets the color of the nodes in the graph.
font_size=20: Sets the font size for the node labels.
font_weight='bold': Sets the font weight for the node labels.
'''

labels = nx.get_edge_attributes(G, 'weight') # use NetworkX's get_edge_attributes() function to get the edge weights as labels.
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) # use the draw_networkx_edge_labels() function to draw the edge labels on the graph.

plt.title('Graph Visualization') # title of the visualization window to 'Graph Visualization' using plt.title().
plt.show() # display the graph using Matplotlib's show() function.

# Input the start and end nodes for shortest path calculation
start_node = input("Enter a start node: ")
end_node = input("Enter the end node: ")

shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')

'''nx.shortest_path() function will find the shortest path between any two nodes in a graph, where
G is the empty graph that we created, A is the source node
E is the target node and weight holds the value of the edge weights
to do the computation'''

shortest_path_distance = nx.shortest_path_length(G, source=start_node, target=end_node, weight='weight')
#to find length of the shortest path

print("Shortest path:", shortest_path)
print("Total distance:", shortest_path_distance)



